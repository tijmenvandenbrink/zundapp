===============
Project Zundapp
===============

This project periodically retrieves information from Cisco Prime Infra through their RESTful API. The main objectives:

 1. Periodic retrieval of data from 4 pre-defined reports in Cisco Prime Infra:
     1.1    Unique Clients Report
     1.2    Client Count Report
     1.3    Client Traffic Report
     1.4    Client Sessions Report
 2. Store calculated theoretical bandwidth available to clients connected to an access points (AP) at a certain time.


Process cycle
=============

Initial steps to take
=====================

     1. Define reports in Cisco Prime Infra 1.3 with the appropriate fields.
     1.1    Unique Clients Report
     1.2    Client Count Report
     1.3    Client Traffic Report
     1.4    Client Sessions Report

Continuous steps
================

     2. Periodic retrieval of data through RESTful API.
     3. Store calculated theoretical bandwidth available to clients connected to an access points (AP) at a certain time.

===================================
Define reports in Cisco Prime Infra
===================================

1.1 Unique Clients Report
=========================

This report displays all unique clients by the time, protocol, and controller filters that you select. A unique client is determined by the MAC address of the client device. These clients are sorted by controller in this report.

A new First Seen column is added in Release 6.0. It is the time that Prime Infrastructure first learned of the client MAC address. For existing clients, Prime Infrastructure sets the First Seen column with the timestamp currently in the database, which is the time the record was last updated.

Note: The Unique Client report covers any client that started the connection during the specified time period or ended the connection during the specified time period or connected during the specified time period. The specified time period refers to the reporting period that you specify while scheduling the report.

    * Host Name
    * AP MAC Address
    * IP Address—The IP address of the controller to which this client is associated.
    * Controller IP Address
    * Port
    * Global Unique—The aggregate global unicast address of an IPv6 address. This field is populated only if a client is assigned a global unique IPv6 address.
    * Local Unique—The local unicast address of an IPv6 address. This field is populated only if a client is assigned a local unique IPv6 address.
    * Link Local—The link local unicast address of an IPv6 address. This field is populated only if a client is assigned a link local IPv6 address.
    * Last Session Length
    * VLAN ID—The VLAN Identifier. The range is 1 to 4096.
    * CCX—The Cisco Client Extension version number.
    * E2E
    * Vendor—The vendor name for this client.
    * IP Address—The IP address of the client. This field displays IPv6 address for IPv6 clients and IPv4 address for IPv4 and dual stack clients.
    * AP Name—The access point to which this client is associated.
    * Controller—The name of the controller to which this client is associated.
    * 802.11 State—Client association status.
    * SSID—The SSID to which this client is associated.
    * Profile—The name of the profile to which this client is associated.
    * Authenticated
    * Protocol—802.11a, 802.11b, 802.11g, 802.11n_5 GHz, or 802.11b_2.4 GHz.
    * Map Location


The following METRICS will be provided by this model:

    * METRIC-1.-02 (# of unique users  WiFi (hourly basis))



1.2 Client Count Report
=======================

This trending report displays the total number of active clients on your wireless network.

The Client Count report displays data on the numbers of clients that connected to the network through a specific device, in a specific geographical area, or through a specific or multiple SSIDs.

The following are results for a Client Count report:

    * Client IP address
    * AP Name
    * Key
    * SSID
    * Date and time the count was taken
    * Associated client count
    * Authenticated client count


The following METRICS will be provided by this model:

    * METRIC-1.-03	(Hourly concurrent (WIFI) Users per AP (hourly))


1.3 Client Traffic Report
=========================
Total data volume per AP

This report displays the traffic by the wireless clients on your network.

# todo: This report isn't providing the data we expected. Check to see if we can use other data to provide this information

The following METRICS will be provided by this model:

    * METRIC-1.-04	(Total data volume per AP (hourly))


1.4 Client Session Report
=========================

This report provides client sessions for the given period of time. It displays the history of client sessions, statistics, and the duration at which clients are connected to an access point at any given period of time.

The following fields need to be configured:

    * Host Name—The DNS hostname of the device the client is on. Prime Infrastructure performs a DNS lookup to resolve the hostname from the IP address of the client. The IP address to hostname mapping must be defined in a DNS server. By default, the hostname lookup is disabled. Use Administration > Settings > Clients to enable hostname lookup.
    * Client Type
    * Global Unique—The aggregate global unicast address of an IPv6 address. This field is populated only if a client is assigned a global unique IPv6 address.
    * Local Unique—The local unicast address of an IPv6 address. This field is populated only if a client is assigned a local unique IPv6 address.
    * Link Local—The link local unicast address of an IPv6 address. This field is populated only if a client is assigned a link local IPv6 address.
    * Speed
    * CCX—The Cisco Client Extension version number.
    * AP MAC Address
    * IP address—The IP address of the client. This field displays IPv6 address for IPv6 clients and IPv4 address for IPv4 and dual stack clients.
    * AP Radio—The radio type of the access point.
    * Device IP Address—The IP address of the device to which this client is associated.
    * Port—The port number for the device to which this client is associated.
    * Anchor Controller—The IP address of the anchor or foreign controller for the mobility client.
    * Association ID—The association ID used for the client session.
    * Disassociation Time—The date and time this client disassociated.
    * Authentication—The authentication method for this client.
    * Encryption Cypher—Encryption cypher used in this client session.
    * EAP Type—EAP type used in this client session.
    * Authentication Algorithm—Authentication algorithm used in this client session.
    * Web Security—Web security used in this client session.
    * Bytes Sent (MB)—The approximate number of bytes transmitted during the session.
    * Bytes Received (MB)—The approximate number of bytes received during the session.
    * Packet Sent
    * Packets Received
    * SNR (dBm)—Signal-to-noise ratio for this client session indicated in dBm.
    * RSSI—The Received Signal Strength Indicator in dBm.
    * Status—Associated or disassociated.
    * Reason—Reason for disassociation.
    * E2E—Version number or Not Supported.
    * Data Retries
    * RTS Retries

The following METRICS will be provided by this model:

    * METRIC-1.-01 (Hourly Volume Unique Users (overlap with 1.-05))
    * METRIC-1.-05 (Total data volume per unique user)
    * METRIC-1.-27 (Max Bandwidth per AP per hour (Ux: 16b))
    * METRIC-1.-28 (Max Bandwidth per user per AP per hour (Ux: 16a))

====================
Zundapp Installation
====================

Set environment variables
=========================

The following environment variables should be set:

::
    ZUNDAPPENV=<DEV|PROD>
    ZUNDAPPPATH=<project path>
    CISCOPIHOST=<ip address>
    CISCOPIUSER=<username>
    CISCOPIPASSWD=<password>

    ZUNDAPPDBNAME=<databasename>
    ZUNDAPPDBUSER=<databaseuser>
    ZUNDAPPDBPASSWORD=<databasepassword>


Virtualenv + Zundapp install
============================

::
    virtualenv zundapp-env
    git clone git://github.com/tijmenvandenbrink/zundapp.git

    source zundapp-env/bin/activate
    pip install -r zundapp/requirements/requirements.txt


Zundapp Development
===================

Syncing database:

::
    django-admin.py syncdb --settings=zundapp.settings.dev --pythonpath=$ZUNDAPPPATH



Zundapp Production
==================

Syncing database:

::
    django-admin.py syncdb --settings=zundapp.settings.prod --pythonpath=$ZUNDAPPPATH

    django-admin.py schemamigration apps.reports --initial --settings=zundapp.settings.prod --pythonpath=$ZUNDAPPPATH
    django-admin.py migrate apps.reports --settings=zundapp.settings.prod --pythonpath=$ZUNDAPPPATH



Cisco RESTful API
=================
Information regarding the RESTful API can be found on the Cisco Prime Infra server at the below url:

https://<host>/webacs/api/v1/