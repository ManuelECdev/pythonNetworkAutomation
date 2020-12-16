import sys
import re
import fileinput
import ast
import os
import ipaddress
import copy
from helper import *
from Global import *

class snippetBlock:

    def __init__(self, data):
        self.deviceName = data['deviceName']
        self.configurationSnippetsNames = data['configurationSnippetsNames']
        self.preTestSnippets = data['preTestSnippets']
        self.preVerifySnippets = data['preVerifySnippets']

        self.configrationSnippets = []
        for configurationSnippetsName in data['configurationSnippetsNames']:
            self.configrationSnippets.append({'name': configurationSnippetsName, 'snippet': {} })

        self.postVerifySnippets = data['postVerifySnippets']
        self.postTestSnippets = data['postTestSnippets']

class snippet1:

    #aswX3
    def __init__(self, data,configurationSnippetNameOder,deviceNameOrder):

        #Array
        self.interfaces = data['interfacesSnippet1']

class snippet2:

    #crtX4
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):

        self.interfaces = []


        # transform the Input

        resultTransformInput = snippet2.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'interfaces':
                self.interfaces = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}
        #interfaces Section
        interfaces = []

        deviceName = inputData['devicesNames'][deviceNameOrder]

        for interfaceOrder,interface in enumerate(inputData['interfacesSnippet2']):

        #if 'interfacesSnippet2' in inputData:

            #interface = inputData['interfacesSnippet2']

            ipMask = None
            interfaceNumber = None
            ospfPriority = None

            interfaceType = interface['interfaceType']
            topology = inputData['topology']
            vrfname = interface['vrfName']

            # transform IpMask

            ipMask = templateHelper.transformIpNetworkChangeIps(interface['ipMask'],interfaceType,deviceNameOrder,vrfname, topology, deviceName)

            # transform interfaceNumber

            interfaceNumber = interface['interfacesNumbers'][deviceNameOrder]

            interfaces.append({ 'vrfName': interface['vrfName'], 'interfaceName': interface['interfaceName'], 'vlanId': interface['vlanId'],
                'ipMask': ipMask, 'interfaceNumber': interfaceNumber, 'description': interface['description'] })

        result['interfaces'] = interfaces

        return result

class snippet3:

    #crtX5
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):

        self.prefixLists = []

        # transform the Input

        resultTransformInput = snippet3.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'prefixLists':
                self.prefixLists = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        #prefixList Section
        prefixLists = []

        for prefixListOrder,prefixList in enumerate(inputData['prefixListsSnippet3']):

            # transform IpMask

            ipNetworks = templateHelper.transformIpMasks(prefixList['ipMasks'],'prefixlen')
            prefixLists.append({ 'name': prefixList['name'], 'ipMasks': ipNetworks })

        result['prefixLists'] = prefixLists

        return result

class snippet4:

    #crtX6
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):

        self.prefixLists = []

        # transform the Input

        resultTransformInput = snippet4.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'prefixLists':
                self.prefixLists = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        #prefixList Section
        prefixLists = []

        for prefixListOrder,prefixList in enumerate(inputData['prefixListsSnippet4']):

            # transform IpMask

            ipNetworks = templateHelper.transformIpMasks(prefixList['ipMasks'],'prefixlen')
            prefixLists.append({ 'name': prefixList['name'], 'ipMasks': ipNetworks })

        result['prefixLists'] = prefixLists

        return result

class snippet5:

    #crtX7
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.ospfs = []

        # transform the Input

        resultTransformInput = snippet5.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'ospfs':
                self.ospfs = transformInputValue

    @staticmethod
    def transformInput(rawInput,deviceNameOrder):

        result = {}

        #ospf Section
        ospfs = []

        for ospfOrder,ospf in enumerate(rawInput['ospfsSnippet5']):

        #if 'ospfsSnippet5' in inputData:

            #ospf = inputData['ospfsSnippet5']

            # transform interfaceNumber

            interfaceNumber = ospf['interfacesNumbers'][deviceNameOrder]

            ospfs.append({ 'ospfProcess': ospf['ospfProcess'], 'vrfName': ospf['vrfName'],'ospfArea': ospf['ospfArea'], 'interfaceNumber': interfaceNumber, 'interfaceName':  ospf['interfaceName'], 'vlanId': ospf['vlanId'], 'ospfPassword': ospf['ospfPassword'] })

        result['ospfs'] = ospfs

        return result

class snippet6:

    #cswX1
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):

        self.interfaces = []


        # transform the Input

        resultTransformInput = snippet6.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'interfaces':
                self.interfaces = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}
        #interfaces Section
        interfaces = []

        deviceName = inputData['devicesNames'][deviceNameOrder]

        for interfaceOrder,interface in enumerate(inputData['interfacesSnippet6']):

        #if 'interfacesSnippet6' in inputData:

            #interface = inputData['interfacesSnippet6']

            ipMask = None
            interfaceNumber = None
            ospfPriority = None

            interfaceType = interface['interfaceType']
            topology = inputData['topology']
            vrfname = interface['vrfName']

            # transform IpMask

            ipMask = templateHelper.transformIpNetworkChangeIps(interface['ipMask'],interfaceType,deviceNameOrder,vrfname, topology, deviceName)

            # transform interfaceNumber

            interfaceNumber = interface['interfacesNumbers'][deviceNameOrder]

            # transform ospfPriority

            ospfPriority = interface['ospfPriority'][deviceNameOrder]

            interfaces.append({ 'vrfName': interface['vrfName'], 'ospfArea': interface['ospfArea'], 'interfaceName': interface['interfaceName'], 'vlanId': interface['vlanId'], 'ospfProcess': interface['ospfProcess'],
                'ipMask': ipMask, 'interfaceNumber': interfaceNumber, 'ospfPassword': interface['ospfPassword'], 'ospfPriority': ospfPriority })


        result['interfaces'] = interfaces

        return result

class snippet7:

    #dswX1
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.context = data['contextSnippet7']

class snippet8:

    #dswX2
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.interfaces = []

        # transform the Input

        resultTransformInput = snippet8.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'interfaces':
                self.interfaces = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        #interfaces Section
        interfaces = []

        deviceName = inputData['devicesNames'][deviceNameOrder]

        #for interfaceOrder,interface in enumerate(inputData['interfacesSnippet8']):

        if 'interfacesSnippet8' in inputData:

            interface = inputData['interfacesSnippet8']

            ipMask = None

            interfaceType = interface['interfaceType']
            topology = inputData['topology']
            vrfname = interface['vrfName']

            ipMask = templateHelper.transformIpNetworkChangeIps(interface['ipMask'],interfaceType,deviceNameOrder,vrfname, topology, deviceName)

            if ipMask != None:
                interfaces.append({ 'interfaceName': interface['interfaceName'], 'interfaceNumber': interface['interfaceNumber'], 'vrfName': interface['vrfName'], 'ipMask': ipMask, 'ospfProcess': interface['ospfProcess'], 'ospfArea': interface['ospfArea'] })

        result['interfaces'] = interfaces

        return result

class snippet9:

    #dswX3
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.ospf = {}

        # transform the Input

        resultTransformInput = snippet9.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'ospf':
                self.ospf = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        deviceName = inputData['devicesNames'][deviceNameOrder]

        #ospf Section
        ospf = {}

        if 'ospfSnippet9' in inputData:

            ospf = inputData['ospfSnippet9']

            interfaceType = "loopback"
            topology = inputData['topology']
            vrfname = ospf['vrfName']

            newOspf = {}
            if 'routerId' in ospf:
                ospfRouterId = templateHelper.transformOspfRouterIdNetworkToIp(ospf['routerId'],deviceNameOrder,vrfname, topology, deviceName)
                newOspf = { 'ospfProcess': ospf['ospfProcess'], 'vrfName': ospf['vrfName'], 'routerId': ospfRouterId, 'ospfArea': ospf['ospfArea'] }

            result['ospf'] = newOspf

        return result

class snippet10:

    #dswX4
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.interfaces = []

        resultTransformInput = snippet10.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'interfaces':
                self.interfaces = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        #interfaces Section
        interfaces = []

        deviceName = inputData['devicesNames'][deviceNameOrder]

        #for interfaceOrder,interface in enumerate(inputData['interfacesSnippet10']):

        if 'interfacesSnippet10' in inputData:

            interface = inputData['interfacesSnippet10']

            ipMask = None
            interfaceNumber = None
            ospfPriority = None

            interfaceType = interface['interfaceType']
            topology = inputData['topology']
            vrfname = interface['vrfName']

            # transform IpMask

            ipMask = templateHelper.transformIpNetworkChangeIps(interface['ipMask'],interfaceType,deviceNameOrder,vrfname, topology, deviceName)

            if ipMask != None:
                interfaces.append({ 'interfaceName': interface['interfaceName'], 'interfaceNumber': interface['interfaceNumber'], 'interfaceDescription': interface['interfaceDescription'], 'vrfName': interface['vrfName'], 'ospfPassword': interface['ospfPassword'],
                    'ipMask': ipMask, 'ospfProcess': interface['ospfProcess'], 'ospfArea': interface['ospfArea'] })

        result['interfaces'] = interfaces

        return result

class snippet11:

    #dswX5
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):
        self.interfaces = []

        resultTransformInput = snippet11.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'interfaces':
                self.interfaces = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        deviceName = inputData['devicesNames'][deviceNameOrder]

        #interfaces Section
        interfaces = []

        for interfaceOrder,interface in enumerate(inputData['interfacesSnippet11']):

            ipMask = None
            interfaceNumber = None
            ospfPriority = None

            interfaceType = interface['interfaceType']
            topology = inputData['topology']
            vrfname = interface['vrfName']

            # transform IpMask

            ipMask = templateHelper.transformIpNetworkChangeIps(interface['ipMask'],interfaceType,deviceNameOrder,vrfname, topology, deviceName)

            #if ipMask != None:

            # transform hsrpPriority

            hsrpPriority = templateHelper.getHsrpPriority(deviceNameOrder,len(inputData['devicesNames']))

            # transform hsrpDelay

            hsrpDelay = templateHelper.getHsrpDelay(deviceNameOrder)

            # transform hsrpVip

            hsrpVip = str(ipaddress.ip_network(interface['ipMask']).network_address + 1)

            interfaces.append({ 'interfaceName': interface['interfaceName'], 'interfaceNumber': interface['vlanId'], 'interfaceDescription': interface['interfaceDescription'], 'vrfName': interface['vrfName'],
                'ipMask': ipMask, 'ospfProcess': interface['ospfProcess'], 'ospfArea': interface['ospfArea'], 'hsrpPriority': hsrpPriority, 'hsrpDelay': hsrpDelay, 'hsrpVip': hsrpVip, 'hsrpId': interface['hsrpId'], 'hsrpAuth': interface['vlanId']  })

        result['interfaces'] = interfaces

        return result

class snippet12:

    #fwbX2
    def __init__(self, data,configurationSnippetNameOder,deviceNameOrder):

        self.bgp = {}

        # transform the Input

        resultTransformInput = snippet12.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'bgp':
                self.bgp = transformInputValue

    @staticmethod
    def transformInput(rawInput,deviceNameOrder):

        result = {}

        #bgp Section
        bgp = {}

        if 'bgpSnippet12' in rawInput:
            bgp = rawInput['bgpSnippet12']

            newBgp = {}
            if 'ipMasks' in bgp:
                ipMasks = templateHelper.transformIpMasks(bgp['ipMasks'],'mask')
                newBgp = { 'asNumber': bgp['asNumber'], 'ipMasks': ipMasks }

            result['bgp'] = newBgp

        return result

class snippet13:

    #fwbX3
    def __init__(self, data,configurationSnippeOrder,deviceNameOrder):

        self.prefixLists = []

        # transform the Input

        resultTransformInput = snippet13.transformInput(data,deviceNameOrder)

        for transformInputKey,transformInputValue in resultTransformInput.iteritems():
            if transformInputKey == 'prefixLists':
                self.prefixLists = transformInputValue

    @staticmethod
    def transformInput(inputData,deviceNameOrder):

        result = {}

        #prefixList Section
        prefixLists = []

        for prefixListOrder,prefixList in enumerate(inputData['prefixListsSnippet13']):

        #if 'prefixListsSnippet13' in inputData:

            #interface = inputData['prefixListsSnippet13']

            # transform IpMask

            ipNetworks = templateHelper.transformIpMasks(prefixList['ipMasks'],'prefixlen')
            prefixLists.append({ 'name': prefixList['name'], 'ipMasks': ipNetworks })

        result['prefixLists'] = prefixLists

        return result

class templateHelper:


    @staticmethod
    def transformIpNetworksChangeIps(IpNetworksInput,deviceNameOrder,vrfname, topology):

        if Global['debug'] == 1:
            print IpNetworksInput

        IpNetworks = []

        for IpNetwork in IpNetworksInput:
            IpNetworks.append(templateHelper.transformIpNetworkChangeIps(IpNetwork,deviceNameOrder,vrfname, topology))

        return IpNetworks

    @staticmethod
    def transformIpNetworkChangeIps(inputIpmask,interfaceType,deviceNameOrder,vrfname, topology,deviceName):

        if Global['debug'] == 1:
            print inputIpmask

        ip = None
        prefixlen = None
        resultIpNetwork = None

        if interfaceType == 'server':
            ipAdd = templateHelper.getIpAdd(vrfname,"server",topology,deviceName)
            ip = str( ipaddress.ip_network(inputIpmask).network_address + deviceNameOrder +  ipAdd )
            prefixlen = str( ipaddress.ip_network(inputIpmask).prefixlen )
        elif interfaceType == 'loopback':
            ipAdd = templateHelper.getIpAdd(vrfname,"loopback",topology,deviceName)
            ip = str( ipaddress.ip_network(inputIpmask).network_address + deviceNameOrder + ipAdd )
            prefixlen = str( templateHelper.getMask(ipaddress.ip_network(inputIpmask).prefixlen, "loopback") )
        elif interfaceType == 'xfer':
            ipAdd = templateHelper.getIpAdd(vrfname,"xfer",topology,deviceName)
            ip = str( ipaddress.ip_network(inputIpmask).network_address + deviceNameOrder + ipAdd )
            prefixlen = str( templateHelper.getMask(ipaddress.ip_network(inputIpmask).prefixlen,"xfer") )

        if ip != None and prefixlen != None:
            resultIpNetwork = {'ip': ip, 'prefixlen' : prefixlen }

        return resultIpNetwork

    @staticmethod
    def transformOspfRouterIdNetworkToIp(inputIpmask,deviceNameOrder,vrfname, topology, deviceName):

        if Global['debug'] == 1:
            print inputIpmask

        ip = str( ipaddress.ip_network(inputIpmask).network_address + deviceNameOrder + templateHelper.getIpAdd(vrfname,"loopback",topology, deviceName) )

        return ip

    @staticmethod
    def getInterfaceNumberFromInterfacesNumbers(input,deviceNameOrder):

        if Global['debug'] == 1:
            print input

        interfaceNumber = None

        if 'interfacesNumbers' in input:
            interfaceNumber = input['interfacesNumbers'][deviceNameOrder]

        return interfaceNumber


    @staticmethod
    def transformIpMasks(inputIpmasks,type):

        if Global['debug'] == 1:
            print inputIpmasks

        resultIpMasks = []

        for IpMask in inputIpmasks:

            if type == 'prefixlen':
                resultIpMasks.append(templateHelper.transformIpMask(IpMask,'prefixlen'))
            else:
                resultIpMasks.append(templateHelper.transformIpMask(IpMask,'mask'))

        return resultIpMasks

    @staticmethod
    def transformIpMask(inputIpmask,type):

        if Global['debug'] == 1:
            print inputIpmask

        ip = str( ipaddress.ip_network(inputIpmask).network_address  )

        if type == 'prefixlen':
            prefixlen = str( ipaddress.ip_network(inputIpmask).prefixlen )
            resultIpMask = {'ip': ip, 'prefixlen' : prefixlen}
        else:
            Mask = str( ipaddress.ip_network(inputIpmask).netmask )
            resultIpMask = {'ip': ip, 'mask' : Mask }

        return resultIpMask

    @staticmethod
    def getHsrpPriority(order,devicesCount):

        hsrpPriority = 0

        if order == 0:
            hsrpPriority = 104
        elif order == 1:
            hsrpPriority = 103
        elif order == 2:
            hsrpPriority = 102
        elif order == 3:
            hsrpPriority = 101

        return str(hsrpPriority)

    @staticmethod
    def getHsrpDelay(order):

        hsrpDelay = " "

        if order == 0:
            hsrpDelay = " minimum 120 "

        return hsrpDelay

    @staticmethod
    def getIpAdd(vrfName,type,topology,deviceName):

        IpAdd = 0

        if type == "loopback" and "DSW-FW" in topology and ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 1
        elif type == "loopback" and "DSW-CSW" in topology and ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 3
        elif type == "loopback" and "DSW-VLB" in topology and ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 1            
        elif type == "xfer" and "DSW-FW" in topology and ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 2
        elif type == "xfer" and "DSW-CSW" in topology and ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 3
        elif type == "xfer" and ( "LB-DRT-CSW" in topology or "DSW-CSW" in topology ) and "csw" in deviceName:
            IpAdd = 1
        elif type == "xfer" and  "LB-DRT-FW-CRT" in topology  and "crt" in deviceName:
            IpAdd = 1
        elif type == "xfer" and  "DSW-VLB" in topology:
            IpAdd = 2
        elif type == "server" and ( "DSW-FW" in topology or "DSW-CSW" in topology or "ANY" in topology ) and  ( "dsw" in deviceName or "dvr" in deviceName ):
            IpAdd = 2

        return IpAdd

    @staticmethod
    def getMask(inputMask,type):

        Mask = inputMask

        if type == "loopback":
            Mask = 32

        return Mask

    @staticmethod
    def buildTemplate(buildTemplateInput,snippetName, deviceNameOrder,configurationSnippetNameOder):

        if Global['debug'] == 1:
            print buildTemplateInput
            print snippetName

        #if templateHelper.checkInput(buildTemplateInput) != -1:
        if 1:
            if snippetName == 'snippet1':
                return snippet1(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet2':
                return snippet2(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet3':
                return snippet3(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet4':
                return snippet4(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet5':
                return snippet5(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet6':
                return snippet6(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet7':
                return snippet7(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet8':
                return snippet8(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet9':
                return snippet9(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet10':
                return snippet10(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet11':
                return snippet11(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet12':
                return snippet12(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)
            elif snippetName == 'snippet13':
                return snippet13(buildTemplateInput,configurationSnippetNameOder,deviceNameOrder)

        return None

    @staticmethod
    def checkInput(input):
        # TO DO
        # Detect duplicate in headers

        supported = ['interfacesCrtX4','ospfsCrtX7','prefixListsCrtX5','prefixListsCrtX6','interfaces1','interfaces2','context','ospf','prefixLists','bgp','topology','taskDescription','interfaces','asNumber','vrfName','vlanId1','vlanId2','vlanId3','hsrpId','ospfProcess','ospfArea','ospfPassword','ospfPriority','devicesNames','prefixListName1','prefixListName2','ipMasks1','ipMasks2','ipMask1','ipMask2','ipMask3','interfaceNumber1','interfaceNumber2','interfaceNumber3','interfacesNumbers1','configurationSnippetsNames']

        if Global['debug'] == 1:
            print len(supported)

        for key in input:
            if key not in supported:
                return -1
            if key == "asNumber" or key == "vlanId1" or key == "vlanId2" or key == "vlanId3" or key == "hsrpId" or key == "interfaceNumber1" or key == "interfaceNumber2" or key == "interfaceNumber3":
                if isinstance(input[key], list):
                    for element in input[key]:
                        if not isInt(element):
                            return -1
                elif isinstance(input[key], str):
                    if not isInt(input[key]):
                        return -1
            elif key == "ipMasks1" or key == "ipMasks2":
                if isinstance(input[key], list):
                    for element in input[key]:
                        if not isIpMask(element):
                            return -1
                elif isinstance(input[key], str):
                    if not isIpMask(input[key]):
                        return -1
            elif key == "ipMask1" or key == "ipMask2" or key == "ipMask3":
                if isinstance(input[key], list):
                    for element in input[key]:
                        if not isIpMask(element):
                            return -1
                elif isinstance(input[key], str):
                    if not isIpMask(input[key]):
                        return -1
            elif key == "ospfArea":
                if not isOspfArea(input[key]):
                    return -1
            elif key == "devicesNames":
                if len(input[key]) != 2 and len(input[key]) != 4:
                    return -1

        return 0
