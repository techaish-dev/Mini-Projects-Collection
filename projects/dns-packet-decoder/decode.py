from scapy.all import  *
import base64
import codecs

network_packets = rdpcap('gnome.pcap')
decoded_commands = []
decoded_data =""
for packet in network_packets:
	if DNSQR in packet:
		if packet[DNS].id == 0x1337:
			b64_string=str(packet[DNS].an.rdata)
			b64_string=b64_string.strip('[')
			b64_string=b64_string.strip('b')
			b64_string=b64_string.strip("'")
			b64_string=b64_string.strip("]")
			decoded_data = base64.b64decode(b64_string)
	if 'FILE:' in str(decoded_data):
			continue
	else:
		decoded_commands.append(decoded_data)
for command in decoded_commands:
	if len(command)>1:
		print (command.rstrip())