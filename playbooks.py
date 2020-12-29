from plays import *


playbook_config_newVrf_fp = { "validatePlays": [ play_validate_newVrf_fp ], "playGroups": [ [ { "play": play_configBuild_newVrf_fp, "printHostName": True } ] ] }

playbook_config_newOspfL3Out_dsFw_fp = { "validatePlays": [ play_validate_newOspfL3Out_dsFw_fp ], "playGroups": [ [ { "play": play_configBuild_newInterfaceLoopback_fp, "printHostName": True }, { "play": play_configBuild_newOspf_fp, "printHostName": False }, { "play": play_configBuild_newInterfaceVlanXferFw_fp, "printHostName": False } ] ] }

playbood_config_newNetwork_fp = { "validatePlays": [ play_validate_newNetwork_fp ], "playGroups":  [ [ play_configBuild_newNetwork_fp ] ] }


def getPlaybook(playbookName):
        
    switcher = {
        "config_newVrf_fp": playbook_config_newVrf_fp,
        "config_newOspfL3Out_dsFw_fp": playbook_config_newOspfL3Out_dsFw_fp,
        "config_newNetwork_fp": playbood_config_newNetwork_fp,
    }
        
    return switcher.get(playbookName, None )
    
def runPlaybook(playbook,inputPlaybook, GroupVar):
	
	renderedTasks = [] 
	
	for validatePlay in playbook['validatePlays']:
		for role in validatePlay['roles']:
			role['role']['task']['name'](role,inputPlaybook)
	
	for playGroup in playbook['playGroups']:
		for hostName in inputPlaybook['hostslist']:
			for play in playGroup:
				for role in play['play']['roles']:
					renderedTasks.append(role['role']['task']['task'](play['printHostName'],hostName,inputPlaybook,GroupVar))
					
	return renderedTasks