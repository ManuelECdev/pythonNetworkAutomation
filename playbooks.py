from plays import *


playbook_config_newVrf_fp = { "plays": [ play_val_newVrf_fp, configBuild_newVrf_fp ] }

playbook_config_newOspfL3Out_dsFw_fp = { "plays": [ val_newOspfL3Out_dsFw_fp, configBuild_newInterfaceLoopback_fp, configBuild_newOspf_fp, configBuild_newInterfaceVlanXferFw_fp, configBuild_newOspfL3Out_dsFw_fp ] }

playbood_config_newNetwork_fp = { "plays": [val_newNetwork_fp, configBuild_newNetwork_fp] }