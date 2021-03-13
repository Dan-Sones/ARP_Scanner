import scapy.all as scapy

#provides more string manipulation options
import re

print(r"""
   _____                                 
  / ____|                                
 | (___   ___ __ _ _ __  _ __   ___ _ __ 
  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  ____) | (_| (_| | | | | | | |  __/ |   
 |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                         
""")
print("\n**************************************\n")


#use re to ensure an ipv4 address is being used
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

#Get the address range from the user

while True:
    ip_add_range_entered = input("\nPlease enter the ip adress and range you want to send the ARP request to (e.g. 192.168.1.0/24)\n")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} IS a valid ip range")
        break

    arp_result = scapy.arping(ip_add_range_entered)