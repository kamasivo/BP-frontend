import nmap
from database.connect import connect
from database.insert import insert
from database.insert import insertPort
from database.delete import delete


def scan():
    print("Start nmap scan to find devices and ports.")
    connect()   #check connection

    delete('devices')         # delete the database before scan
    delete('ports')  

    nmScan = nmap.PortScanner()    # initialize the port scanner

    scanRange = nmScan.scan(hosts="192.168.1.0/24", arguments="-O")
    # nmScan.scan('127.0.0.1', arguments='-O')


    for host in nmScan.all_hosts():
        ipAddress = host
        # print(nmScan[host])
        # print("====================")
        if(nmScan[host]['vendor']):
            vendor = nmScan[host]['vendor']
            values_view = vendor.values()
            value_iterator = iter(values_view)
            vendor = next(value_iterator)
        else:
            vendor = "unknown"
        if(nmScan[host]['osmatch']):
            os = nmScan[host]['osmatch'][0]['name']
            osFamily = nmScan[host]['osmatch'][0]['osclass'][0]['osfamily']
            osGen = nmScan[host]['osmatch'][0]['osclass'][0]['osgen']
        else:
            os = 'unknown'
            osFamily = 'unknown'
            osGen = 'unknown'
        name = nmScan[host].hostname()

        openPorts = 0
        for proto in nmScan[host].all_protocols():
            lport = nmScan[host][proto].keys()
            for port in lport:
                if(nmScan[host][proto][port]['state'] == 'open'):
                    openPorts += 1
                    insertPort(port, ipAddress)

        numOfVulns = 0
        insert(ipAddress, os, name, vendor, osFamily, osGen ,numOfVulns, openPorts)  
