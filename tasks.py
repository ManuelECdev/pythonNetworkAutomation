#- name: BUILD CONFIGS
#  buildSnippet:
#    src: "{{templateName}}.j2"
#    dest: "/etc/ansible/configs/{{idNumber}}/{{idNumber}}_{{hostname}}_{{templateName}}.cfg"

task_commonTasks_buildConfigFromTemplate = {
    "description": "BUILD CONFIGS",
    "name": "buildSnippet",
}


task_validate_vrfName = {
    "description": "validate vrfName",
    "name": "validateVrfName"
}

task_validate_vlanId = {
    "description": "validate vlanId",
    "name": "validateVlanId"
}

task_validate_ospfProcess = {
    "description": "validate ospfProcess",
    "name": "validateOspfProcess"
}

task_validate_ospfArea = {
    "description": "validate ospfArea",
    "name": "validateOspfArea"
}

role_validate_ipNetwork = {
    "description": "validate ipNetwork",
    "name": "validateIpNetwork"
}

task_validate_interfaceLoopBackNumber = {
    "description": "validate interfaceLoopBackNumber",
    "name": "validateInterfaceLoopBackNumber"
}

task_validate_idNumber = {
    "description": "validate idNumber",
    "name": "validateIdNumber"
}

task_validate_hsrpGroup = {
    "description": "validate hsrpGroup",
    "name": "validateHsrpGroup"
}

task_validate_hostslist = {
    "description": "validate hostslist",
    "name": "validateHostslist"
}