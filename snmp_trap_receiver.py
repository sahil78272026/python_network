"""
SNMP trap receiver script: This script can be used to receive and parse SNMP traps sent by network devices. 
It can be helpful in monitoring and troubleshooting network issues. Here's an example script using the PySNMP library

SNMP (Simple Network Management Protocol) is a widely used protocol for monitoring and managing network devices. It allows network administrators to monitor the performance, availability, and utilization of network devices. SNMP traps are messages sent by network devices to alert the SNMP manager about events such as device failures, high CPU usage, interface errors, and other issues.

A trap receiver is a software application that listens for and receives SNMP traps sent by network devices. When an SNMP trap is received, the trap receiver can process and display the information contained in the trap, such as the type of event, the device that generated the trap, and other details.

The SNMP trap receiver script is a Python script that can be used to receive and process SNMP traps sent by network devices. The PySNMP library is used in this script to create a trap receiver that listens on a specified port for incoming SNMP traps.

The script uses the AsyncoreDispatcher class to create an event loop that listens for incoming SNMP traps. When a trap is received, the cbFun callback function is called to process the trap. The cbFun function decodes the trap message and extracts information such as the device that generated the trap, the type of event, and any other details included in the trap message.

The trap receiver script can be useful in monitoring and troubleshooting network issues. When a network device generates an SNMP trap, the script can be used to quickly identify the cause of the event and take appropriate action to resolve the issue. By processing SNMP traps in real-time, network administrators can respond to network events quickly and proactively.

In an interview, discussing this script can showcase your understanding of SNMP and its use in network management, as well as your proficiency in Python programming and libraries such as PySNMP. Additionally, it can demonstrate your ability to troubleshoot and resolve network issues using automation and scripting.
"""


from pysnmp.entity import engine, config
from pysnmp.carrier.asyncore.dispatch import AsyncoreDispatcher
from pysnmp.carrier.asyncore.dgram import udp, udp6
from pysnmp.proto import api

def cbFun(transportDispatcher, transportDomain, transportAddress, wholeMsg):
    while wholeMsg:
        msgVer = int(api.decodeMessageVersion(wholeMsg))
        if msgVer in api.protoModules:
            pMod = api.protoModules[msgVer]
        else:
            print('Unsupported SNMP version %s' % msgVer)
            return
        reqMsg, wholeMsg = decoder.decode(
            wholeMsg, asn1Spec=pMod.Message(),
        )
        print('Notification message from %s:%s: ' % (
            transportAddress[0], transportAddress[1]
        ))
        reqPDU = pMod.apiMessage.getPDU(reqMsg)
        if reqPDU.isSameTypeWith(pMod.TrapPDU()):
            if msgVer == api.protoVersion1:
                print('Enterprise: %s' % (
                    pMod.apiTrapPDU.getEnterprise(reqPDU).prettyPrint()
                ))
                print('Agent Address: %s' % (
                    pMod.apiTrapPDU.getAgentAddr(reqPDU).prettyPrint()
                ))
                print('Generic Trap: %s' % (
                    pMod.apiTrapPDU.getGenericTrap(reqPDU).prettyPrint()
                ))
                print('Specific Trap: %s' % (
                    pMod.apiTrapPDU.getSpecificTrap(reqPDU).prettyPrint()
                ))
                print('Uptime: %s' % (
                    pMod.apiTrapPDU.getTimeStamp(reqPDU).prettyPrint()
                ))
                varBinds = pMod.apiTrapPDU.getVarBindList(reqPDU)
            else:
                varBinds = pMod.apiPDU.getVarBindList(reqPDU)
            print('Var-binds:')
            for oid, val in varBinds:
                print('%s = %s' % (oid.prettyPrint(), val.prettyPrint()))

transportDispatcher = AsyncoreDispatcher()

transportDispatcher.registerRecvCbFun(cbFun)

config.addTransport(
    transportDispatcher, udp.domainName, udp.UdpSocketTransport().openServerMode(('0.0.0.0', 162))
)

transportDispatcher.jobStarted(1)

try:
    # Dispatcher will never finish as job#1 never reaches zero
    transportDispatcher.runDispatcher()
except Exception:
    transportDispatcher.closeDispatcher()
    raise
