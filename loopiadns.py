#!/usr/local/bin/python
# -*- coding: utf-8 -*-  
  
import calendar  
import sys  
import time  
import xmlrpclib  
import socket

username  = '<api-username>'  
password  = '<api-password'  
domain    = '<domain>'
subdomains = ['subdomain1','subdomain2']

s4 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s4.connect(('ipv4.google.com', 80))
IP4 = s4.getsockname()[0]

s6 = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
s6.connect(('ipv6.google.com', 80))
IP6 = s6.getsockname()[0]

global_domain_server_url = 'https://api.loopia.se/RPCSERV'   
client = xmlrpclib.ServerProxy(uri = global_domain_server_url, encoding = 'utf-8')  

for subdomain in subdomains:
	myrecords = client.getZoneRecords(username, password, domain, subdomain)
	for myrecord in myrecords:
		if myrecord['type'] == 'AAAA' and myrecord['rdata'] != IP6:
			myrecord['rdata'] = IP6
			client.updateZoneRecord(username, password, domain, subdomain, myrecord)
			print subdomain + "." + domain, "=", myrecord
		elif myrecord['type'] == 'A' and myrecord['rdata'] != IP4:
			myrecord['rdata'] = IP4
			client.updateZoneRecord(username, password, domain, subdomain, myrecord)
			print subdomain + "." + domain, "=", myrecord
