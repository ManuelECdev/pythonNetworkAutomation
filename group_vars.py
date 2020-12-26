#HostOrder group vars

from ipaddress import *

firstsHosts_fp = {
    "hsrpPriority": 104,
    "ipOffsetXfer": 2,
    "ipOffsetLoopback": 1,
    "ipOffsetServer": 2,
    "deviceOrder": 1
}

secondsHosts_fp = {
    "hsrpPriority": 103,
    "ipOffsetXfer": 3,
    "ipOffsetLoopback": 2,
    "ipOffsetServer": 3,
    "deviceOrder": 2
}

thirdsHosts_fp = {
    "hsrpPriority": 102,
    "ipOffsetXfer": 4,
    "ipOffsetLoopback": 3,
    "ipOffsetServer": 4,
    "deviceOrder": 3    
}

fourthsHosts_fp = {
    "hsrpPriority": 101,
    "ipOffsetXfer": 5,
    "ipOffsetLoopback": 4,
    "ipOffsetServer": 5,
    "deviceOrder": 4    
}

#Arquitecture solution group vars
fp = {
    "hsrpVipOffset": 1,
    "interfaceVlanName": 'Vlan',
    "intefaceLoopbackName": 'Loopback',
    "interfaceDescriptionXferFw": 'xfer_Fw',
    "interfaceDescriptionLoopback": 'lLoopback',
    "interfaceDescriptionServer": 'serverNetwork',
    "ospfPasswordFunction": buildOspfPassword,
    "routerIdFunction": buildRouterId,
    "hsrpAuthFunction": buildHsrpAuth,
    "HsrpVipFunction": buildHsrpVip,
}

def buildOspfPassword(vlanId, vrfName):
    mySeparator = ""
    join = mySeparator.join([str(vlanId),vrfName])
    return join[0:8]
    
def buildRouterId(subnet,ipOffsetLoopback,deviceOrder):
    
    ipAddress = str( ipaddress.ip_network(subnet).network_address + deviceOrder + ipOffsetLoopback )

    return ipAddress    

def buildHsrpAuth(vlanId):
    return vlanId
    
def buildHsrpVip(subnet,hsrpVipOffset):
    
    ipAddress = str( ipaddress.ip_network(subnet).network_address + hsrpVipOffset )
    
    return ipAddress
    
    
hostName2GroupVar = {
    "fpDs-1": { "hostOrder": firstsHosts_fp, "design": fp },
    "fpDs-2": { "hostOrder": secondsHosts_fp, "design": fp },
    "fpDs-3": { "hostOrder": thirdsHosts_fp, "design": fp },
    "fpDs-4": { "hostOrder": fourthsHosts_fp, "design": fp } 
}