import logging

from django.core.management.base import BaseCommand
from ....reports.models import ClientSession
from ....reports.utils import parse_datetime
from ....reports.utils import CiscoPrimeResource

logger = logging.getLogger(__name__)


def get_client_sessions():
    """ Stores ClientSessions retrieved from Cisco Prime Infra """

    PARAMS = {'reportTitle': 'api-clientsessions', 'async': 'false', }
    report = CiscoPrimeResource('/webacs/api/v1/op/reportService/report', PARAMS)

    r = report.get()

    for session in r.json()['mgmtResponse']['reportDataDTO']['dataRows']['dataRow']:
        data = {}
        if not type(session) == dict:
            continue

        for record in session['entries']['entry']:
            if record['dataValue'] == 'N/A':
                data[record['attributeName']] = None
            else:
                data[record['attributeName']] = record['dataValue']

        sessionStartTime = parse_datetime(data['sessionStartTime'])

        defaults = {'client_ip_address': data['clientIpAddress'],
                    'client_username': data['clientUsername'],
                    'vendor': data['vendor'],
                    'ap_name': data['lradName'],
                    'device_name': data['deviceName'],
                    'map_location': data['location'],
                    'ssid': data['ssId'],
                    'profile': data['profileName'],
                    'vlan_id': data['clientVlanIdDisplay'],
                    'protocol': data['protocol'],
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

        if not data['sessionEndTime'] == '':
            defaults['disassociation_time'] = parse_datetime(data['sessionEndTime'])
            defaults['session_duration'] = (parse_datetime(data['sessionEndTime']) - sessionStartTime).total_seconds()
        else:
            logger.debug("Session is still ongoing: {} - {}".format(data['clientUsername'], data['sessionStartTime']))
            defaults['session_duration'] = 0

        cs, created = ClientSession.objects.get_or_create(client_mac_address=data['clientMacAddress'],
                                                          association_time=parse_datetime(data['sessionStartTime']),
                                                          defaults=defaults)

        if not created:
            for k, v in defaults.items():
                setattr(cs, k, v)
            cs.save()
            logger.info("Updated ClientSession object: {} - {} - {}".format(data.get('clientUsername', 'Unknown'),
                                                                            data['sessionStartTime'],
                                                                            data['sessionEndTime']))
        else:
            logger.info("Saved ClientSession object: {} - {} - {}".format(data.get('clientUsername', 'Unknown'),
                                                                          data['sessionStartTime'],
                                                                          data['sessionEndTime']))


class Command(BaseCommand):
    args = 'report'
    help = ("Fetches predefined report from Cisco Prime Infra and imports it into the Zundapp database."
            "type can be: api-clientsessions, ..."
            )

    def handle(self, report, *args, **options):
        logger.debug('Running "{}" report from Cisco Prime Infra'.format(report))
        if report == 'api-clientsessions':
            get_client_sessions()
            logger.info('Running "{}" report finished successfully.'.format(report))