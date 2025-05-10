import argparse
# Python3 sniffer1.py -v -i wlan0
from scapy.all import sniff

class Sniffer:
    def __init__(self, args):  # Corrected __init__ method
        self.args = args

    def __call__(self, packet):  # Corrected __call__ method
        if self.args.verbose:
            packet.show()
        else:
            print(packet.summary())

    def run_forever(self):
        sniff(iface=self.args.interface, prn=self, store=0)

# Main block should be outside the class and correctly indented
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", default=False, action="store_true", help="be more talkative")
    parser.add_argument("-i", "--interface", type=str, required=True, help="network interface name")
    args = parser.parse_args()

    sniffer = Sniffer(args)
    sniffer.run_forever()

