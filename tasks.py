from snippets import *
from helper import *
from group_vars import *



def task_buildConfig_newVrf_fp_function(printHostName,hostName,inputPlaybook,groupVars):
     
    #setting up variables from inputPlaybook
    vrfName = inputPlaybook['vrfName']
    
    newVrfObject = newVrf(vrfName)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet1', {"snippetObject": newVrfObject.__dict__ }),
        "printHostName": printHostName
    }    
    
    return rendered_buildConfig

task_buildConfig_newVrf_fp = {
    "description":  "build snippet for newVrf",
    "function": task_buildConfig_newVrf_fp_function
}

def task_buildConfig_newInterfaceVlanXferFw_fp_function(printHostName,hostName,inputPlaybook,groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars[hostName]['hostOrder']
    designGroupVar = groupVars[hostName]['design']
    
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
    ipPrefix = buildPrefixlen(subnet)
    
    newInterfaceVlanXferFwObject = newInterfaceVlanXferFw(interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefix, ospfPassword , ospfProcess, ospfArea)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet4', {"snippetObject": newInterfaceVlanXferFwObject.__dict__ }),
        "printHostName": printHostName
    }    
    
    return rendered_buildConfig

task_buildConfig_newInterfaceVlanXferFw_fp = {
    "description": "build snippet for newInterfaceVlanXferFw",
    "function": task_buildConfig_newInterfaceVlanXferFw_fp_function
}    


def task_buildConfig_newInterfaceLoopback_fp_function(printHostName,hostName,inputPlaybook,groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars[hostName]['hostOrder']
    designGroupVar = groupVars[hostName]['design']
    
    #setting up variables from inputPlaybook
    interfaceNumber = inputPlaybook['interfaceLoopbackNumber']
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    subnet = inputPlaybook['ipNetworkLoopBack']
   
    #setup variables from group vars
    interfaceName = designGroupVar['intefaceLoopbackName']
    deviceOrder= hostOrderGroupVar['deviceOrder']
    ipOffsetLoopback = hostOrderGroupVar['ipOffsetLoopback']
    
    #build variables from groupVars, inputVars
    ipAddress = buildIpAddress(subnet,deviceOrder, ipOffsetLoopback)
    ipPrefix = designGroupVar['LoopbackPrefix']
    
    newInterfaceLoopbackObject = newInterfaceLoopback(interfaceName, interfaceNumber, vrfName, ipAddress, ipPrefix , ospfProcess, ospfArea)
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet2', {"snippetObject": newInterfaceLoopbackObject.__dict__ }),
        "printHostName": printHostName
    }    
    
    return rendered_buildConfig

task_buildConfig_newInterfaceLoopback_fp = {
    "description": "build snippet for newInterfaceLoopback",
    "function": task_buildConfig_newInterfaceLoopback_fp_function
    
}

def task_buildConfig_newOspf_fp_function(printHostName,hostName,inputPlaybook,groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars[hostName]['hostOrder']
    designGroupVar = groupVars[hostName]['design']
    
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
        "renderedSnippet": gen_snippet('snippet3', {"snippetObject": newOspfObject.__dict__ }),
        "printHostName": printHostName
    }    
    
    return rendered_buildConfig

task_buildConfig_newOspf_fp = {
    "description": "newOspf",
    "function": task_buildConfig_newOspf_fp_function
}

def task_buildConfig_newNetwork_fp_function(printHostName,hostName,inputPlaybook,groupVars):
    
    #setting up group vars
    hostOrderGroupVar = groupVars[hostName]['hostOrder']
    designGroupVar = groupVars[hostName]['design']
    
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
    ipAddress = buildIpAddress(subnet,deviceOrder, ipOffsetServer)
    ipPrefix = buildPrefixlen(subnet)
    hsrpAuth = designGroupVar['hsrpAuthFunction'](vlanId)
    hsrpPriority = hostOrderGroupVar['hsrpPriority']
    hsrpVip = designGroupVar['HsrpVipFunction'](subnet,hsrpVipOffset)
    

    newNetworkObject = newNetwork(interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefix, ospfProcess, ospfArea, hsrpGroup, hsrpAuth, deviceOrder,hsrpPriority, hsrpVip )
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": gen_snippet('snippet5',{"snippetObject":  newNetworkObject.__dict__ }),
        "printHostName": printHostName
    }    
    
    return rendered_buildConfig

task_buildConfig_newNetwork_fp = {
    "description": "build snippet for newNetwork",
    "function": task_buildConfig_newNetwork_fp_function
}

def task_validate_vrfName_function(role,inputPlaybook):
    
    if 'vrfName' in inputPlaybook and inputPlaybook['vrfName'] != None:
        vrfName = inputPlaybook['vrfName']
    else:
        print('Invalid input for variable vrfName: vrfName input empty or vrfName key not included')
        return -1

    if ( len(vrfName) > 32  ) or  ( len(vrfName)  == 0 )  or ( re.search("[^a-zA-Z0-9\\-;_]", vrfName) != None ):
        print('Invalid input for variable vrfName: vrfName input is not valid')
        return -1
        
    return 1

task_validate_vrfName = {
    "description": "validate vrfName",
    "function": task_validate_vrfName_function
}

def task_validate_vlanId_function(role,inputPlaybook):
    
    if 'vlanId' in inputPlaybook and inputPlaybook['vlanId'] != None:
        vlanId = inputPlaybook['vlanId']
    else:
        print('Invalid input for variable vlanId: vlanId input empty or vlanId key not included')
        return -1
    
    if isInt(vlanId):
        if ( vlanId < 1 ) or ( vlanId > 4095 ):
            print('Invalid input for variable vlanId: vlanId input is less than 1 or more than 4095')
            return -1
            
    return 1

task_validate_vlanId = {
    "description": "validate vlanId",
    "function": task_validate_vlanId_function
}

def task_validate_ospfProcess_function(role,inputPlaybook):
    
    if 'ospfProcess' in inputPlaybook and inputPlaybook['ospfProcess'] != None:
        ospfProcess = inputPlaybook['ospfProcess']
    else:
        print('Invalid input for variable ospfProcess: ospfProcess input empty or ospfProcess key not included')
        return -1
    
    if isInt(ospfProcess):
        if ( ospfProcess  < 1 ) or  ( ospfProcess > 65535 ):
            print('Invalid input for variable vlanId: vlanId input is less than 1 or more than 65535')
            return -1
    
    return 1 

task_validate_ospfProcess = {
    "description": "validate ospfProcess",
    "function": task_validate_ospfProcess_function
}


def task_validate_ospfArea_function(role,inputPlaybook):
    
    if 'ospfArea' in inputPlaybook and inputPlaybook['ospfArea'] != None:
        ospfArea = inputPlaybook['ospfArea']
    else:
        print('Invalid input for variable ospfArea: ospfArea input empty or ospfArea key not included')
        return -1
    
    if isInt(ospfArea) or not isOspfArea(ospfArea): 
        print('Invalid input for variable ospfArea: ospfArea input is not valid')
        return -1
            
    return 1

task_validate_ospfArea = {
    "description": "validate ospfArea",
    "function": task_validate_ospfArea_function
}

def task_validate_ipNetwork_function(role,inputPlaybook):
    
    if role['inputVar'] in inputPlaybook and inputPlaybook[role['inputVar']] != None:
        subnet = inputPlaybook[role['inputVar']]
    else:
        print('Invalid input for variable ' +  role['inputVar'] + ': ' + role['inputVar'] + ' input empty or ' + role['inputVar'] + ' key not included')
        return -1
    
    if not isSubnet(subnet):
        print('Invalid input for variable ' +  role['inputVar'] + ': ' + role['inputVar'] + ' is not valid')
        return -1
    
    return 1  

task_validate_ipNetwork = {
    "description": "validate ipNetwork",
    "function": task_validate_ipNetwork_function
}

def task_validate_interfaceLoopBackNumber_function(role,inputPlaybook):
    
    if 'interfaceLoopbackNumber' in inputPlaybook and inputPlaybook['interfaceLoopbackNumber'] != None:
        interfaceLoopbackNumber = inputPlaybook['interfaceLoopbackNumber']
    else:
        print('Invalid input for variable interfaceLoopbackNumber: interfaceLoopbackNumber input empty or interfaceLoopbackNumber key not included')
        return -1
    
    if isInt(interfaceLoopbackNumber):
        if ( interfaceLoopbackNumber  < 0 ) or ( interfaceLoopbackNumber > 1023 ):
            print('Invalid input for variable interfaceLoopbackNumber: interfaceLoopbackNumber is less than 0 or higher than 1023')
            return -1
    
    return 1 

task_validate_interfaceLoopBackNumber = {
    "description": "validate interfaceLoopBackNumber",
    "function": task_validate_interfaceLoopBackNumber_function
}


def task_validate_idNumber_function(role,inputPlaybook):
    
    if 'idNumber' in inputPlaybook and inputPlaybook['idNumber'] != None:
        idNumber = inputPlaybook['idNumber']
    else:
        print('Invalid input for variable idNumber: idNumber input empty or idNumber key not included')
        return -1

    if len(idNumber) > 15  or len(idNumber)  == 0:
        print('Invalid input for variable idNumber: idNumber lenght is  0 or higher than 15')
        return -1
        
    return 1

task_validate_idNumber = {
    "description": "validate idNumber",
    "function": task_validate_idNumber_function
}

def task_validate_hsrpGroup_function(role,inputPlaybook):
    
    if 'hsrpGroup' in inputPlaybook and inputPlaybook['hsrpGroup'] != None:
        hsrpGroup = inputPlaybook['hsrpGroup']
    else:
        print('Invalid input for variable hsrpGroup: hsrpGroup input empty or hsrpGroup key not included')
        return -1
        
    if isInt(hsrpGroup):
        if ( hsrpGroup < 1 ) or ( hsrpGroup > 4095 ):
            print('Invalid input for variable hsrpGroup: hsrpGroup lenght is less than 1 or higher than 4095')
            return -1
    
    return 1

task_validate_hsrpGroup = {
    "description": "validate hsrpGroup",
    "function": task_validate_hsrpGroup_function
}

def task_validate_hostslist_function(role,inputPlaybook):
    
    if 'hostslist' in inputPlaybook and inputPlaybook['hostslist'] != None:
        hostslist = inputPlaybook['hostslist']
    else:
        print('Invalid input for variable hostslist: hostslist input empty or hostslist key not included')
        return -1
    
    index = 0
    for hostName in hostslist:
        if index == 0 and not hostName in firstsHosts:
            printHostNameError()
            return -1
        elif index == 1 and not hostName in secondsHosts:
            printHostNameError()
            return -1
        elif index == 2 and not hostName in thirdsHosts:
            printHostNameError()
            return -1
        elif index == 3 and not hostName in fourthsHosts:
            printHostNameError()
            return -1
            
        index = index + 1
    
    return 1
    
task_validate_hostslist = {
    "description": "validate hostslist",
    "function": task_validate_hostslist_function
}