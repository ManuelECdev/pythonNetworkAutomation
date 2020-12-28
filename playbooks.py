from plays import *


playbook_config_newVrf_fp = { "validatePlays": [ play_validate_newVrf_fp ], "playGroups": [ [ play_val_newVrf_fp, play_configBuild_newVrf_fp ] ] }

playbook_config_newOspfL3Out_dsFw_fp = { "validatePlays": [ play_validate_newOspfL3Out_dsFw_fp ], "playGroups": [ [ play_configBuild_newInterfaceLoopback_fp, play_configBuild_newOspf_fp, play_configBuild_newInterfaceVlanXferFw_fp ] ] }

playbood_config_newNetwork_fp = { "validatePlays": [ play_val_newNetwork_fp ], "playGroups":  [ [ play_configBuild_newNetwork_fp ] ] }


def getPlaybook(playbookName):
        
    switcher = {
        "config_newVrf_fp": playbook_config_newVrf_fp,
        "config_newOspfL3Out_dsFw_fp": playbook_config_newOspfL3Out_dsFw_fp,
        "config_newNetwork_fp": playbood_config_newNetwork_fp,
    }
        
    return switcher.get(playbookName, None )
    
def runPlaybook(playbook,inputPlaybook, GroupVar):
	
	for validatePlay in playbook['validatePlays']:
		for role in validatePlay['roles']:
			role['task'](role,inputPlaybook)
			
	for playGroup in playbook['playGroups']:
	    for play in playGroup:
	        for hostName in inputPlaybook['hostslist']:
	            for role in play['roles']:
	               role['task'](hostName,inputPlaybook,GroupVar)