# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
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

        # Adding model 'ClientTraffic'
        db.create_table(u'reports_clienttraffic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'reports', ['ClientTraffic'])

        # Adding model 'ClientSession'
        db.create_table(u'reports_clientsession', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client_username', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('client_ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('client_mac_address', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('association_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('vendor', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('ap_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('device_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('map_location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ssid', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('profile', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('vlan_id', self.gf('django.db.models.fields.IntegerField')()),
            ('protocol', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('session_duration', self.gf('django.db.models.fields.PositiveIntegerField')(blank=True)),
            ('policy_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('avg_session_throughput', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=1)),
            ('host_name', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('client_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('global_unique', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('local_unique', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('link_local', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('speed', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('ccx', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('ap_mac_address', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('ap_ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('ap_radio', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('device_ip', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('port', self.gf('django.db.models.fields.IntegerField')(blank=True)),
            ('anchor_controller', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, blank=True)),
            ('association_id', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('disassociation_time', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('encryption_cipher', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('eap_type', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('authentication_algorithm', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('web_security', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('bytes_sent', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('bytes_received', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('packets_sent', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('packets_received', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('snr', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('rssi', self.gf('django.db.models.fields.IntegerField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('reason', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('e2e', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('data_retries', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('rts_retries', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('mobility_status', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('network_access_id', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('pmip_state', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('connected_interface', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('home_address', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('access_technology_type', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('local_link_identifier', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('lma', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'reports', ['ClientSession'])

        # Adding unique constraint on 'ClientSession', fields ['client_username', 'association_time']
        db.create_unique(u'reports_clientsession', ['client_username', 'association_time'])

        # Adding model 'AccessPoint'
        db.create_table(u'reports_accesspoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('admin_status', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('boot_version', self.gf('django.db.models.fields.CharField')(max_length=25)),
            ('client_count', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('client_count_2_4', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('client_count_5', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('controller_ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39, null=True, blank=True)),
            ('controller_name', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('country_code', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('ethernet_mac', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('hreap_enabled', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('ip_address', self.gf('django.db.models.fields.GenericIPAddressField')(max_length=39)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('lwapp_uptime', self.gf('django.db.models.fields.BigIntegerField')()),
            ('mac_address', self.gf('django.db.models.fields.CharField')(max_length=17)),
            ('model', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=25)),
            ('serial', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('software_version', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('uptime', self.gf('django.db.models.fields.BigIntegerField')()),
        ))
        db.send_create_signal(u'reports', ['AccessPoint'])

        # Adding model 'AccessPointLoad'
        db.create_table(u'reports_accesspointload', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('ap_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')()),
            ('clients_mcs_0', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_1', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_2', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_3', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_4', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_5', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_6', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('clients_mcs_7', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('bandwidth_available', self.gf('django.db.models.fields.DecimalField')(max_digits=10, decimal_places=1)),
        ))
        db.send_create_signal(u'reports', ['AccessPointLoad'])

        # Adding unique constraint on 'AccessPointLoad', fields ['ap_name', 'timestamp']
        db.create_unique(u'reports_accesspointload', ['ap_name', 'timestamp'])


    def backwards(self, orm):
        # Removing unique constraint on 'AccessPointLoad', fields ['ap_name', 'timestamp']
        db.delete_unique(u'reports_accesspointload', ['ap_name', 'timestamp'])

        # Removing unique constraint on 'ClientSession', fields ['client_username', 'association_time']
        db.delete_unique(u'reports_clientsession', ['client_username', 'association_time'])

        # Deleting model 'UniqueClient'
        db.delete_table(u'reports_uniqueclient')

        # Deleting model 'ClientCount'
        db.delete_table(u'reports_clientcount')

        # Deleting model 'ClientTraffic'
        db.delete_table(u'reports_clienttraffic')

        # Deleting model 'ClientSession'
        db.delete_table(u'reports_clientsession')

        # Deleting model 'AccessPoint'
        db.delete_table(u'reports_accesspoint')

        # Deleting model 'AccessPointLoad'
        db.delete_table(u'reports_accesspointload')


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
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
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
            'bandwidth_available': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            'clients_mcs_0': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_1': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_2': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_3': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_4': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_5': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_6': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'clients_mcs_7': ('django.db.models.fields.PositiveIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        },
        u'reports.clientcount': {
            'Meta': {'object_name': 'ClientCount'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'reports.clientsession': {
            'Meta': {'ordering': "['-association_time']", 'unique_together': "(('client_username', 'association_time'),)", 'object_name': 'ClientSession'},
            'access_technology_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'anchor_controller': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'blank': 'True'}),
            'ap_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'ap_mac_address': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'ap_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'ap_radio': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'association_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'association_time': ('django.db.models.fields.DateTimeField', [], {}),
            'authentication_algorithm': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'avg_session_throughput': ('django.db.models.fields.DecimalField', [], {'max_digits': '10', 'decimal_places': '1'}),
            'bytes_received': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'bytes_sent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'ccx': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'client_ip_address': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'client_mac_address': ('django.db.models.fields.CharField', [], {'max_length': '17'}),
            'client_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'client_username': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'connected_interface': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'data_retries': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'device_ip': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39'}),
            'device_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'disassociation_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'e2e': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'eap_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'encryption_cipher': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'global_unique': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'home_address': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'host_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link_local': ('django.db.models.fields.GenericIPAddressField', [], {'max_length': '39', 'null': 'True', 'blank': 'True'}),
            'lma': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'local_link_identifier': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'local_unique': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'map_location': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'mobility_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'network_access_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'packets_received': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'packets_sent': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'pmip_state': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'policy_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'port': ('django.db.models.fields.IntegerField', [], {'blank': 'True'}),
            'profile': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'protocol': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'reason': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'rssi': ('django.db.models.fields.IntegerField', [], {}),
            'rts_retries': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'session_duration': ('django.db.models.fields.PositiveIntegerField', [], {'blank': 'True'}),
            'snr': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'speed': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'ssid': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'vendor': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'vlan_id': ('django.db.models.fields.IntegerField', [], {}),
            'web_security': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
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