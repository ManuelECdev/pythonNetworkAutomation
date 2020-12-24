from helper import *


def buildIpAddress(subnet,deviceNameOrder,ipOffset ):
    return str( ipaddress.ip_network(subnet).network_address + deviceNameOrder + ipOffset )
    
def buildPrefixlen(subnet):
    return str( ipaddress.ip_network(subnet).prefixlen )

class newVrf:

    def __init__(self, vrfName):
        
        self.vrfName = vrfName

def task_buildConfig_newVrf_fp(playbook,role, hostName,inputPlaybook):
     
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": None
    }
    
    #setting up variables from inputPlaybook
    vrfName = inputPlaybook['vrfName']
    
    newVrfObject = newVrf(vrfName)
    
    rendered_buildConfig['renderedSnippet']  = gen_snippet('snippet7', newVrfObject.__dict__)
    
    return rendered_buildConfig
    
class newInterfaceVlanXferFw:

    #dswX4
    def __init__(self, interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefixlen, ospfPassword, ospfProcess, ospfArea):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.interfaceDescription = interfaceDescription
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefixlen = ipPrefixlen
        self.ospfPassword = ospfPassword
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea


    
def task_buildConfig_newInterfaceVlanXferFw_fp(playbook,role, hostName,inputPlaybook, groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars['hostOrder']
    designGroupVar = groupVars['design']
    
    #setting up variables from inputPlaybook
    vlanId = inputPlaybook['vlanId']
    interfaceNumber = inputPlaybook['vlanId']
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    subnet = inputPlaybook['ipNetworkXfer']
   
    #setup variables from group vars
    interfaceName = designGroupVar['interfaceVlanName']
    interfaceDescription = designGroupVar['interfaceDescriptionXferFw']
    deviceOrder= hostOrderGroupVar['deviceOrder']
    ipOffsetXfer = hostOrderGroupVar['ipOffsetXfer']
    
    #build variables from groupVars, inputVars
    ospfPassword = designGroupVar['ospfPasswordFunction'](vlanId, vrfName)
    ipAddress = buildIpAddress(subnet,deviceOrder, ipOffsetXfer)
    ipPrefixlen = buildPrefixlen(subnet)
    
    newInterfaceVlanXferFwObject = newInterfaceVlanXferFw(interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefixlen, ospfPassword , ospfProcess, ospfArea)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet10', newInterfaceVlanXferFwObject.__dict__)
    }    
    
    return rendered_buildConfig
    
class newInterfaceLoopback:

    def __init__(self, interfaceName, interfaceNumber, vrfName, ipAddress, ipPrefixlen, ospfProcess, ospfArea):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefixlen = ipPrefixlen
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea
        
def task_buildConfig_newInterfaceLoopback_fp(playbook,role, hostName,inputPlaybook, groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars['hostOrder']
    designGroupVar = groupVars['design']
    
    #setting up variables from inputPlaybook
    interfaceNumber = inputPlaybook['vlanId']
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    subnet = inputPlaybook['ipNetworkLoopBack']
   
    #setup variables from group vars
    interfaceName = designGroupVar['interfaceVlanName']
    deviceOrder= hostOrderGroupVar['deviceOrder']
    ipOffsetLoopback = hostOrderGroupVar['ipOffsetLoopback']
    
    #build variables from groupVars, inputVars
    ipAddress = buildIpAddress(subnet,deviceOrder, ipOffsetLoopback)
    ipPrefixlen = buildPrefixlen(subnet)
    
    newInterfaceLoopbackObject = newInterfaceLoopback(interfaceName, interfaceNumber, vrfName, ipAddress, ipPrefixlen , ospfProcess, ospfArea)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet8', newInterfaceLoopbackObject.__dict__)
    }    
    
    return rendered_buildConfig
    
    
class newOspf:

    def __init__(self,ospfProcess, vrfName, routerId, ospfArea):
        
        self.ospfProcess = ospfProcess        
        self.vrfName = vrfName        
        self.routerId = routerId
        self.ospfArea = ospfArea
        
def task_buildConfig_newOspf_fp(playbook,role, hostName,inputPlaybook, groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars['hostOrder']
    designGroupVar = groupVars['design']
    
    #setting up variables from inputPlaybook
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    subnet = inputPlaybook['ipNetworkLoopBack']
    
    #setup variables from group vars
    deviceOrder= hostOrderGroupVar['deviceOrder']
    ipOffsetLoopback = hostOrderGroupVar['ipOffsetLoopback']
    routerId = designGroupVar['routerIdFunction'](subnet,ipOffsetLoopback,deviceOrder)

    newOspfObject = newOspf(ospfProcess, vrfName, routerId, ospfArea)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet9', newOspfObject.__dict__)
    }    
    
    return rendered_buildConfig
    

class newNetwork:

    #dswX4
    def __init__(self, interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefixlen, ospfProcess, ospfArea, hsrpGroup, hsrpAuth, deviceOrder,hsrpPriority, hsrpVip ):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.interfaceDescription = interfaceDescription
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefixlen = ipPrefixlen
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea
        self.hsrpGroup = hsrpGroup
        self.hsrpAuth = hsrpAuth
        self.deviceOrder = deviceOrder
        self.hsrpPriority = hsrpPriority
        self.hsrpVip = hsrpVip


    
def task_buildConfig_newNetwork_fp(playbook,role, hostName,inputPlaybook, groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars['hostOrder']
    designGroupVar = groupVars['design']
    
    #setting up variables from inputPlaybook
    vlanId = inputPlaybook['vlanId']
    interfaceNumber = inputPlaybook['vlanId']
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    subnet = inputPlaybook['ipNetwork']
    hsrpGroup = inputPlaybook['hsrpGroup']
   
    #setup variables from group vars
    interfaceName = designGroupVar['interfaceVlanName']
    interfaceDescription = designGroupVar['interfaceDescriptionServer']
    deviceOrder= hostOrderGroupVar['deviceOrder']
    ipOffsetServer = hostOrderGroupVar['ipOffsetServer']
    hsrpVipOffset = designGroupVar['hsrpVipOffset']
    
    #build variables from groupVars, inputVars
    ipAddress = buildIpAddress(subnet,deviceOrder, ipOffsetXfer)
    ipPrefixlen = buildPrefixlen(subnet)
    hsrpAuth = designGroupVar['hsrpAuthFunction'](vlanId)
    hsrpPriority = hostOrderGroupVar['hsrpPriority']
    hsrpVip = designGroupVar['HsrpVipFunction'](subnet,hsrpVipOffset)
    
    newNetworkObject = newNetwork(interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefixlen, ospfProcess, ospfArea, hsrpGroup, hsrpAuth, deviceOrder,hsrpPriority, hsrpVip )
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet11', newNetworkObject.__dict__)
    }    
    
    return rendered_buildConfig
    

        
    