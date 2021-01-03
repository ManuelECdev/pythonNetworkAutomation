from ipaddress import *
import ipaddress

#supportedInputKeys = ['vrfName','idNumber','vrfName','hostslist','ipNetwork','ospfArea','hsrpGroup','vlanId','ospfProcess','ipNetworkXfer','ipNetworkLoopBack','interfaceLoopbackNumber','ospfPassword']

firstsHosts = {'fpDs-1'}

firstsHosts_fp = {
    "hsrpPriority": 104,
    "ipOffsetXfer": 2,
    "ipOffsetLoopback": 1,
    "ipOffsetServer": 2,
    "deviceOrder": 1
}

secondsHosts = {'fpDs-2'}

secondsHosts_fp = {
    "hsrpPriority": 103,
    "ipOffsetXfer": 3,
    "ipOffsetLoopback": 2,
    "ipOffsetServer": 3,
    "deviceOrder": 2
}

thirdsHosts = {'fpDs-3'}

thirdsHosts_fp = {
    "hsrpPriority": 102,
    "ipOffsetXfer": 4,
    "ipOffsetLoopback": 3,
    "ipOffsetServer": 4,
    "deviceOrder": 3    
}

fourthsHosts = {'fpDs-4'}

fourthsHosts_fp = {
    "hsrpPriority": 101,
    "ipOffsetXfer": 5,
    "ipOffsetLoopback": 4,
    "ipOffsetServer": 5,
    "deviceOrder": 4    
}

#Arquitecture solution group vars

def buildOspfPassword(vlanId, vrfName):
    mySeparator = ""
    join = mySeparator.join([str(vlanId),vrfName])
    return join[0:8]
    
def buildRouterId(subnet,ipOffsetLoopback):
    
    ipAddress = str( ipaddress.ip_network(subnet).network_address  + ipOffsetLoopback )

    return ipAddress    

def buildHsrpAuth(authInput):
    return authInput
    
def buildHsrpVip(subnet,hsrpVipOffset):
    
    ipAddress = str( ipaddress.ip_network(subnet).network_address + hsrpVipOffset )
    
    return ipAddress
    
fp = {
    "hsrpVipOffset": 1,
    "interfaceVlanName": 'Vlan',
    "intefaceLoopbackName": 'Loopback',
    "LoopbackPrefix": "32",
    "interfaceDescriptionXferFw": 'xfer_Fw',
    "interfaceDescriptionLoopback": 'Loopback',
    "interfaceDescriptionServer": 'serverNetwork',
    "ospfPasswordFunction": buildOspfPassword,
    "routerIdFunction": buildRouterId,
    "hsrpAuthFunction": buildHsrpAuth,
    "HsrpVipFunction": buildHsrpVip,
}

hostName2GroupVar = {
    "fpDs-1": { "hostOrder": firstsHosts_fp, "design": fp },
    "fpDs-2": { "hostOrder": secondsHosts_fp, "design": fp },
    "fpDs-3": { "hostOrder": thirdsHosts_fp, "design": fp },
    "fpDs-4": { "hostOrder": fourthsHosts_fp, "design": fp } 
}