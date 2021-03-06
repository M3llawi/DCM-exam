from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public', mpModel=0),
                          UdpTransportTarget(('demo.snmplabs.com', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifDescr')),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifMtu')),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifSpeed')),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifPhysAddress')),
                          ObjectType(ObjectIdentity('IF-MIB', 'ifType')),
                          lexicographicMode=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))