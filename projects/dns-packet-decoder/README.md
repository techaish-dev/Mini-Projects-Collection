# DNS Packet Base64 Decoder

A Python script that decodes base64-encoded commands from DNS packets in a PCAP file using Scapy. It extracts, decodes, and filters the data for network traffic analysis and cybersecurity research.

## Features

- Read and process network packets from a PCAP file.
- Identify and extract base64-encoded data from DNS responses.
- Decode base64 data to human-readable format.
- Filter and display decoded commands, excluding specified patterns.

## Requirements

- Python 3.x
- Scapy
- base64

## Installation

Install the required package using pip:
```bash
pip install scapy
```
## Usage

Ensure you have Scapy and base64 modules installed.  
Place the `gnome.pcap` file in the same directory as the script.  
Run the script `decode.py` to decode and print the commands.
```bash
python decode.py
```
