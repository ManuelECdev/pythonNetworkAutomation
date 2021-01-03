import pytest
from helper import *
from group_vars import *
from tasks import *
from group_vars import *
from playbooks import *

def tests():
    
    ############## helper.py ################
    
    assert buildIpAddress('192.168.0.0/24',1 ) == '192.168.0.1'
    assert buildIpAddress('192.168.0.0/24',5 ) == '192.168.0.5'
    
    assert buildPrefixlen('192.168.0.0/24') == '24'
    assert buildPrefixlen('192.168.0.0/26') == '26'
    
    assert isInt('3') == True
    assert isInt('t') == False
    
    assert isOspfArea('0.256.0.0') == True
    assert isOspfArea('0.16.0.0') == True
    assert isOspfArea('0.0.0.1') == True
    assert isOspfArea('0.df.0.1') == False
    
    assert isSubnet('192.168.0.0/24') == True
    assert isSubnet('192.168.0.1/24') == False
    
    assert printHostName('fpDs-1') == "################### fpDs-1 ###################\n"
    assert printHostName('fpDs-2') == "################### fpDs-2 ###################\n"
    
    ############## tasks.py ################
    
    inputPlaybook1 = { "playbookName": "config_newVrf_fp", "idNumber": "idNumber1", "vrfName": "MNG-MNG-M1-IA-02", "hostslist": ["fpDs-1", "fpDs-2"] }
    assert task_buildConfig_newVrf_fp_function(True,"fpDs-1",inputPlaybook1,hostName2GroupVar) == { "hostName": "fpDs-1", "renderedSnippet": "\nvrf context MNG-MNG-M1-IA-02", "printHostName": True }
    
    inputPlaybook2 = { "playbookName": "config_newOspfL3Out_dsFw_fp", "idNumber": "idNumber1", "vrfName": "MNG-MNG-M1-IA-02", "ipNetworkXfer": "192.168.0.0/24", "ipNetworkLoopBack": "192.168.1.0/24","ospfProcess": "service", "ospfArea": "0.0.0.1","interfaceLoopbackNumber": "201", "vlanId": "2001", "hostslist": ["fpDs-1", "fpDs-2"] }
    assert task_buildConfig_newInterfaceVlanXferFw_fp_function(True,"fpDs-1",inputPlaybook2,hostName2GroupVar) == { "hostName": "fpDs-1", "renderedSnippet": "\ninterface Vlan2001\n description xfer_Fw\n vrf member MNG-MNG-M1-IA-02\n ip address 192.168.0.2/24\n no ip redirects\n ip ospf authentication message-digest\n ip ospf message-digest-key 1 md5 2001MNG-\n no ip ospf passive-interface\n ip router ospf service area 0.0.0.1\n no shutdown", "printHostName": True }
    
    assert task_buildConfig_newInterfaceLoopback_fp_function(True,"fpDs-1",inputPlaybook2,hostName2GroupVar) == { "hostName": "fpDs-1", "renderedSnippet": "\ninterface Loopback201\n  vrf member MNG-MNG-M1-IA-02\n  ip address 192.168.1.1/32\n  ip router ospf service area 0.0.0.1", "printHostName": True }
    
    assert task_buildConfig_newOspf_fp_function(True,"fpDs-1",inputPlaybook2,hostName2GroupVar) == { "hostName": "fpDs-1", "renderedSnippet": "\nrouter ospf service\n vrf MNG-MNG-M1-IA-02\n   router-id 192.168.1.1\n   auto-cost reference-bandwidth 100000\n   area 0.0.0.1 nssa\n   log-adjacency-changes\n   passive-interface default", "printHostName": True }
    
    inputPlaybook3 = { "playbookName": "config_newNetwork_fp", "idNumber": "idNumber1", "vrfName": "MNG-MNG-M1-IA-02", "ipNetwork": "192.168.2.0/24","ospfProcess": "service", "ospfArea": "0.0.0.1","hsrpGroup": "2010", "vlanId": "2001", "hostslist": ["fpDs-1", "fpDs-2"] }
    assert task_buildConfig_newNetwork_fp_function(True,"fpDs-1",inputPlaybook3,hostName2GroupVar) == { "hostName": "fpDs-1", "renderedSnippet": "\ninterface Vlan2001\n  description serverNetwork\n  vrf member MNG-MNG-M1-IA-02\n  no ip redirects\n  ip address 192.168.2.2/24\n  ip router ospf service area 0.0.0.1\n  hsrp version 2\n  hsrp 2010\n    authentication text vlan2001\n    preempt delay minimum 120 reload 600\n    priority 104\n    track 490 decrement 10\n    track 500 decrement 50\n    ip 192.168.2.1\n  no shutdown", "printHostName": True }
    
    assert task_validate_vrfName_function(None,{ "vrfName": "MNG-MNG-M1-IA-02"}) == 1
    assert task_validate_vrfName_function(None,{ }) == -1
    assert task_validate_vrfName_function(None,{ "vrfName": None}) == -1
    
    assert task_validate_ospfProcess_function(None,{ "ospfProcess": 1 }) == 1
    assert task_validate_ospfProcess_function(None,{ }) == -1
    assert task_validate_ospfProcess_function(None,{ "ospfProcess": None }) == -1 
    assert task_validate_ospfProcess_function(None,{ "ospfProcess": 65536 }) == -1
    
    assert task_validate_ospfArea_function(None,{ "ospfArea": "0.0.0.1" }) == 1
    assert task_validate_ospfArea_function(None,{ "ospfArea": "0.0.0.e" }) == -1
    assert task_validate_ospfArea_function(None,{ "ospfArea": None }) == -1
    assert task_validate_ospfArea_function(None,{ }) == -1
    
    assert task_validate_ipNetwork_function({"inputVar": "ipNetwork"},{ "ipNetwork": "192.168.0.0/24" }) == 1
    assert task_validate_ipNetwork_function({"inputVar": "ipNetwork"},{ "ipNetwork": "192.168.0.2/24" }) == -1
    assert task_validate_ipNetwork_function({"inputVar": "ipNetwork"},{ "ipNetwork": None }) == -1
    assert task_validate_ipNetwork_function({"inputVar": "ipNetwork"},{  }) == -1
    
    assert task_validate_interfaceLoopBackNumber_function(None,{ "interfaceLoopbackNumber": 1024 }) == -1
    assert task_validate_interfaceLoopBackNumber_function(None,{ "interfaceLoopbackNumber": None }) == -1
    assert task_validate_interfaceLoopBackNumber_function(None,{ }) == -1
    assert task_validate_interfaceLoopBackNumber_function(None,{ "interfaceLoopbackNumber": 1000 }) == 1

    assert task_validate_idNumber_function(None,{ "idNumber": "idnumber100000000000000" }) == -1
    assert task_validate_idNumber_function(None,{ "idNumber": None }) == -1
    assert task_validate_idNumber_function(None,{ }) == -1
    assert task_validate_idNumber_function(None,{ "idNumber": "idnumber1" }) == 1
    
    assert task_validate_hsrpGroup_function(None,{ "hsrpGroup": 4096 }) == -1
    assert task_validate_hsrpGroup_function(None,{ "hsrpGroup": None }) == -1
    assert task_validate_hsrpGroup_function(None,{ }) == -1
    assert task_validate_hsrpGroup_function(None,{ "hsrpGroup": 4000 }) == 1

    assert task_validate_hostslist_function(None,{ "hostslist": ["fpDs-1", "fpDs-3"] }) == -1
    assert task_validate_hostslist_function(None,{ "hostslist": None }) == -1
    assert task_validate_hostslist_function(None,{ }) == -1
    assert task_validate_hostslist_function(None,{ "hostslist": ["fpDs-1", "fpDs-2"] }) == 1    
    
    ############## group_vars.py ################
    
    assert buildOspfPassword("2011", "MNG-MNG-M1-IA-02") == "2011MNG-"
    assert buildOspfPassword("2031", "MNG-M1") == "2031MNG-"
    assert buildOspfPassword("2041", "MNG1-M1") == "2041MNG1"
    
    assert buildRouterId("192.168.0.0/24",1) == "192.168.0.1"
    assert buildRouterId("192.168.1.0/24",2) == "192.168.1.2"
    assert buildRouterId("192.168.2.0/24",3) == "192.168.2.3"
    
    assert buildHsrpAuth("2001") == "2001"
    assert buildHsrpAuth("2002") == "2002"
    assert buildHsrpAuth("2003") == "2003"
    
    assert buildHsrpVip("192.168.2.0/24",1) == "192.168.2.1"
    assert buildHsrpVip("192.168.3.0/24",1) == "192.168.3.1"
    assert buildHsrpVip("192.168.4.0/24",1) == "192.168.4.1"
    assert buildHsrpVip("192.168.5.0/24",1) == "192.168.5.1"
    
    ############## playbooks ################
    
    assert getPlaybook("config_newVrf_fp") == playbook_config_newVrf_fp
    assert getPlaybook("config_newOspfL3Out_dsFw_fp") == playbook_config_newOspfL3Out_dsFw_fp
    assert getPlaybook("config_newNetwork_fp") == playbood_config_newNetwork_fp
    assert getPlaybook("test") == None
    
    