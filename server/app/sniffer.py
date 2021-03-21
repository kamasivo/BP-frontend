#!/usr/bin/python

from scapy.all import *
import socket
import datetime
import os
from geoip import geolite2
import json
import pandas as panda

tcpPackets = 0
udpPackets = 0
icmpPackets = 0

ipAdresses = []

def network_monitoring_for_visualization_version(pkt):
    if(pkt.haslayer(IP)):
        inList = True
        for ip in ipAdresses:
            if(ip == pkt[IP].dst):
                inList = False
                continue
        if(inList):
            ipAdresses.append(pkt[IP].dst)
            print(pkt[IP].dst)
            panda.DataFrame(ipAdresses).to_json("ipAdresses.json")

    if (pkt.haslayer(TCP)):
        with open('packets.json', 'r+') as f:
            data = json.load(f)
            global tcpPackets 
            tcpPackets += 1
            data['tcp'] = tcpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     
    if (pkt.haslayer(UDP)):
        with open('packets.json', 'r+') as f:
            data = json.load(f)
            global udpPackets 
            udpPackets += 1
            data['udp'] = tcpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     
    if (pkt.haslayer(ICMP)):
        with open('packets.json', 'r+') as f:
            data = json.load(f)
            global icmpPackets 
            icmpPackets += 1
            data['icmp'] = icmpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     

def sniffer():
    print("sniffer connected")
    sniff(prn=network_monitoring_for_visualization_version)