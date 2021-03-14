# ak by som chcel spravit aj ARP stop poisoning a aby sa ARP vratilo tak ako ma je potrebne prerobit cely utok
# treba to spravit tak aby to bola trieda vo vlastnom vlakne...tiez zabezpecit moznost volania metod v tom istom vlakne,
# teraz neviem sa dostat do tej metody

from spoofer import *
from sniffer import sniffer

def main(): 
    targets = ("192.168.1.12")
    spooferThread = threading.Thread(target=spoofer, name="spoofer_function", args=(targets,))
    spooferThread.start()

    snifferThread = threading.Thread(target=sniffer, name="sniffer_function", args=())
    snifferThread.start()


    # try:
    #     while spooferThread.is_alive():
    #         time.sleep(2) 
    # except KeyboardInterrupt:
    #     print("ctrl c detected")
    #     restore_ARP_caches()
        # restore_ARP_caches(targets)
    # try:
        # while spooferThread.is_alive():
            # time.sleep(2) 

    # except KeyboardInterrupt:
        # Ctrl+C detected, so let's finish the poison thread and exit
        # print("ctrl c detected")
        # exitSpoofer()
        # control_queue.put(('quit',))
        # poison_thread.join()

    # // todo key ctrl c handler
    # sniffer()


main()