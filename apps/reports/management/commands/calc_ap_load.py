import logging
import sys
from datetime import datetime, timedelta

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.db.models import Q

from ....reports.models import ClientSession, AccessPointLoad
from ....reports.utils import get_mcs_index, get_available_bandwidth
from ....reports.report_settings import SAMPLE_INTERVAL, CALCULATE_AP_LOAD_LAG

logger = logging.getLogger(__name__)


def calculate_bandwidth(timestamp):
    """ Creates AccessPointLoad objects

    Cisco APs will share the bandwidth equally over all connected clients, meaning that clients in MCS index 0 are
    expensive because they require more airtime to get the same data throughput as a client in MCS index 7.
    The airtime index defines a client's share of airtime. Depending on the MCS index the client is in, it will need
    more airtime to get the same throughput as a client in a higher MCS index. A client in MCS index 0 would need a
    total of 0.1388 seconds to transfer 1Mbit. A client in MCS index 7 would only need 0.01385 seconds to transfer
    1 Mbit. See column "airtime index" in Table 1.

    If we want to calculate the max amount of data throughput for the users connected to a Cisco AP we would first need
    to know how many clients are connected and in which MCS index they are.

    Then we would calculate the amount of airtime the clients in a certain MCS index would require resulting in an equal
    data throughput for all clients. If we sum the product of airtime index and the number of clients we can calculate
    the number of seconds the clients would need to each transfer 1Mbit. See column "Sum airtime (s/Mbits)" in Table 1.

    Sum airtime = clients_MCS0 x a_MCS0 + clients_MCS1 x a_MCS1 + clients_MCS2 x a_MCS2 + clients_MCS3 x a_MCS3 +
                  clients_MCS4 x a_MCS4 + clients_MCS5 x a_MCS5 + clients_MCS6 x a_MCS6 + clients_MCS7 x a_MCS7

    With this total we can calculate the amount of airtime (See column "total airtime (%)) the clients in a particular
    MCS index will get and therefor how much data they can potentially transfer.

    The bandwidth available to a user can be calculated as follows:

    BW = (b_MCS0 x g) / clients_MCS0

    :param timestamp: timestamp for which the bw available to clients on a certain access point should be calculated
    :type timestamp: datetime
    """
    start = timestamp
    end = timestamp + timedelta(seconds=SAMPLE_INTERVAL)

    sessions = ClientSession.objects.filter(Q(association_time__lte=start,
                                              disassociation_time__gte=start, disassociation_time__lte=end) |
                                            Q(association_time__lte=start, disassociation_time__gte=end) |
                                            Q(association_time__gte=start, association_time__lte=end,
                                              disassociation_time__lte=end) |
                                            Q(association_time__lte=start, status='Associated') |
                                            Q(association_time__lte=end, status='Associated') |
                                            Q(association_time__gte=start, association_time__lte=end,
                                              disassociation_time__gte=end))

    data = {}
    for session in sessions:
        data.setdefault(session.ap_name, {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0})
        data[session.ap_name][get_mcs_index(session.rssi)] += 1

    for ap, stats in data.items():
        apl = AccessPointLoad(ap_name=ap,
                              timestamp=timestamp,
                              clients_mcs_0=stats[0],
                              clients_mcs_1=stats[1],
                              clients_mcs_2=stats[2],
                              clients_mcs_3=stats[3],
                              clients_mcs_4=stats[4],
                              clients_mcs_5=stats[5],
                              clients_mcs_6=stats[6],
                              clients_mcs_7=stats[7],
                              bandwidth_available=get_available_bandwidth(stats))

        try:
            apl.save()
        except IntegrityError, e:
            logger.debug("Duplicate entry exists: {}".format(e))


class Command(BaseCommand):
    args = 'start'
    help = "Calculates the bandwidth available to clients connected to a certain access point." \
           "format: 'YYYY-MM-dd HH:SS'"

    def handle(self, *args, **options):
        now = datetime.now().replace(second=0, microsecond=0)
        if 'start' in options:
            try:
                t = datetime.strptime(options['start'], '%Y-%m-%d %H:%M')
            except ValueError, e:
                logger.critical("ValueError: {}".format(e))
                logger.critical("Please provide a valid format (e.g. 2013-05-23 23:12)")
                sys.exit(1)
        else:
            t = now - timedelta(seconds=CALCULATE_AP_LOAD_LAG)

        while t <= now:
            logger.debug("Starting calculations for {} - {}".format(t.strftime('%a %b %d %H:%M %Y'),
                                                                    now.strftime('%a %b %d %H:%M %Y')))
            calculate_bandwidth(t)
            t += timedelta(seconds=SAMPLE_INTERVAL)