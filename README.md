loopiadns
=========

Python-script using Loopias API to update DNS-records à la DynDNS

* Supports both IPv6 and IPv4
* Updates A/AAAA-records

Makes use of sockets and gets what IP was used to connect to ipv4.google.com and ipv6.google.com.
What server is used is changeable. However, consider the servers uptime and availability.

Note:
DNS-records must be created in beforehand.
