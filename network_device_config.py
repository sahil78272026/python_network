"""
Network device configuration script: This script can be used to configure network devices such as routers and switches. 
It can automate repetitive tasks such as updating access control lists or configuring VLANs. 
Here's an example script using the Netmiko library:
"""

from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.1.1',
    'username': 'admin',
    'password': 'password',
}

with ConnectHandler(**device) as net_connect:
    commands = [
        'interface fa0/1',
        'description Test Interface',
        'ip address 192.168.1.10 255.255.255.0',
    ]
    output = net_connect.send_config_set(commands)
    print(output)
