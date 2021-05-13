import nmap
import pandas as panda

def find_vulnerabilities():
    # nasledujuci sken je rovanky: takto ich potrebujem prepisovat
    # nmap -vv --script ssl-cert,ssl-enum-ciphers -p 443,465,993,995,3389
    # nmScan.scan('127.0.0.1', '443,465,993,995,3389', arguments='--script ssl-cert,ssl-enum-ciphers')

    print("Start nmap script scan to find vulnerabilities.")

    nmScan = nmap.PortScanner()  
    nmScan.scan('192.168.1.220', arguments='-sV -script vulners')
    # nmScan.scan('192.168.1.1/24', arguments='-sV -script vulners')
    # print(nmScan.command_line())
    vuln_list = [[]]
    for host in nmScan.all_hosts():
        # print(host) # ip adddress
        # print(nmScan[host])
        if('tcp' in nmScan[host]):
            for port in nmScan[host]['tcp']:
                # print(port)
                # print(nmScan[host]['tcp'][port]["state"])
                # print(nmScan[host]['tcp'][port]["name"])
                if('script' in nmScan[host]['tcp'][port]):
                    if('vulners' in nmScan[host]['tcp'][port]["script"]):
                        vuln_list.append([host, port, nmScan[host]['tcp'][port]["state"], nmScan[host]['tcp'][port]["name"], nmScan[host]['tcp'][port]["product"], nmScan[host]['tcp'][port]["script"]['vulners']])   
                else:
                    vuln_list.append([host, port, nmScan[host]['tcp'][port]["state"], nmScan[host]['tcp'][port]["name"], nmScan[host]['tcp'][port]["product"], ""]) 
        vuln_list.append([host, "", "", "", "", ""]) 
    panda.DataFrame(vuln_list, columns=['ipAddress', 'port', 'state', 'name', 'product', 'script']).to_json("networkdata/vulns.json", orient="table")


    # vulns hlada super, skusa brutalne vela veci ale dlho to trvaaj 10 minut 
    # nmScan.scan('192.168.1.1/24', arguments='-sV -script vuln')
    # print(nmScan.command_line())
    # for host in nmScan.all_hosts():
    #     print(nmScan[host])

