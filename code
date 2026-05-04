from scapy.all import sniff, IP, TCP, UDP, ICMP

# Function to process each packet
def process_packet(packet):
    print("\n--- New Packet Captured ---")

    # Check if packet has IP layer
    if packet.haslayer(IP):
        ip_layer = packet[IP]

        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        print(f"Packet Size: {len(packet)} bytes")

        # Check protocol
        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")
        elif packet.haslayer(ICMP):
            print("Protocol: ICMP")
        else:
            print("Protocol: Other")

        # Optional: show raw payload (safe preview)
        if packet.payload:
            payload = bytes(packet.payload)
            print(f"Payload (first 50 bytes): {payload[:50]}")


# Start sniffing
def start_sniffer():
    print("Starting network sniffer... Press Ctrl+C to stop.")
    
    sniff(
        prn=process_packet,  # function to call
        store=False          # don’t store packets in memory
    )


if __name__ == "__main__":
    start_sniffer()
