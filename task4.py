#import json
from pysnmp.hlapi import *

errorIndication, errorStatus, errorIndex, varBinds = next(

    getCmd(SnmpEngine(),

           CommunityData('public', mpModel=0),

           UdpTransportTarget(('104.236.166.95', 161)),

           ContextData(),

           ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)),
           ObjectType(ObjectIdentity('1.3.6.1.4.1.2021.4.6.0')),
           ObjectType(ObjectIdentity('1.3.6.1.4.1.2021.4.11.0')))

)
 

if errorIndication:

    print(errorIndication)

elif errorStatus:

    print('%s at %s' % (errorStatus.prettyPrint(),

                        errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))

else:

    for varBind in varBinds:

        print(' = '.join([x.prettyPrint() for x in varBind]))

#with open('data.txt', 'w') as outfile:  
#    json.dump(varBind, outfile)
