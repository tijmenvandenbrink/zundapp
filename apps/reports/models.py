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
    client_ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    client_mac_address = models.CharField(max_length=17)
    association_time = models.DateTimeField()
    vendor = models.CharField(max_length=100, blank=True, null=True)
    ap_name = models.CharField(max_length=20)
    device_name = models.CharField(max_length=20, blank=True, null=True)
    map_location = models.CharField(max_length=100, blank=True, null=True)
    ssid = models.CharField(max_length=50)
    profile = models.CharField(max_length=50, blank=True, null=True)
    vlan_id = models.IntegerField(blank=True, null=True)
    protocol = models.CharField(max_length=50, blank=True, null=True)
    session_duration = models.PositiveIntegerField(blank=True)
    policy_type = models.CharField(max_length=20, blank=True, null=True)
    avg_session_throughput = models.DecimalField(max_digits=10, decimal_places=1)
    host_name = models.CharField(max_length=50, blank=True, null=True)
    client_type = models.CharField(max_length=20, blank=True, null=True)
    global_unique = models.CharField(max_length=50, blank=True, null=True)
    local_unique = models.CharField(max_length=50, blank=True, null=True)
    link_local = models.GenericIPAddressField(protocol='IPv6', blank=True, null=True)
    speed = models.CharField(max_length=20, blank=True, null=True)
    ccx = models.CharField(max_length=50, blank=True, null=True)
    ap_mac_address = models.CharField(max_length=17, blank=True, null=True)
    ap_ip = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    ap_radio = models.CharField(max_length=50, blank=True, null=True)
    device_ip = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    port = models.IntegerField(blank=True, null=True)
    anchor_controller = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    association_id = models.PositiveIntegerField(blank=True, null=True)
    disassociation_time = models.DateTimeField(blank=True, null=True)
    encryption_cipher = models.CharField(max_length=20, blank=True, null=True)
    eap_type = models.CharField(max_length=20, blank=True, null=True)
    authentication_algorithm = models.CharField(max_length=20, blank=True, null=True)
    web_security = models.CharField(max_length=20, blank=True, null=True)
    bytes_sent = models.PositiveIntegerField(blank=True, null=True)
    bytes_received = models.PositiveIntegerField(blank=True, null=True)
    packets_sent = models.PositiveIntegerField(blank=True, null=True)
    packets_received = models.PositiveIntegerField(blank=True, null=True)
    snr = models.PositiveIntegerField(blank=True, null=True)
    rssi = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    e2e = models.CharField(max_length=20, blank=True, null=True)
    data_retries = models.PositiveIntegerField(blank=True, null=True)
    rts_retries = models.PositiveIntegerField(blank=True, null=True)
    mobility_status = models.CharField(max_length=20, blank=True, null=True)
    network_access_id = models.CharField(max_length=20, blank=True, null=True)
    pmip_state = models.CharField(max_length=20, blank=True, null=True)
    connected_interface = models.CharField(max_length=50, blank=True, null=True)
    home_address = models.CharField(max_length=50, blank=True, null=True)
    access_technology_type = models.CharField(max_length=50, blank=True, null=True)
    local_link_identifier = models.CharField(max_length=50, blank=True, null=True)
    lma = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        ordering = ['-association_time']
        unique_together = ('client_mac_address', 'association_time')

    def __unicode__(self):
        return "{} - ({} - {})".format(self.client_username, self.association_time, self.disassociation_time)


class AccessPoint(models.Model):
    """
        Access point model
        https://<ip>/webacs/api/v1/data/AccessPoints?.full=true
    """
    admin_status = models.CharField(max_length=25)
    boot_version = models.CharField(max_length=25)
    client_count = models.PositiveIntegerField()
    client_count_2_4 = models.PositiveIntegerField()
    client_count_5 = models.PositiveIntegerField()
    controller_ip_address = models.GenericIPAddressField(protocol='both', blank=True, null=True)
    controller_name = models.CharField(max_length=25, blank=True, null=True)
    country_code = models.CharField(max_length=10, blank=True)
    ethernet_mac = models.CharField(max_length=17)
    hreap_enabled = models.BooleanField()
    ip_address = models.GenericIPAddressField(protocol='both')
    location = models.CharField(max_length=100)
    lwapp_uptime = models.BigIntegerField()
    mac_address = models.CharField(max_length=17)
    model = models.CharField(max_length=20)
    name = models.CharField(max_length=25, unique=True)
    serial = models.CharField(max_length=30)
    software_version = models.CharField(max_length=30)
    status = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    uptime = models.BigIntegerField()

    def __unicode__(self):
        return "{} ({})".format(self.name, self.type)


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
    total_clients = models.PositiveIntegerField()
    bandwidth_available = models.DecimalField(max_digits=10, decimal_places=2)
    snr_median = models.FloatField(blank=True, null=True)
    snr_mean = models.FloatField(blank=True, null=True)
    snr_std = models.FloatField(blank=True, null=True)
    snr_var = models.FloatField(blank=True, null=True)
    rssi_median = models.FloatField(blank=True, null=True)
    rssi_mean = models.FloatField(blank=True, null=True)
    rssi_std = models.FloatField(blank=True, null=True)
    rssi_var = models.FloatField(blank=True, null=True)
    ux_red = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ux_yellow = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    ux_green = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        ordering = ['ap_name', 'timestamp']
        unique_together = ("ap_name", "timestamp")

    def __unicode__(self):
        return "{} - {}".format(self.ap_name, self.timestamp)