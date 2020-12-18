
from roles import *
#- name: new loopbak interface configuration in existing vrf - build
  #hosts: "{{ hostslist }}"
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #gather_facts: false
  #vars:
  #  hostname: "{{ inventory_hostname }}"
  #  templateName: 'nx-os_newInterfaceLoopBack_snippet'
 # roles:
 #  - role: configBuild_newInterfaceLoopback_fp

play_configBuild_newInterfaceLoopback_fp = {
    "description": "new loopbak interface configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newInterfaceLoopback_fp }]
}

 #- name: new xfer interface configuration in existing vrf - build
  #hosts: "{{ hostslist }}"
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #gather_facts: false
  #vars:
  #  hostname: "{{ inventory_hostname }}"
  #  templateName: 'nx-os_newInterfaceVlanXfer_snippet'
  #roles:
  # - role: configBuild_newInterfaceVlanXferFw_fp 
 
 
 
play_configBuild_newInterfaceVlanXferFw_fp = {
    "description": "new xfer interface configuration in existing vrf - build",
    "roles": [ { "role": role_configBuild_newInterfaceVlanXferFw_fp } ]
}

#- name: new server network Configuration in existing vrf - build
  #hosts: "{{ hostslist }}"
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #gather_facts: false
  #vars:
  #  hostname: "{{ inventory_hostname }}"
  #  templateName: 'nx-os_newInterface_snippet'
#  roles:
#   - role: configBuild_newNetwork_fp
 

play_configBuild_newNetwork_fp = {
    "description": "new server network Configuration in existing vrf - build",
    "roles": [ { "role":"configBuild_newNetwork_fp" } ]
}


#- name: new ospf configuration in existing vrf - build
  #hosts: "{{ hostslist }}"
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #gather_facts: false
  #vars:
  #  hostname: "{{ inventory_hostname }}"
  #  templateName: 'nx-os_newOspf_snippet'
#  roles:
#   - role: configBuild_newOspf_fp

play_configBuild_newOspf_fp = {
    "description": "new ospf configuration in existing vrf - build",
    "roles": [ { "role":"configBuild_newOspf_fp" }]
}    


#- name: merge configurations into one file - build
  #hosts: "{{ hostslist }}"
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #gather_facts: false
#  roles:
#   - role: configBuild_newOspfL3Out_dsFw_fp
   #- local_action: copy content={{ config_newInterfaceLoopback_fp + config_newOspf_fp + config_newInterfaceVlanXferFw_fp }} dest="/etc/ansible/configs/{{ idNumber }}/{{ idNumber }}_{{ inventory_hostname }}_config_newOspfL3Out_dsFw_fp.cfg"

play_configBuild_newOspfL3Out_dsFw_fp = {
    "description": "merge configurations into one file - build",
    "roles": [ { "role":"configBuild_newOspfL3Out_dsFw_fp" } ]
}

#- name: new vrf Configuration - build
  #hosts: "{{ hostslist }}"
  #gather_facts: false
  #any_errors_fatal: true
  #max_fail_percentage: 0
  #vars:
  #  hostname: "{{ hostslist | join('_') }}"
  #  templateName: 'nx-os_newVrf_snippet'
#  roles:
#   - role: configBuild_newVrf_fp

play_configBuild_newVrf_fp = {
    "description": "new vrf Configuration - build",
    "roles": [ { "role":"configBuild_newVrf_fp" } ]
}

#- name: Validate extra vars parameters
  #hosts: localhost
  #gather_facts: false
  #any_errors_fatal: true
  #max_fail_percentage: 0
#  roles:
#   - role: validate_hostslist
#   - role: validate_vrfName
#   - role: validate_vlanId
#   - role: validate_hsrpGroup
#   - role: validate_ipNetwork
#   - role: validate_ospfArea
#   - role: validate_ospfProcess   
#   - role: validate_idNumber
   
play_val_newNetwork_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ { "role":"validate_hostslist" }, { "role":"validate_vrfName" }, { "role": "validate_vlanId" }, { "role": "validate_hsrpGroup" }, { "role": "validate_ipNetwork" }, { "role":"validate_ospfArea" }, { "role": "validate_ospfProcess" }, { "role":"validate_idNumber" } ]
}

#- name: Validate extra vars parameters
  #hosts: localhost
  #gather_facts: false
  #any_errors_fatal: true
  #max_fail_percentage: 0
 # roles:
 #  - role: validate_hostslist
 #  - role: validate_vrfName
 #  - role: validate_vlanId
 #  - role: validate_ipNetwork
   #  vars:
   #    ipNetwork: "{{ ipNetworkXfer }}"
 #  - role: validate_ipNetwork
   #  vars:
   #    ipNetwork: "{{ ipNetworkLoopBack }}"
 #  - role: validate_ospfArea
 #  - role: validate_ospfProcess     
 #  - role: validate_idNumber
 #  - role: validate_interfaceLoopBackNumber
   
play_val_newOspfL3Out_dsFw_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ {"role": "validate_hostslist" }, {"role": "validate_vrfName" }, {"role": "validate_vlanId"}, {"role": "validate_ipNetwork", "inputVar": "ipNetworkXfer" }, {"role": "validate_ipNetwork", "inputVar": "ipNetworkLoopBack"}, {"role": "validate_ospfArea"}, {"role": "validate_ospfProcess"}, {"role": "validate_idNumber"}, {"role": "validate_interfaceLoopBackNumber"} ]
}   



#- name: Validate extra vars parameters
  #hosts: localhost
  #gather_facts: false
  #any_errors_fatal: true
  #max_fail_percentage: 0
#  roles:
#   - role: validate_hostslist
#   - role: validate_vrfName
#   - role: validate_idNumber
   
play_val_newVrf_fp = {
    "description": "Validate extra vars parameters",
    "roles": [ {"role": "validate_hostslist" }, {"role": "validate_vrfName" }, {"role": "validate_idNumber"} ]
}      