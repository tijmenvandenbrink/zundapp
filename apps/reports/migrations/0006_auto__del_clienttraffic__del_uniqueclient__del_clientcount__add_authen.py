# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'ClientTraffic'
        db.delete_table(u'reports_clienttraffic')

        # Deleting model 'UniqueClient'
        db.delete_table(u'reports_uniqueclient')

        # Deleting model 'ClientCount'
        db.delete_table(u'reports_clientcount')

        # Adding model 'AuthenticationSuccesRate'
        db.create_table(u'reports_authenticationsuccesrate', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hostname', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('accepted', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('eligible_rejected', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('ineligible_rejected', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('pct_accepted_clean', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
            ('pct_accepted_total', self.gf('django.db.models.fields.DecimalField')(max_digits=5, decimal_places=2)),
        ))
        db.send_create_signal(u'reports', ['AuthenticationSuccesRate'])

        # Adding unique constraint on 'AuthenticationSuccesRate', fields ['hostname', 'timestamp']
        db.create_unique(u'reports_authenticationsuccesrate', ['hostname', 'timestamp'])


    def backwards(self, orm):
        # Removing unique constraint on 'AuthenticationSuccesRate', fields ['hostname', 'timestamp']
        db.delete_unique(u'reports_authenticationsuccesrate', ['hostname', 'timestamp'])

        # Adding model 'ClientTraffic'
        db.create_table(u'reports_clienttraffic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['ClientTraffic'])

        # Adding model 'UniqueClient'
        db.create_table(u'reports_uniqueclient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['UniqueClient'])

        # Adding model 'ClientCount'
        db.create_table(u'reports_clientcount', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['ClientCount'])

        # Deleting model 'AuthenticationSuccesRate'
        db.delete_table(u'reports_authenticationsuccesrate')


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
        u'reports.authenticationsuccesrate': {
            'Meta': {'ordering': "['hostname', 'timestamp']", 'unique_together': "(('hostname', 'timestamp'),)", 'object_name': 'AuthenticationSuccesRate'},
            'accepted': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'eligible_rejected': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'hostname': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ineligible_rejected': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pct_accepted_clean': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'pct_accepted_total': ('django.db.models.fields.DecimalField', [], {'max_digits': '5', 'decimal_places': '2'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
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
        }
    }

    complete_apps = ['reports']