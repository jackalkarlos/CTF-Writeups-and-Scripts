from scapy.all import *

pcap = rdpcap("EzPz.pcap")

for pkt in pcap:
    if Raw in pkt:
        print pkt[Raw]
