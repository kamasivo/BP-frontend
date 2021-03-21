import nmap
from database.connect import connect
from database.insert import insert
from database.insert import insertPort
from database.delete import delete


def pingScan():

    nmScan = nmap.PortScanner()    # initialize the port scanner

    nmScan.scan(hosts="192.168.1.0/24", arguments="-sn")
    # nmScan.scan('127.0.0.1', arguments='-n sP')

    allIpAddresses = []
    for host in nmScan.all_hosts():
        # print(host)
        allIpAddresses.append(host)
        # print(allIpAddresses)

    return allIpAddresses
       

# pingScan()