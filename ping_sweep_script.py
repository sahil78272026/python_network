"""
Ping sweep script: This script can be used to ping multiple devices on a network to determine which ones are up and which ones are down. 
It can be helpful in identifying network connectivity issues. Here's an example script:
"""

import subprocess

for i in range(1, 255):
    ip = "192.168.1." + str(i)
    result = subprocess.call(['ping', '-c', '1', '-w', '1', ip])
    if result == 0:
        print(ip + " is up!")
    else:
        print(ip + " is down.")