import logging
import sys
from datetime import datetime, timedelta
import pytz
from optparse import make_option
from numpy import array, mean, var, std, median

from django.core.management.base import BaseCommand
from django.db import IntegrityError
from django.db.models import Q

from ....reports.models import ClientSession, AccessPoint, AccessPointLoad
from ....reports.utils import get_mcs_index, get_available_bandwidth, get_ux
from ....reports.report_settings import *
from zundapp.settings.base import TIME_ZONE

logger = logging.getLogger(__name__)


def calculate_bandwidth(timestamp, **options):
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

    sessions = ClientSession.objects.filter(avg_session_throughput__gte=BW_LOW_WATERMARK
                                            ).filter(Q(association_time__lte=start,
                                                       disassociation_time__gte=start, disassociation_time__lte=end) |
                                                     Q(association_time__lte=start, disassociation_time__gte=end) |
                                                     Q(association_time__gte=start, association_time__lte=end,
                                                       disassociation_time__lte=end) |
                                                     Q(association_time__lte=start, status='Associated') |
                                                     Q(association_time__lte=end, status='Associated') |
                                                     Q(association_time__gte=start, association_time__lte=end,
                                                       disassociation_time__gte=end))

    logger.debug("Found a total of {} concurrent sessions during {} - {}".format(len(sessions),
                                                                                 start.strftime('%a %b %d %H:%M %Y %Z'),
                                                                                 end.strftime('%a %b %d %H:%M %Y %Z')))

    data = {}
    for access_point in AccessPoint.objects.all():
        data.setdefault(access_point.name, {'clients': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0},
                                            'total_clients': 0,
                                            'snr': [],
                                            'rssi': [],
                                            'ux_red': 0.0,
                                            'ux_yellow': 0.0,
                                            'ux_green': 0.0})

    for session in sessions:
        data[session.ap_name]['clients'][get_mcs_index(session.rssi)] += 1
        data[session.ap_name]['total_clients'] += 1
        data[session.ap_name]['rssi'].append(session.rssi)
        data[session.ap_name]['snr'].append(session.snr)

        if session.snr <= SNR_LOW_WATERMARK:
            data[session.ap_name]['ux_red'] += 1
        elif SNR_LOW_WATERMARK < session.snr < SNR_HIGH_WATERMARK:
            data[session.ap_name]['ux_yellow'] += 1
        else:
            data[session.ap_name]['ux_green'] += 1

    for ap, stats in data.items():
        if len(stats['snr']) == 0:
            snr_median = snr_mean = snr_var = snr_std = None
        else:
            snr_median = median(array(stats['snr']))
            snr_mean = mean(array(stats['snr']))
            snr_var = var(array(stats['snr']))
            snr_std = std(array(stats['snr']))

        if len(stats['rssi']) == 0:
            rssi_median = rssi_mean = rssi_var = rssi_std = None
        else:
            rssi_median = median(array(stats['rssi']))
            rssi_mean = mean(array(stats['rssi']))
            rssi_var = var(array(stats['rssi']))
            rssi_std = std(array(stats['rssi']))

        ux = get_ux(stats['ux_red'], stats['ux_yellow'], stats['ux_green'], stats['total_clients'])

        apl = AccessPointLoad(ap_name=ap,
                              timestamp=timestamp,
                              clients_mcs_0=stats['clients'][0],
                              clients_mcs_1=stats['clients'][1],
                              clients_mcs_2=stats['clients'][2],
                              clients_mcs_3=stats['clients'][3],
                              clients_mcs_4=stats['clients'][4],
                              clients_mcs_5=stats['clients'][5],
                              clients_mcs_6=stats['clients'][6],
                              clients_mcs_7=stats['clients'][7],
                              total_clients=stats['total_clients'],
                              bandwidth_available=get_available_bandwidth(stats['clients']),
                              snr_median=snr_median,
                              snr_mean=snr_mean,
                              snr_std=snr_std,
                              snr_var=snr_var,
                              rssi_median=rssi_median,
                              rssi_mean=rssi_mean,
                              rssi_std=rssi_std,
                              rssi_var=rssi_var,
                              ux_red=ux['ux_red'],
                              ux_yellow=ux['ux_yellow'],
                              ux_green=ux['ux_green'],
                              )

        try:
            apl.save()
            logger.debug("Successfully saved AccessPointLoad object in database:"
                         " {} - BW available: {}".format(apl, apl.bandwidth_available))
        except IntegrityError, e:
            logger.debug("Duplicate entry exists: {}".format(e))
            if options['recalc']:
                logger.debug("Updating object with latest information (--recalc=True)")
                AccessPointLoad.objects.filter(ap_name=ap,
                                               timestamp=timestamp
                                               ).update(clients_mcs_0=stats[0],
                                                        clients_mcs_1=stats[1],
                                                        clients_mcs_2=stats[2],
                                                        clients_mcs_3=stats[3],
                                                        clients_mcs_4=stats[4],
                                                        clients_mcs_5=stats[5],
                                                        clients_mcs_6=stats[6],
                                                        clients_mcs_7=stats[7],
                                                        total_clients=stats['total_clients'],
                                                        bandwidth_available=get_available_bandwidth(stats),
                                                        snr_median=snr_median,
                                                        snr_mean=snr_mean,
                                                        snr_std=snr_std,
                                                        snr_var=snr_var,
                                                        rssi_median=rssi_median,
                                                        rssi_mean=rssi_mean,
                                                        rssi_std=rssi_std,
                                                        rssi_var=rssi_var,
                                                        ux_red=stats['ux_red'] / stats['total_clients'] * 100,
                                                        ux_yellow=stats['ux_yellow'] / stats['total_clients'] * 100,
                                                        ux_green=stats['ux_green'] / stats['total_clients'] * 100,
                                                        )


class Command(BaseCommand):
    args = '<start>'
    help = ("Calculates the bandwidth available to clients connected to a certain access point."
            " Provide date in format: 'YYYY-MM-dd HH:SS'")
    option_list = BaseCommand.option_list + (make_option('--start',
                                                         dest='start',
                                                         help=('Start calculating from this time. Provide datetime '
                                                               'in format: 2013-05-23 23:12')),
                                             make_option('--recalc',
                                                         action='store_true',
                                                         dest='recalc',
                                                         default=False,
                                                         help='Overwrite existing calculations.')
                                             )

    def handle(self, *args, **options):
        now = datetime.utcnow().replace(second=0, microsecond=0, tzinfo=pytz.utc)
        if options['start']:
            try:
                naive = datetime.strptime(options['start'], '%Y-%m-%d %H:%M')
                local = pytz.timezone(TIME_ZONE)
                local_dt = local.localize(naive, is_dst=None)
                t = local_dt.astimezone(pytz.utc)
            except ValueError, e:
                logger.critical("ValueError: {}".format(e))
                logger.critical("Please provide a valid format (e.g. 2013-05-23 23:12)")
                sys.exit(1)
        else:
            t = now - timedelta(seconds=CALCULATE_AP_LOAD_LAG)

        start = t
        logger.info("Running calc_ap_load starting from: {} till {}".format(t.strftime('%a %b %d %H:%M %Y %Z'),
                                                                            now.strftime('%a %b %d %H:%M %Y %Z')))
        while t <= now:
            logger.debug("Starting calculations for {} - {}".format(t.strftime('%a %b %d %H:%M %Y %Z'),
                                                                   (t + timedelta(seconds=SAMPLE_INTERVAL)
                                                                    ).strftime('%a %b %d %H:%M %Y %Z')))
            calculate_bandwidth(t, **options)
            t += timedelta(seconds=SAMPLE_INTERVAL)

        logger.info("Successfully ran calc_ap_load from: {} till {}".format(start.strftime('%a %b %d %H:%M %Y %Z'),
                                                                            now.strftime('%a %b %d %H:%M %Y %Z')))