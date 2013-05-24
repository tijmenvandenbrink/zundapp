import logging
from datetime import datetime
import pytz
from decimal import *

from zundapp.settings.base import TIME_ZONE
from report_settings import RSSI_MCS_MAP, MCS_DATARATE_MAP, DEFAULT_AP_TYPE

logger = logging.getLogger(__name__)


def parse_datetime(s):
    """ Returns timezone aware datetime object (tz=utc).

    :param s: String representation of datetime object including a timezone (e.g. Fri May 17 13:49:45 CEST 2013)
    :type s: string
    :returns: datetime
    """
    naive = datetime.strptime("{} {}".format(" ".join(s.split()[:-2]), "".join(s.split()[-1:])), '%a %b %d %H:%M:%S %Y')
    local = pytz.timezone(TIME_ZONE)
    local_dt = local.localize(naive, is_dst=None)

    return local_dt.astimezone(pytz.utc)


def get_mcs_index(rssi, ap_type=DEFAULT_AP_TYPE):
    """ Returns the MCS index based on the RSSI value

    :params rssi: Received Signal Strength Indication for a client session
    :type rssi: int
    :params ap_type: Access point type (e.g. AIRONET1300, AIRONET2600), which can be defined in report_settings.py
    :type ap_type: String
    :returns: int
    """
    if not ap_type in RSSI_MCS_MAP.keys():
        logger.error("Please add the RSSI to MCS index specs for {} to report_settings.py".format(ap_type))
        logger.info("Using DEFAULT_AP_TYPE ({}) for calculations".format(DEFAULT_AP_TYPE))
        ap_type = DEFAULT_AP_TYPE

    MAP = RSSI_MCS_MAP[ap_type]

    if rssi >= MAP[7]:
        return 7
    elif MAP[7] > rssi >= MAP[6]:
        return 6
    elif MAP[6] > rssi >= MAP[5]:
        return 5
    elif MAP[5] > rssi >= MAP[4]:
        return 4
    elif MAP[4] > rssi >= MAP[3]:
        return 3
    elif MAP[3] > rssi >= MAP[2]:
        return 2
    elif MAP[2] > rssi >= MAP[1]:
        return 1
    elif rssi <= MAP[0]:
        return 0


def get_available_bandwidth(stats, ap_type=DEFAULT_AP_TYPE):
    """ Returns the bandwidth available per client connected to an access point.

    :params stats: Dictionary in the form {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}
    :type stats: dict
    :params ap_type: Access point type (e.g. AIRONET1300, AIRONET2600)
    :type ap_type: String
    :returns: Decimal
    """
    if not ap_type in MCS_DATARATE_MAP.keys():
        logger.error("Please add the MCS to DATARATE specs for {} to report_settings.py".format(ap_type))
        logger.info("Using DEFAULT_AP_TYPE ({}) for calculations".format(DEFAULT_AP_TYPE))
        ap_type = DEFAULT_AP_TYPE

    airtime_index = {}
    airtime = {}

    for k, v in MCS_DATARATE_MAP[ap_type].items():
        airtime_index[k] = 1.0 / v
        airtime[k] = airtime_index[k] * stats[k]

    airtime_total = 0
    for v in airtime.values():
        airtime_total += v

    # If there are no clients connected full bandwidth is available
    if airtime_total == 0:
        return Decimal(MCS_DATARATE_MAP[ap_type][7])
    else:
        for k, v in stats.items():
            if not v == 0:
                return Decimal((((stats[k] * airtime_index[k]) /
                                 airtime_total) * MCS_DATARATE_MAP[ap_type][k]) / stats[k])


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    import os
    from django.core.exceptions import ImproperlyConfigured

    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s env variable" % var_name
    raise ImproperlyConfigured(error_msg)


class CiscoPrimeResource():
    """ Get resources from Cisco Prime Infra API """

    def __init__(self, url, **params):
        self.url = 'https://{}{}'.format(get_env_variable('CISCOPIHOST'), url)
        self.params = params
        self.headers = {'Accept': 'application/json'}

    def get(self):
        """ Returns resources from Cisco Prime Infra API

        :returns: request.models.Response object
        """
        import requests
        from requests.auth import HTTPBasicAuth

        logger.debug('Requesting data from endpoint: {}'.format(self.url))
        r = requests.get(self.url, params=self.params, auth=HTTPBasicAuth(get_env_variable('CISCOPIUSER'),
                                                                          get_env_variable('CISCOPIPASSWD')),
                         verify=False, headers=self.headers)

        if not r.status_code == requests.codes.ok:
            logger.critical("We could not run the report: {} at {}".format(self.url))
            r.raise_for_status()

        return r