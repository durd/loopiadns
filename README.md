loopiadns
=========

Python-script using Loopias API to update DNS-records à la DynDNS

* Supports both IPv6 and IPv4
* Updates A/AAAA-records

Makes use of sockets and gets what IP was used to connect to ipv4.google.com and ipv6.google.com.
What server is used is changeable. However, consider the servers uptime and availability.

Requirements:
* DNS-records must be created in beforehand.
* An API-account for LoopiaAPI, this can be created in your Customer- or Reseller Zone.

More information about LoopiaAPI can be found here: https://www.loopia.com/api/

Of course, make the python-script executable and add it to your crontab.
`chmod +x loopiadns.py`
`@reboot                                 root    /bin/sleep 160 ; /usr/local/etc/ipv6_he-dyndns >/dev/null 2>&1
*/20       *       *       *       *       root    /usr/local/etc/ipv6_he-dyndns >/dev/null 2>&1`
