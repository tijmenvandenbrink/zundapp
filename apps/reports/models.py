from django.db import models


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


class AuthenticationSuccesRate(models.Model):
    """
        This model holds the Authentication success rate.
        We make a distinction between eligible and ineligible rejects.

        pct_accepted_clean = accepted / (accepted + eligible_rejected) * 100
        pct_rejected_clean = eligible_rejected / (accepted + eligible_rejected) * 100

        pct_accepted_total = accepted / (accepted + eligible_rejected + ineligible_rejected) * 100
        pct_rejected_total = (eligible_rejected + ineligible_rejected) /
                                                            (accepted + eligible_rejected + ineligible_rejected) * 100
    """
    hostname = models.CharField(max_length=50)
    timestamp = models.DateTimeField()
    accepted = models.PositiveIntegerField()
    eligible_rejected = models.PositiveIntegerField()
    ineligible_rejected = models.PositiveIntegerField()
    pct_accepted_clean = models.DecimalField(max_digits=5, decimal_places=2)
    pct_accepted_total = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        ordering = ['hostname', 'timestamp']
        unique_together = ("hostname", "timestamp")

    def __unicode__(self):
        return "{} - {}".format(self.hostname, self.timestamp)