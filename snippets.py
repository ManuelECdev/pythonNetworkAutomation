class newVrf:

    def __init__(self, vrfName):
        
        self.vrfName = vrfName
        
class newInterfaceVlanXferFw:

    def __init__(self, interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefix, ospfPassword, ospfProcess, ospfArea):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.interfaceDescription = interfaceDescription
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefix = ipPrefix
        self.ospfPassword = ospfPassword
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea
        
class newInterfaceLoopback:

    def __init__(self, interfaceName, interfaceNumber, vrfName, ipAddress, ipPrefix, ospfProcess, ospfArea):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefix = ipPrefix
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea
        
        
class newOspf:

    def __init__(self,ospfProcess, vrfName, routerId, ospfArea):
        
        self.ospfProcess = ospfProcess        
        self.vrfName = vrfName        
        self.routerId = routerId
        self.ospfArea = ospfArea
        
        
class newNetwork:

    def __init__(self, interfaceName, interfaceNumber, interfaceDescription, vrfName, ipAddress, ipPrefix, ospfProcess, ospfArea, hsrpGroup, hsrpAuth, deviceOrder,hsrpPriority, hsrpVip ):

        self.interfaceName = interfaceName
        self.interfaceNumber = interfaceNumber
        self.interfaceDescription = interfaceDescription
        self.vrfName = vrfName        
        self.ipAddress = ipAddress
        self.ipPrefix = ipPrefix
        self.ospfProcess = ospfProcess
        self.ospfArea = ospfArea
        self.hsrpGroup = hsrpGroup
        self.hsrpAuth = hsrpAuth
        self.deviceOrder = deviceOrder
        self.hsrpPriority = hsrpPriority
        self.hsrpVip = hsrpVip