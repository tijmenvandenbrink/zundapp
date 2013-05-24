from django.contrib import admin
from ..reports.models import ClientSession, AccessPoint, AccessPointLoad


class ClientSessionAdmin(admin.ModelAdmin):
    list_display = ('client_username', 'client_ip_address', 'client_mac_address', 'association_time',
                    'disassociation_time', 'vendor', 'ap_name', 'session_duration', 'avg_session_throughput',
                    'bytes_sent', 'bytes_received', 'packets_sent', 'packets_received', 'snr', 'rssi', 'status',
                    'reason', 'data_retries', 'rts_retries')
    list_filter = ('client_username', 'client_ip_address', 'client_mac_address', 'association_time',
                    'disassociation_time', 'vendor', 'ap_name', 'snr', 'rssi', 'status', )
    search_fields = ('client_username', 'client_ip_address', 'client_mac_address', 'ap_name')


class AccessPointAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'serial', 'ip_address', 'model', 'boot_version', 'software_version',
                    'controller_name', 'location', 'status', 'admin_status', 'uptime')
    list_filter = ('name', 'type', 'model', 'boot_version', 'software_version', 'status', 'admin_status')
    search_fields = ('name', 'type', 'model', 'boot_version', 'software_version')


class AccessPointLoadAdmin(admin.ModelAdmin):
    list_display = ('ap_name', 'timestamp', 'bandwidth_available', 'clients_mcs_0', 'clients_mcs_1', 'clients_mcs_2',
                    'clients_mcs_3', 'clients_mcs_4', 'clients_mcs_5', 'clients_mcs_6', 'clients_mcs_7')
    list_filter = ('ap_name', 'timestamp', )
    search_fields = ('ap_name', )


admin.site.register(ClientSession, ClientSessionAdmin)
admin.site.register(AccessPoint, AccessPointAdmin)
admin.site.register(AccessPointLoad, AccessPointLoadAdmin)