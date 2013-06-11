# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'AccessPointLoad.total_clients'
        db.add_column(u'reports_accesspointload', 'total_clients',
                      self.gf('django.db.models.fields.PositiveIntegerField')(default=None),
                      keep_default=False)

        # Adding field 'AccessPointLoad.snr_median'
        db.add_column(u'reports_accesspointload', 'snr_median',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'AccessPointLoad.rssi_median'
        db.add_column(u'reports_accesspointload', 'rssi_median',
                      self.gf('django.db.models.fields.FloatField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'AccessPointLoad.ux_red'
        db.add_column(u'reports_accesspointload', 'ux_red',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'AccessPointLoad.ux_yellow'
        db.add_column(u'reports_accesspointload', 'ux_yellow',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)

        # Adding field 'AccessPointLoad.ux_green'
        db.add_column(u'reports_accesspointload', 'ux_green',
                      self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=5, decimal_places=2, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'AccessPointLoad.total_clients'
        db.delete_column(u'reports_accesspointload', 'total_clients')

        # Deleting field 'AccessPointLoad.snr_median'
        db.delete_column(u'reports_accesspointload', 'snr_median')

        # Deleting field 'AccessPointLoad.rssi_median'
        db.delete_column(u'reports_accesspointload', 'rssi_median')

        # Deleting field 'AccessPointLoad.ux_red'
        db.delete_column(u'reports_accesspointload', 'ux_red')

        # Deleting field 'AccessPointLoad.ux_yellow'
        db.delete_column(u'reports_accesspointload', 'ux_yellow')

        # Deleting field 'AccessPointLoad.ux_green'
        db.delete_column(u'reports_accesspointload', 'ux_green')


    models = {
        u'reports.accesspoint': {
            'Meta': {'object_name': 'AccessPoint'},
            'admin_status': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'boot_version': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'client_count': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'client_count_2_4': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'client_count_5': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'controller_ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'controller_name': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'country_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'ethernet_mac': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'hreap_enabled': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'lwapp_uptime': ('django.db.models.fields.BigIntegerField', [], {}),
            'mac_address': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '25'}),
            'serial': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'software_version': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'uptime': ('django.db.models.fields.BigIntegerField', [], {})
        },
        u'reports.accesspointload': {
            'Meta': {'ordering': "['ap_name', 'timestamp']", 'unique_together': "(('ap_name', 'timestamp'),)", 'object_name': 'AccessPointLoad'},
            'ap_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'bandwidth_available': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '2'}),
            'clients_mcs_0': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_1': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_2': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_3': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_4': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_5': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_6': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_7': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rssi_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rssi_median': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rssi_std': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'rssi_var': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snr_mean': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snr_median': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snr_std': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'snr_var': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {}),
            'total_clients': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ux_green': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ux_red': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'}),
            'ux_yellow': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '5', 'decimal_places': '2', 'blank': 'True'})
        },
        u'reports.clientcount': {
            'Meta': {'object_name': 'ClientCount'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.clientsession': {
            'Meta': {'ordering': "['-association_time']", 'unique_together': "(('client_mac_address', 'association_time'),)", 'object_name': 'ClientSession'},
            'access_technology_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'anchor_controller': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'ap_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'ap_mac_address': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'ap_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ap_radio': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'association_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'association_time': ('django.db.models.fields.DateTimeField', [], {}),
            'authentication_algorithm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'avg_session_throughput': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            'bytes_received': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'bytes_sent': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'ccx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'client_ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'client_mac_address': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'client_username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'connected_interface': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'data_retries': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'device_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'device_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'disassociation_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'e2e': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'eap_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'encryption_cipher': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'global_unique': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'home_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'host_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_local': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'lma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'local_link_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'local_unique': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'map_location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mobility_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'network_access_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'packets_received': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'packets_sent': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'pmip_state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'policy_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'rssi': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rts_retries': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'session_duration': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'snr': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'ssid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'vlan_id': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'web_security': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'reports.clienttraffic': {
            'Meta': {'object_name': 'ClientTraffic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.uniqueclient': {
            'Meta': {'object_name': 'UniqueClient'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['reports']