from django.db import models


class UniqueClient(models.Model):
    """
        This model displays all unique clients by the time, protocol, and controller filters that you select.
        A unique client is determined by the MAC address of the client device.
    """
    pass


class ClientCount(models.Model):
    """
        This model displays the total number of active clients on your wireless network.

        The Client Count model displays data on the numbers of clients that connected to the network through a specific
        device, in a specific geographical area, or through a specific or multiple SSIDs.
    """
    pass


class ClientTraffic(models.Model):
    """

    """
    pass


class ClientSession(models.Model):
    """
        This model provides client sessions for the given period of time. It displays the history of client sessions,
        statistics, and the duration at which clients are connected to an access point at any given period of time.
    """
    client_username = models.CharField(max_length=100)
    client_ip_address = models.GenericIPAddressField(protocol='both')
    client_mac_address = models.CharField(max_length=17)
    association_time = models.DateTimeField()
    vendor = models.CharField(max_length=100, blank=True)
    ap_name = models.CharField(max_length=20)
    device_name = models.CharField(max_length=20)
    map_location = models.CharField(max_length=50)
    ssid = models.CharField(max_length=50)
    profile = models.CharField(max_length=50, blank=True)
    vlan_id = models.IntegerField()
    protocol = models.CharField(max_length=50)
    session_duration = models.PositiveIntegerField(blank=True)
    policy_type = models.CharField(max_length=20, blank=True)
    avg_session_throughput = models.DecimalField(max_digits=10, decimal_places=1)
    host_name = models.CharField(max_length=50, blank=True)
    client_type = models.CharField(max_length=20, blank=True)
    global_unique = models.CharField(max_length=50, blank=True)
    local_unique = models.CharField(max_length=50, blank=True)
    link_local = models.GenericIPAddressField(protocol='IPv6', blank=True, null=True)
    speed = models.CharField(max_length=20, blank=True)
    ccx = models.CharField(max_length=50, blank=True)
    ap_mac_address = models.CharField(max_length=17)
    ap_ip = models.GenericIPAddressField(protocol='both')
    ap_radio = models.CharField(max_length=50)
    device_ip = models.GenericIPAddressField(protocol='both')
    port = models.IntegerField(blank=True)
    anchor_controller = models.GenericIPAddressField(protocol='both', blank=True)
    association_id = models.PositiveIntegerField()
    disassociation_time = models.DateTimeField(blank=True, null=True)
    encryption_cipher = models.CharField(max_length=20, blank=True)
    eap_type = models.CharField(max_length=20, blank=True)
    authentication_algorithm = models.CharField(max_length=20, blank=True)
    web_security = models.CharField(max_length=20, blank=True)
    bytes_sent = models.PositiveIntegerField()
    bytes_received = models.PositiveIntegerField()
    packets_sent = models.PositiveIntegerField()
    packets_received = models.PositiveIntegerField()
    snr = models.PositiveIntegerField()
    rssi = models.IntegerField()
    status = models.CharField(max_length=20)
    reason = models.CharField(max_length=100, blank=True)
    e2e = models.CharField(max_length=20, blank=True)
    data_retries = models.PositiveIntegerField()
    rts_retries = models.PositiveIntegerField()
    mobility_status = models.CharField(max_length=20, blank=True)
    network_access_id = models.CharField(max_length=20, blank=True)
    pmip_state = models.CharField(max_length=20, blank=True)
    connected_interface = models.CharField(max_length=50, blank=True)
    home_address = models.CharField(max_length=50, blank=True)
    access_technology_type = models.CharField(max_length=50, blank=True)
    local_link_identifier = models.CharField(max_length=50, blank=True)
    lma = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['-association_time']
        unique_together = ('client_username', 'association_time')

    def __unicode__(self):
        return "{} - ({} - {})".format(self.client_username, self.association_time, self.disassociation_time)


class AccessPointLoad(models.Model):
    """
        This model holds the maximum bandwidth available to clients
        connected to a specific Access Point at a certain time.
    """
    ap_name = models.CharField(max_length=20)
    timestamp = models.DateTimeField()
    clients_mcs_0 = models.PositiveIntegerField()
    clients_mcs_1 = models.PositiveIntegerField()
    clients_mcs_2 = models.PositiveIntegerField()
    clients_mcs_3 = models.PositiveIntegerField()
    clients_mcs_4 = models.PositiveIntegerField()
    clients_mcs_5 = models.PositiveIntegerField()
    clients_mcs_6 = models.PositiveIntegerField()
    clients_mcs_7 = models.PositiveIntegerField()
    bandwidth_available = models.DecimalField(max_digits=10, decimal_places=1)

    class Meta:
        ordering = ['ap_name', 'timestamp']
        unique_together = ("ap_name", "timestamp")

    def __unicode__(self):
        return "{} - {}".format(self.ap_name, self.timestamp)