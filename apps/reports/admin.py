from django.contrib import admin
from apps.reports.models import ClientSession


class ClientSessionAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'client_ip_address', 'client_mac_address', 'association_time',
                    'disassociation_time', 'vendor', 'ap_name', 'session_duration', 'avg_session_throughput',
                    'bytes_sent', 'bytes_received', 'packets_sent', 'packets_received', 'snr', 'rssi', 'status',
                    'reason', 'data_retries', 'rts_retries')
    list_filter = ('client_username', 'client_ip_address', 'client_mac_address', 'association_time',
                    'disassociation_time', 'vendor', 'ap_name', 'snr', 'rssi', 'status', )
    search_fields = ('client_username', 'client_ip_address', 'client_mac_address', 'ap_name')

admin.site.register(ClientSession)