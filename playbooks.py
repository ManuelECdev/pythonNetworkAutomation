from plays import *


playbook_config_newVrf_fp = { "plays": [ play_val_newVrf_fp, play_configBuild_newVrf_fp ] }

playbook_config_newOspfL3Out_dsFw_fp = { "plays": [ play_val_newOspfL3Out_dsFw_fp, play_configBuild_newInterfaceLoopback_fp, play_configBuild_newOspf_fp, play_configBuild_newInterfaceVlanXferFw_fp, play_configBuild_newOspfL3Out_dsFw_fp ] }

playbood_config_newNetwork_fp = { "plays": [ play_val_newNetwork_fp, play_configBuild_newNetwork_fp] }