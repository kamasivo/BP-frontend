import nmap


def vuln_scan():

    nmScan = nmap.PortScanner()    # initialize the port scanner

    #nasledujuci sken je rovanky: takto ich potrebujem prepisovat
    # nmap -vv --script ssl-cert,ssl-enum-ciphers -p 443,465,993,995,3389
    # nmScan.scan('127.0.0.1', '443,465,993,995,3389', arguments='--script ssl-cert,ssl-enum-ciphers')
    print(nmScan.command_line())
    for host in nmScan.all_hosts():
        print(nmScan[host])

vuln_scan()