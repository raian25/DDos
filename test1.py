from scapy.all import *

# Define the target host and port
target_host = "10.123.152.1"
target_port = 80

# Define the maximum byte size of the packet
max_byte_size = 50000

# Define the number of packets to send
num_packets = 10

# Define the types of packets to send
packet_types = ["ICMP", "TCP", "UDP"]

# Create a function to send packets
def send_packet(packet_type):
    # Create the packet
    if packet_type == "ICMP":
        packet = IP(dst=target_host)/ICMP()/(b'\x00' * max_byte_size)
    elif packet_type == "TCP":
        packet = IP(dst=target_host)/TCP(dport=target_port)/(b'\x00' * max_byte_size)
    elif packet_type == "UDP":
        packet = IP(dst=target_host)/UDP(dport=target_port)/(b'\x00' * max_byte_size)
    else:
        raise ValueError("Invalid packet type")

    # Send the packets
    for i in range(num_packets):
        try:
            response = sr1(packet, timeout=1)
            if response:
                print(f"{packet_type} packet {i+1} received from {response.src}")
            else:
                print(f"{packet_type} packet {i+1} failed to receive")
        except:
            print(f"{packet_type} packet {i+1} failed to send")

# Send the packets
for packet_type in packet_types:
    send_packet(packet_type)
