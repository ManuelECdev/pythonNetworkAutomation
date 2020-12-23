from helper import *

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
    
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": None
    }
    
    #setting up group vars
    hostOrderGroupVar = groupVars['hostOrder']
    designGroupVar = groupVars['design']
    
    #setting up variables from inputPlaybook
    interfaceNumber = inputPlaybook['vlanId']
    vrfName = inputPlaybook['vrfName']
    ospfProcess = inputPlaybook['ospfProcess']
    ospfArea = inputPlaybook['ospfArea']
    
    #setup variables from group vars
    interfaceName = designGroupVar['interfaceVlanName']
    interfaceDescription = designGroupVar['interfaceDescriptionXferFw']
    ospfPassword = None
    ipAddress = None
    ipPrefixlen = None
    
    newInterfaceVlanXferFwObject = newInterfaceVlanXferFw(interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefixlen, ospfPassword , ospfProcess, ospfArea)
    
    rendered_buildConfig['renderedSnippet']  = gen_snippet('snippet10', newInterfaceVlanXferFwObject.__dict__)
    
    return rendered_buildConfig