"""
SNMP monitoring script: This script can be used to monitor network devices using SNMP (Simple Network Management Protocol). 
It can be used to retrieve information such as CPU utilization, memory usage, and interface statistics. 
Here's an example script using the PySNMP library:
"""

from pysnmp.hlapi import *

ip = '192.168.1.1'
community = 'public'

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in bulkCmd(SnmpEngine(),
                          CommunityData(community),
                          UdpTransportTarget((ip, 161)),
                          ContextData(),
                          0, 25,
                          ObjectType(ObjectIdentity('IF-MIB', 'ifInOctets'))):

    if errorIndication:
        print(errorIndication)
        break

    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
        break

    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))
