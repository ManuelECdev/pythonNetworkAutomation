from tasks import *

#- include_task:
#    file: /etc/ansible/tasks/common/commonTasks_buildConfigFromTemplate.yml

role_configBuild_newInterfaceLoopback_fp = {
    "description": "build snippet for newInterfaceLoopback",
    "task": task_commonTasks_buildConfigFromTemplate
    
}

#- include_task:
#    file: /etc/ansible/tasks/common/commonTasks_buildConfigFromTemplate.yml

role_configBuild_newInterfaceVlanXferFw_fp = {
    "description": "build snippet for newInterfaceVlanXferFw",
    "task": task_commonTasks_buildConfigFromTemplate
}

#- include_task:
#    file: /etc/ansible/tasks/common/commonTasks_buildConfigFromTemplate.yml

role_configBuild_newNetwork_fp = {
    "description": "build snippet for newNetwork",
    "task": task_commonTasks_buildConfigFromTemplate
}

#- include_task:
#    file: /etc/ansible/tasks/common/commonTasks_buildConfigFromTemplate.yml

role_configBuild_newOspf_fp = {
    "description": "newOspf",
    "task": task_commonTasks_buildConfigFromTemplate
}

#- name: merge configuration files into one
#  command: mergeConfigs
    
role_configBuild_newOspfL3Out_dsFw_fp = {
    "description": "merge configuration files into one",
    "task": task_commonTasks_buildConfigFromTemplate
}

#- name: merge configuration files into one
#  command: mergeConfigs
    
role_configBuild_newVrf_fp = {
    "description":  "build snippet for newVrf",
    "task": task_commonTasks_buildConfigFromTemplate
}


#· name: fail if hostslist is not defined, if it is defined and blank or not a list
#  command: validate_hostslist
 
  
role_validate_hostslist = {
    "description":  "validate  hostslist",
    "task": task_validate_hostslist
}

role_validate_hsrpGroup = {
    "description":  "validate  hsrpGroup",
    "task": task_validate_hsrpGroup
}

role_validate_idNumber = {
    "description":  "validate  idNumber",
    "task": task_validate_idNumber
}

role_validate_interfaceLoopBackNumber = {
    "description":  "validate  interfaceLoopBackNumber",
    "task": task_validate_interfaceLoopBackNumber
}

role_validate_ipNetwork = {
    "description":  "validate ipNetwork",
    "task": task_validate_ipNetwork
}

role_validate_ospfArea = {
    "description":  "validate ospfArea",
    "task": task_validate_ospfArea
}

role_validate_ospfProcess = {
    "description":  "validate ospfProcess",
    "task": task_validate_ospfProcess
}

role_validate_vlanId = {
    "description":  "validate vlanId",
    "task": task_validate_vlanId
}

role_validate_vrfName = {
    "description":  "validate vrfName",
    "task": task_validate_vrfName
}