import logging

from django.core.management.base import BaseCommand

from ....reports.models import AccessPoint
from ....reports.utils import CiscoPrimeResource

logger = logging.getLogger(__name__)


def get_access_points():
    """ Stores access points retrieved from Cisco Prime Infra """
    PARAMS = {'.full': 'true', 'async': 'false', }
    access_points = CiscoPrimeResource('/webacs/api/v1/data/AccessPoints', PARAMS)

    r = access_points.get()

    for ap in r.json()['queryResponse']['entity']:
        data = ap['accessPointsDTO']
        defaults = {'admin_status': data['adminStatus'],
                    'boot_version': data['bootVersion'],
                    'client_count': data['clientCount'],
                    'client_count_2_4': data['clientCount_2_4GHz'],
                    'client_count_5': data['clientCount_5GHz'],
                    'controller_ip_address': data['controllerIpAddress'],
                    'controller_name': data['controllerName'],
                    'country_code': data['countryCode'],
                    'ethernet_mac': data['ethernetMac'],
                    'hreap_enabled': data['hreapEnabled'],
                    'ip_address': data['ipAddress'],
                    'location': data['location'],
                    'lwapp_uptime': data['lwappUpTime'],
                    'mac_address': data['macAddress'],
                    'model': data['model'],
                    'serial': data['serialNumber'],
                    'software_version': data['softwareVersion'],
                    'status': data['status'],
                    'type': data['type'],
                    'uptime': data['upTime'],
                    }

        access_point, created = AccessPoint.objects.get_or_create(name=data['name'], defaults=defaults)

        if not created:
            logger.debug('Access Point already exists. Updating it with latest information')
            for k, v in defaults.items():
                setattr(ap, k, v)
            ap.save()
        else:
            logger.info('Created new Access Point object: {}'.format(ap))


class Command(BaseCommand):
    args = ''
    help = "Fetches the Access Points managed by Cisco Prime Infra and imports them into the Zundapp database."

    def handle(self, *args, **options):
        logger.debug('Retrieving Access Points from Cisco Prime Infra')
        get_access_points()
        logger.info('Retrieved Access Points from Cisco Prime Infra')