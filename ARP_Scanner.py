#Imports Scapy
import scapy.all as scapy

# provides more string manipulation options to be used when formatting Ipv4 address
import re

print(r"""
           _____  _____     _____                                 
     /\   |  __ \|  __ \   / ____|                                
    /  \  | |__) | |__) | | (___   ___ __ _ _ __  _ __   ___ _ __ 
   / /\ \ |  _  /|  ___/   \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  / ____ \| | \ \| |       ____) | (_| (_| | | | | | | |  __/ |   
 /_/    \_\_|  \_\_|      |_____/ \___\__,_|_| |_|_| |_|\___|_|   
                                                                  
                                                                  
                                         
""")
print("\n**************************************\n")

# use re to ensure an ipv4 address is being used
ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    # Get the address range from the user
    ip_add_range_entered = input(
        "\nPlease enter the ip adress and range you want to send the ARP request to (e.g. 192.168.1.0/24)\n")
    # If what the user entered fufills the 're' requirements then print it is valid and break
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} IS a valid ip range")
        break

arp_result = scapy.arping(ip_add_range_entered)
