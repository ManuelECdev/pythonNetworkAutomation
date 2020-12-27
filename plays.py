
from roles import *

play_configBuild_newInterfaceLoopback_fp = {
    "description": "new loopbak interface configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newInterfaceLoopback_fp }]
}

play_configBuild_newInterfaceVlanXferFw_fp = {
    "description": "new xfer interface configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newInterfaceVlanXferFw_fp } ]
}

play_configBuild_newNetwork_fp = {
    "description": "new server network Configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newNetwork_fp } ]
}

play_configBuild_newOspf_fp = {
    "description": "new ospf configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newOspf_fp }]
}    

play_configBuild_newOspfL3Out_dsFw_fp = {
    "description": "merge configurations into one file - build",
    "roles": [ { "role": role_configBuild_newOspfL3Out_dsFw_fp } ]
}

play_configBuild_newVrf_fp = {
    "description": "new vrf Configuration - build",
    "roles": [ { "role": role_configBuild_newVrf_fp } ]
}

play_val_newNetwork_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ { "role": role_validate_hostslist }, { "role": role_validate_vrfName }, { "role": role_validate_vlanId }, { "role": role_validate_hsrpGroup }, { "role": role_validate_ipNetwork }, { "role": role_validate_ospfArea }, { "role": role_validate_ospfProcess }, { "role": role_validate_idNumber } ]
}

play_val_newOspfL3Out_dsFw_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ {"role": role_validate_hostslist }, {"role": role_validate_vrfName }, {"role": role_validate_vlanId }, {"role": role_validate_ipNetwork, "inputVar": "ipNetworkXfer" }, {"role": role_validate_ipNetwork, "inputVar": "ipNetworkLoopBack"}, {"role": role_validate_ospfArea }, {"role": role_validate_ospfProcess }, {"role": role_validate_idNumber }, {"role": role_validate_interfaceLoopBackNumber } ]
}   

play_val_newVrf_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ {"role": role_validate_hostslist }, {"role": role_validate_vrfName }, {"role": role_validate_idNumber } ]
}      