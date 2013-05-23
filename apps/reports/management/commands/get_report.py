import logging

import requests
from requests.auth import HTTPBasicAuth

from django.core.management.base import BaseCommand
from ....reports.models import ClientSession
from ....reports.utils import parse_datetime, get_env_variable

logger = logging.getLogger(__name__)


def get_report(report_title):
    """ Returns report data

    :param report_title: Name of the report
    :type report_title: string
    :returns: request.models.Response object
    """
    CISCOPIHOST = get_env_variable('CISCOPIHOST')
    CISCOPIUSER = get_env_variable('CISCOPIUSER')
    CISCOPIPASSWD = get_env_variable('CISCOPIPASSWD')

    URL = 'https://{}/webacs/api/v1/op/reportService/report'.format(CISCOPIHOST)
    PARAMS = {'reportTitle': report_title, 'async': 'False', }
    HEADERS = {'Accept': 'application/json'}

    logger.debug('Requesting data from endpoint: {}'.format(report_title))
    r = requests.get(URL, params=PARAMS, auth=HTTPBasicAuth(CISCOPIUSER, CISCOPIPASSWD), verify=False, headers=HEADERS)
    if not r.status_code == requests.codes.ok:
        logger.critical("We could not run the report: {} at {}".format(report_title), URL)
        r.raise_for_status()

    return r


def get_client_sessions():
    """

    """
    r = get_report('api-clientsessions')

    for session in r.json()['mgmtResponse']['reportDataDTO']['dataRows']['dataRow']:
        data = {}
        for record in session['entries']['entry']:
            data[record['attributeName']] = record['dataValue']

        #if data['sessionEndTime'] == '':
        #    logger.debug("Session hasn't ended yet. Will be added during next run if session has ended."
        #                 "[{} - {}]".format(data['clientUsername'], data['sessionStartTime']))
        #    continue

        sessionStartTime = parse_datetime(data['sessionStartTime'])
        sessionDuration = ''

        if not data['sessionEndTime'] == '':
            sessionEndTime = parse_datetime(data['sessionEndTime'])
            sessionDuration = (sessionEndTime - sessionStartTime).total_seconds()

        defaults = {'client_ip_address': data['clientIpAddress'],
                    'client_mac_address': data['clientMacAddress'],
                    'vendor': data['vendor'],
                    'ap_name': data['lradName'],
                    'device_name': data['deviceName'],
                    'map_location': data['location'],
                    'ssid': data['ssId'],
                    'profile': data['profileName'],
                    'vlan_id': data['clientVlanIdDisplay'],
                    'protocol': data['protocol'],
                    'session_duration': sessionDuration,
                    'policy_type': data['policyType'],
                    'avg_session_throughput': str(data['throughput']).translate(None, '< ,'),
                    'host_name': data['clientHostName'],
                    'client_type': data['className'],
                    'global_unique': data['globalUnique'],
                    'local_unique': data['localUnique'],
                    'link_local': data['linkLocal'],
                    'speed': data['speed'],
                    'ccx': data['ccxVersion'],
                    'ap_mac_address': data['associatedAP'],
                    'ap_ip': data['ipAddress'],
                    'ap_radio': data['apRadio'],
                    'device_ip': data['deviceIpAddress'],
                    'port': data['switchPortString'],
                    'anchor_controller': str(data['anchorControllerIpAddress']).translate(None, ' '),
                    'association_id': data['aidString'],
                    'disassociation_time': parse_datetime(data['sessionEndTime']),
                    'encryption_cipher': data['encryptionCypher'],
                    'eap_type': data['eapType'],
                    'authentication_algorithm': data['authenticationAlgorithm'],
                    'web_security': data['webSecurity'],
                    'bytes_sent': data['bytesSent'],
                    'bytes_received': data['bytesReceived'],
                    'packets_sent': data['packetsSent'],
                    'packets_received': data['packetsReceived'],
                    'snr': data['snr'],
                    'rssi': data['rssiString'],
                    'status': data['status'],
                    'reason': data['reasonMsg'],
                    'e2e': data['e2eVersion'],
                    'data_retries': data['clientDataRetriesString'],
                    'rts_retries': data['clientRtsRetriesString'],
                    'mobility_status': data['mobilityStatus'],
                    'network_access_id': data['pmipNai'],
                    'pmip_state': data['pmipState'],
                    'connected_interface': data['pmipInterface'],
                    'home_address': data['pmipHomeAddress'],
                    'access_technology_type': data['pmipAccessTechnology'],
                    'local_link_identifier': data['pmipLocalLinkId'],
                    'lma': data['pmipLmaName']
                    }

        cs, created = ClientSession.get_or_create(client_username=data['clientUsername'],
                                                  association_time=parse_datetime(data['sessionStartTime']),
                                                  defaults=defaults)

        if not created:
            cs.update(**defaults)


class Command(BaseCommand):
    args = 'report'
    help = ("Fetches predefined report from Cisco Prime Infra and imports it into the Zundapp database."
            "type can be: api-clientsessions, ..."
            )

    def handle(self, report, *args, **options):

        logger.debug('Running "{}" report from Cisco Prime Infra'.format(report))
        if report == 'api-clientsessions':
            get_client_sessions()
            logger.info('Running "{}" report finished successfully.')