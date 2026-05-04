from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys

def process_packet(packet):
    print("\n--- New Packet Captured ---")
    if packet.haslayer(IP):
        ip = packet[IP]
        print(f"Source IP      : {ip.src}")
        print(f"Destination IP : {ip.dst}")
        print(f"Packet Size    : {len(packet)} bytes")

        if packet.haslayer(TCP):   print("Protocol: TCP")
        elif packet.haslayer(UDP): print("Protocol: UDP")
        elif packet.haslayer(ICMP):print("Protocol: ICMP")
        else:                      print("Protocol: Other")

        if packet.payload:
            raw = bytes(packet.payload)[:50]
            try:    print(f"Payload: {raw.decode('utf-8', errors='replace')}")
            except: print(f"Payload (raw): {raw}")

def start_sniffer(iface=None, count=0):
    print("Starting sniffer... Press Ctrl+C to stop.")
    try:
        sniff(iface=iface, prn=process_packet, store=False, count=count)
    except PermissionError:
        print("Error: Run as administrator/root.")
        sys.exit(1)

if __name__ == "__main__":
    start_sniffer()
