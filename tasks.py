#- name: BUILD CONFIGS
#  buildSnippet:
#    src: "{{templateName}}.j2"
#    dest: "/etc/ansible/configs/{{idNumber}}/{{idNumber}}_{{hostname}}_{{templateName}}.cfg"

from snippets import *
from helper import *

task_buildConfig_newVrf_fp = {
    "description":  "build snippet for newVrf",
    "task": task_buildConfig_newVrf_fp_function
}

def task_buildConfig_newVrf_fp_function(playbook,role, hostName,inputPlaybook):
     
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": None
    }
    
    #setting up variables from inputPlaybook
    vrfName = inputPlaybook['vrfName']
    
    newVrfObject = newVrf(vrfName)
    
    rendered_buildConfig['renderedSnippet']  = gen_snippet('snippet7', newVrfObject.__dict__)
    
    return rendered_buildConfig
    
task_buildConfig_newInterfaceVlanXferFw_fp = {
    "description": "build snippet for newInterfaceVlanXferFw",
    "task": task_buildConfig_newInterfaceVlanXferFw_fp_function
}
    
def task_buildConfig_newInterfaceVlanXferFw_fp_function(playbook,role, hostName,inputPlaybook, groupVars):
    
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
    

task_buildConfig_newInterfaceLoopback_fp = {
    "description": "build snippet for newInterfaceLoopback",
    "task": task_buildConfig_newInterfaceLoopback_fp_function
    
}

def task_buildConfig_newInterfaceLoopback_fp_function(playbook,role, hostName,inputPlaybook, groupVars):
    
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
    
task_buildConfig_newOspf_fp = {
    "description": "newOspf",
    "task": task_buildConfig_newOspf_fp_function
}
    
def task_buildConfig_newOspf_fp_function(playbook,role, hostName,inputPlaybook, groupVars):
    
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
    
task_buildConfig_newNetwork_fp = {
    "description": "build snippet for newNetwork",
    "task": task_buildConfig_newNetwork_fp_function
}
    
def task_buildConfig_newNetwork_fp_function(playbook,role, hostName,inputPlaybook, groupVars):
    
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
    
    if 'vrfName' in inputPlaybook:
        vrfName = inputPlaybook['vrfName']
    else:
        return -1

    if ( len(vrfName) > 32  ) or  ( len(vrfName)  == 0 )  or ( re.search("[^a-zA-Z0-9\\-;_]", vrfName) != None ):
        return -1
        
    return 1


task_validate_vlanId = {
    "description": "validate vlanId",
    "name": task_validate_vlanId_function
}

def task_validate_vlanId_function(role,inputPlaybook):
    
    if 'vlanId' in inputPlaybook:
        vlanId = inputPlaybook['vlanId']
    else:
        return -1
    
    if isInt(vlanId):
        if ( vlanId < 1 ) or ( vlanId > 4095 ):
            return -1
            
    return 1

task_validate_ospfProcess = {
    "description": "validate ospfProcess",
    "name": task_validate_ospfProcess_function
}

def task_validate_ospfProcess_function(role,inputPlaybook):
    
    if 'ospfProcess' in inputPlaybook:
        ospfProcess = inputPlaybook['ospfProcess']
    else:
        return -1
    
    if isInt(ospfProcess):
        if ( ospfProcess  < 1 ) or  ( ospfProcess > 65535 ):
            return -1
    
    return 1 

task_validate_ospfArea = {
    "description": "validate ospfArea",
    "name": task_validate_ospfArea_function
}

def task_validate_ospfArea_function(role,inputPlaybook):
    
    if 'ospfArea' in inputPlaybook:
        ospfArea = inputPlaybook['ospfArea']
    else:
        return -1
    
    if isInt(ospfArea) or not isOspfArea(ospfArea): 
        return -1
            
    return 1

task_validate_ipNetwork = {
    "description": "validate ipNetwork",
    "name": task_validate_ipNetwork_function
}

def task_validate_ipNetwork_function(role,inputPlaybook):
    
    if role['inputVar'] in inputPlaybook:
        subnet = inputPlaybook[role['inputVar']]
    else:
        return -1
    
    if isSubnet(subnet):
        return 1
    
    return -1  

task_validate_interfaceLoopBackNumber = {
    "description": "validate interfaceLoopBackNumber",
    "name": task_validate_interfaceLoopBackNumber_function
}

def task_validate_interfaceLoopBackNumber_function(role,inputPlaybook):
    
    if 'interfaceLoopbackNumber' in inputPlaybook:
        interfaceLoopbackNumber = inputPlaybook['interfaceLoopbackNumber']
    else:
        return -1
    
    if isInt(interfaceLoopbackNumber):
        if ( interfaceLoopbackNumber  < 0 ) or  ( interfaceLoopbackNumber > 1023 ):
            return -1
    
    return 1 

task_validate_idNumber = {
    "description": "validate idNumber",
    "name": task_validate_idNumber_function
}

def task_validate_idNumber_function(role,inputPlaybook):
    
    if 'idNumber' in inputPlaybook:
        idNumber = inputPlaybook['idNumber']
    else:
        return -1

    if len(idNumber) > 15  or len(idNumber)  == 0:
        return -1
        
    return 1

task_validate_hsrpGroup = {
    "description": "validate hsrpGroup",
    "name": task_validate_hsrpGroup_function
}

def task_validate_hsrpGroup_function(role,inputPlaybook):
    
    if 'hsrpGroup' in inputPlaybook:
        hsrpGroup = inputPlaybook['hsrpGroup']
    else:
        return -1
        
    if isInt(hsrpGroup):
        if ( hsrpGroup < 1 ) or ( hsrpGroup > 4095 ):
            return -1
    
    return 1

task_validate_hostslist = {
    "description": "validate hostslist",
    "name": task_validate_hostslist_function
}

def task_validate_hostslist_function(role,inputPlaybook):
    
    if 'hostlists' in inputPlaybook:
        hostlists = inputPlaybook['hostlists']
    else:
        return -1
    
    for (index,hostName) in hostlists:
        if index == 0 and not hostName in firstsHosts:
            return -1
        elif index == 1 and not hostName in secondsHosts:
            return -1
        elif index == 2 and not hostName in thirdsHosts:
            return -1
        elif index == 3 and not hostName in fourthsHosts:
            return -1
    
    return 1