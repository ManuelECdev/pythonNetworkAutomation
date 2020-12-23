from helper import *

class newVrf:

    def __init__(self, vrfName):
        self.vrfName = vrfName

def task_buildConfig_newVrf_fp(playbook,role, hostName,inputPlaybook):
     
    rendered_buildConfig = {
        "hostName": hostName,
        "renderedSnippet": None
    }
    
    newVrfObject = newVrf(inputPlaybook['vrfName'])
    
    rendered_buildConfig['renderedSnippet']  = gen_snippet('snippet7', newVrfObject.__dict__)
    
    return rendered_buildConfig
    