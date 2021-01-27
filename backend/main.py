import nmap
from connect import connect
from insert import insert


print("hello world")

connect()   #check connection

insert("192.168.0.1", "WIN 7", "Jogurt", 1)

# initialize the port scanner
# nmScan = nmap.PortScanner()

# scan localhost for ports in range 21-443
# nmScan.scan('127.0.0.1')
# scanRange = nmScan.scan(hosts="192.168.0.0/24")
# print(scanRange)

# print(nmScan.all_hosts())

# # run a loop to print all the found result about the ports
# for host in nmScan.all_hosts():
#      print('Host : %s (%s)' % (host, nmScan[host].hostname()))
#      print('State : %s' % nmScan[host].state())
#      for proto in nmScan[host].all_protocols():
#         print('----------')
#         print('Protocol : %s' % proto)
 
#         lport = nmScan[host][proto].keys()


