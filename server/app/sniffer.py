from scapy.all import *
import socket
import datetime
import os
from geoip import geolite2
import json
import pandas as panda
from spam_lists import SPAMHAUS_DBL as checker

tcpPackets = 0
udpPackets = 0
icmpPackets = 0

ipAdresses = [[]]
localNetwork = '192.168.'
frame = ''

#return true if already in list
def is_in_ipadresses(ipAddressFrom, ipAddressTo):
    global ipAdresses
    for ip in ipAdresses:
        if(ip and ip[0] == ipAddressFrom and ip[1] == ipAddressTo):
            # ip[1] = ipAddressTo
            ip[2] += 1
            return True
        if(ip and ip[0] == ipAddressTo and ip[1] == ipAddressFrom):
            # ip[1] = ipAddressFrom
            ip[3] += 1
            return True
    return False

# myslienka...mam localnu..k nej pride niaka cuzdia..zaznacim si a pocet prijatych a odoslanych k tej cudzej
def network_sniffer(pkt):
    if(pkt.haslayer(IP)):
        global ipAdresses, localNetwork
        inList = is_in_ipadresses(pkt[IP].src, pkt[IP].dst)

        if(not inList):
            if(pkt[IP].src.startswith(localNetwork)):
                onBlacklist = False
                if(pkt[IP].dst in checker):
                    print('IP found on blacklist')
                    onBlacklist = True
                ipAdresses.append([pkt[IP].src, pkt[IP].dst, 1, 0, onBlacklist])
            elif(pkt[IP].dst.startswith(localNetwork)):
                onBlacklist = False
                if(pkt[IP].dst in checker):
                    print('IP found on blacklist')
                    onBlacklist = True
                ipAdresses.append([pkt[IP].dst, pkt[IP].src, 0, 1, onBlacklist])
                panda.DataFrame(ipAdresses, columns=['ipAddressLocal', 'ipAddressForeign', 'sendPackets', 'receivedPackets', 'blackList']).to_json("networkdata/ipAdresses.json", orient="table")
    if (pkt.haslayer(TCP)):
        with open('networkdata/packets.json', 'r+') as f:
            data = json.load(f)
            global tcpPackets 
            tcpPackets += 1
            data['tcp'] = tcpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     
    if (pkt.haslayer(UDP)):
        with open('networkdata/packets.json', 'r+') as f:
            data = json.load(f)
            global udpPackets 
            udpPackets += 1
            data['udp'] = tcpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     
    if (pkt.haslayer(ICMP)):
        with open('networkdata/packets.json', 'r+') as f:
            data = json.load(f)
            global icmpPackets 
            icmpPackets += 1
            data['icmp'] = icmpPackets 
            f.seek(0)       
            json.dump(data, f, indent=4)
            f.truncate()     

def sniffer():
    print("Network packet counter started.")
    sniff(prn=network_sniffer)