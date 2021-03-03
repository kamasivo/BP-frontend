from spoofer import *
from sniffer import sniffer

def main(): 
    # targets = "192.168.1.10, 192.168.1.12"
    targets = ("192.168.1.10")
    # spoofer(targets)
    spooferThread = threading.Thread(target=spoofer, name="spoofer_function", args=(targets,))
    spooferThread.start()


    # // todo key ctrl c handler
    # sniffer()


main()