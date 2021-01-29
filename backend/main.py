import nmap
from connect import connect
from insert import insert

# connect()   #check connection

# insert("192.168.1.0", "WIN 7", "Jogurt", 1)   # funckne ulozenie do db...uz len ziskat data ktore ukladat

# initialize the port scanner
nmScan = nmap.PortScanner()

scanRange = nmScan.scan(hosts="192.168.1.0/24", arguments="-O")
# nmScan.scan('127.0.0.1', arguments='-O')


for host in nmScan.all_hosts():
    print('IP address: %s' % host)
    print('info: %s' % nmScan[host]['osmatch'][0])
    if(nmScan[host]['osmatch'][0]):
        print('OS: %s' % nmScan[host]['osmatch'][0]['name'])
        print('vendor: %s' % nmScan[host]['osmatch'][0]['osclass'][0]['vendor'])
        print('os family: %s' % nmScan[host]['osmatch'][0]['osclass'][0]['osfamily'])
        print('osgen: %s' % nmScan[host]['osmatch'][0]['osclass'][0]['osgen'])
    else:
        print('OS unknown')
    print('NAME: %s' % nmScan[host].hostname())
    # print('-------------------------------')
    # print('%s' % nmScan[host])
    # print('-----------------------------')

    #protocols todo
    # for proto in nmScan[host].all_protocols():
    #     print('----------')
    #     print('Protocol : %s' % proto)
 
    #     lport = nmScan[host][proto].keys()
    #     for port in lport:
    #         print('port : %s  ' % port)
    #         print('state : %s' % nmScan[host][proto][port]['state'])


