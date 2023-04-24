"""
VLAN information script: This script can be used to retrieve information about VLANs configured on a switch or router. 
It can be useful for troubleshooting VLAN-related issues. Here's an example script using the Netmiko library:
"""

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

with ConnectHandler(**device) as net_connect:
    output = net_connect.send_command('show vlan')
    print(output)
