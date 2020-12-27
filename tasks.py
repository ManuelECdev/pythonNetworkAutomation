#- name: BUILD CONFIGS
#  buildSnippet:
#    src: "{{templateName}}.j2"
#    dest: "/etc/ansible/configs/{{idNumber}}/{{idNumber}}_{{hostname}}_{{templateName}}.cfg"

from snippets import *
from helper import *


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
    
task_validate_vrfName = {
    "description": "validate vrfName",
    "name": task_validate_vrfName_function
}

def task_validate_vrfName_function(role,inputPlaybook):
    
    vrfName = inputPlaybook['vrfName']

    if ( len(vrfName) > 32  ) or  ( len(vrfName)  == 0 )  or ( re.search("[^a-zA-Z0-9\\-;_]", vrfName) != None ):
        return -1
        
    return 1



task_validate_vlanId = {
    "description": "validate vlanId",
    "name": task_validate_vlanId_function
}

def task_validate_vlanId_function(role,inputPlaybook):
    
    vlanId = inputPlaybook['vlanId']
    
    if isInt(vlanId):
        if ( vlanId < 1 ) or ( vlanId > 4095 ):
            return -1
            
    return 1

task_validate_ospfProcess = {
    "description": "validate ospfProcess",
    "name": task_validate_ospfProcess_function
}

def task_validate_ospfProcess_function(role,inputPlaybook):
    
    ospfProcess = inputPlaybook['ospfProcess']
    
    if isInt(ospfProcess):
        if ( ospfProcess  < 1 ) or  ( ospfProcess > 65535 ):
            return -1
    
    return 1 

task_validate_ospfArea = {
    "description": "validate ospfArea",
    "name": task_validate_ospfArea_function
}

def task_validate_ospfArea_function(role,inputPlaybook):
    
    ospfArea = inputPlaybook['ospfArea']
    
    if isInt(ospfArea) or not isOspfArea(ospfArea): 
        return -1
            
    return 1

task_validate_ipNetwork = {
    "description": "validate ipNetwork",
    "name": task_validate_ipNetwork_function
}

def task_validate_ipNetwork_function(role,inputPlaybook):
    
    subnet = inputPlaybook[role['inputVar']]
    
    if isSubnet(subnet):
        return 1
    
    return -1  

task_validate_interfaceLoopBackNumber = {
    "description": "validate interfaceLoopBackNumber",
    "name": task_validate_interfaceLoopBackNumber_function
}

def task_validate_interfaceLoopBackNumber_function(role,inputPlaybook):
    
    interfaceLoopbackNumber = inputPlaybook['interfaceLoopbackNumber']
    
    if isInt(interfaceLoopbackNumber):
        if ( interfaceLoopbackNumber  < 0 ) or  ( interfaceLoopbackNumber > 1023 ):
            return -1
    
    return 1 

task_validate_idNumber = {
    "description": "validate idNumber",
    "name": task_validate_idNumber_function
}

def task_validate_idNumber_function(role,inputPlaybook):
    
    idNumber = inputPlaybook['idNumber']

    if len(idNumber) > 15  or len(idNumber)  == 0:
        return -1
        
    return 1

task_validate_hsrpGroup = {
    "description": "validate hsrpGroup",
    "name": task_validate_hsrpGroup_function
}

def task_validate_hsrpGroup_function(role,inputPlaybook):
    
    hsrpGroup = inputPlaybook['hsrpGroup']
    
    if isInt(hsrpGroup):
        if ( hsrpGroup < 1 ) or ( hsrpGroup > 4095 ):
            return -1
    
    return 1

task_validate_hostslist = {
    "description": "validate hostslist",
    "name": "validateHostslist"
}