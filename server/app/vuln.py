import nmap
import pandas as panda

def find_vulnerabilities():
    # pomocka
    # nasledujuci sken je rovanky: takto ich potrebujem prepisovat
    # nmap -vv --script ssl-cert,ssl-enum-ciphers -p 443,465,993,995,3389
    # nmScan.scan('127.0.0.1', '443,465,993,995,3389', arguments='--script ssl-cert,ssl-enum-ciphers')

    print("Start nmap script scan to find vulnerabilities.")

    nmScan = nmap.PortScanner()  

    # odskusane scripty v konzole na implementaciu
    # nmap -sV --script vuln 192.168.1.1
    # nmap -sV --script vulners 192.168.1.1
    # nmap -sV --script vulscan/scipag_vulscan/vulscan.nse 192.168.1.1

    nmScan.scan('192.168.1.1', arguments='-sV -script vulscan/scipag_vulscan/vulscan.nse, ')
    print(nmScan.command_line())
    for host in nmScan.all_hosts():
        vuln_list = [[]]
        print(host) # ip adddress
        for port in nmScan[host]['tcp']:
            print(port)
            print(nmScan[host]['tcp'][port]["state"])
            print(nmScan[host]['tcp'][port]["name"])
            if('script' in nmScan[host]['tcp'][port]):
                if('fingerprint-strings' in nmScan[host]['tcp'][port]["script"]):
                    print(nmScan[host]['tcp'][port]["script"]['fingerprint-strings']) 
                    vuln_list.append([host, port, nmScan[host]['tcp'][port]["state"], nmScan[host]['tcp'][port]["name"], nmScan[host]['tcp'][port]["script"]['fingerprint-strings']])   
                if('vulscan' in nmScan[host]['tcp'][port]["script"]):
                    print(nmScan[host]['tcp'][port]["script"]['vulscan'])
                    vuln_list.append([host, port, nmScan[host]['tcp'][port]["state"], nmScan[host]['tcp'][port]["name"], nmScan[host]['tcp'][port]["script"]['vulscan']])   
    print(vuln_list)
    panda.DataFrame(vuln_list, columns=['ipAddress', 'port', 'state', 'name', 'script']).to_json("networkdata/vulns.json", orient="table")


    # vulns hlada super, skusa brutalne vela veci ale dlho to trvaaj 10 minut 

    # nmScan.scan('192.168.1.1/24', arguments='-sV script vulners')
    # print(nmScan.command_line())
    # # print(nmScan.all_host())
    # for host in nmScan.all_hosts():
    #     print(nmScan[host])

    # nmScan.scan('192.168.1.1/24', arguments='-sV -script vuln')
    # print(nmScan.command_line())
    # for host in nmScan.all_hosts():
    #     print(nmScan[host])

find_vulnerabilities()