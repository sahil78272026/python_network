"""
IP address validation script: This script can be used to validate whether an IP address is in a correct format or not. 
It can be useful in situations where you need to check if the IP address entered is a valid IP address. 
Here's an example script:
"""

import socket

def is_valid_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        return False

ip = "192.168.1.1"
if is_valid_ip(ip):
    print(ip + " is a valid IP address.")
else:
    print(ip + " is not a valid IP address.")
