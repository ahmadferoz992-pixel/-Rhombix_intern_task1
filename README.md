# -Rhombix_intern_task1
This is a simple network sniffer built in Python using Scapy. The project captures and analyzes live network traffic, making it useful for beginners who want to understand how data moves across a network and how packets are structured.

Features:
Captures live network packets
Displays important details such as:
Source IP address
Destination IP address
Protocol (TCP, UDP, ICMP)
Packet size
Provides a basic preview of packet payload data
Written in a simple and easy-to-understand way
Learning Objectives

This project is designed to help you understand:

How network communication works
The structure of network packets (headers and payload)
Differences between common protocols like TCP, UDP, and ICMP
The basic idea behind packet analysis tools

Requirements:
Python 3.x
Scapy
Npcap (required for Windows)
How to Run
Install the required library:
pip install scapy
Run the script with administrator privileges:
python sniffer.py
Generate some network activity (for example, open a website or use ping) to see captured packets.

Disclaimer:

This project is for educational purposes only. It should only be used on networks that you own or have explicit permission to monitor.
