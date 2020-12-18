#/usr/bin/env python
"""

"""

import sys
from helper import *
import re
import fileinput
import ast
import os
import ipaddress
from templates import *
from Global import *
from playbooks import *


def run():

    #
    #
    #Variable initialization
    #
    #
    fileName = ""
    IdName = ""
    yamlFileName = ""
    headersCheck = 0
    output_from_parsed_template = ""
    templateindex = 0
    deviceindex = 0
    templateArray = []
    input = {}

    #
    #
    # Check the input arguments.
    #
    #
    try:

        argslen = len(sys.argv)
        if argslen > 1:
            index = 1
            for index in range(argslen):

                if sys.argv[index] == "-f":

                    if index == argslen -1:
                        print 'Error in the arguments. Usage: -f output file, -d enable debugging'
                        sys.exit()
                    else:
                        IdName = sys.argv[index + 1]

                elif sys.argv[index] == "-d":
                    Global['debug'] = 1
                elif sys.argv[index] == "-yaml":
                    yamlFileName = sys.argv[index + 1]

    except IndexError:
        print "A bug happened, It will be fixed asap... exiting"
        sys.exit()

    #
    #
    # Read the input data
    #
    #
    if yamlFileName != "":
        input = get_config(yamlFileName)
    else:
        print 'Error: Yaml file name was not provided'
        sys.exit()
        
    if Global['debug'] == 1:
        print input

    playbooks = input
    if 'playbooks' in input:
        playbooks = input['playbooks']
    else:
        print 'Error: playbooks not provided in inputTemplate file'
        sys.exit()

    def buildSnippet(play,role,task):
        
        
        
        
        
    def runPlaybook(playbook):
        
        for play in playbook['plays']:
            for role in play['roles']:
                ##run the task
                runTask(play, role, task)        
        
    #
    #
    #Process the lines
    #
    #
    for playbook in playbooks:

        if Global['debug'] == 1:
            print playbooks
    
        runPlaybook(playbook['playbookName'])

        #
        #
        #Process the object
        #
        #

        if 'configurationSnippetsNames' in TemplateObject:

            for deviceNameOrder,deviceName in enumerate(TemplateObject['devicesNames']):

                snippetB = snippetBlock(dict(deviceName=deviceName,configurationSnippetsNames=TemplateObject['configurationSnippetsNames'],preTestSnippets=[],preVerifySnippets=[],postVerifySnippets=[],postTestSnippets=[]))

                #for configurationSnippetNameOder,snippetName in enumerate(TemplateObject['configurationSnippetsNames']):
                for configurationSnippetOder,configrationSnippet in enumerate(snippetB.configrationSnippets):

                    snippetObject =  templateHelper.buildTemplate(TemplateObject,configrationSnippet['name'],deviceNameOrder,configurationSnippetOder)

                    if snippetObject != None:
                        configrationSnippet['snippet'] = snippetObject
                        #snippetB.configrationSnippets.append(snippetObject)
                    else:
                        print 'Error in the input... no snippetObject ... exiting'
                        sys.exit()

                templateArray.append(snippetB)


    #
    #
    #Print the data
    #
    #
    for aTemplate in templateArray:

        output_from_parsed_template = ""
        templateName = ""
        output_from_parsed_template = "################### " + aTemplate.deviceName + " ###################\n\n"

        for order,snippetObject in enumerate(aTemplate.configrationSnippets):


            if order == len(aTemplate.configrationSnippets) -1:
                output_from_parsed_template = output_from_parsed_template + gen_snippet(snippetObject['name'], snippetObject['snippet'].__dict__) + "\n"
            else:
                output_from_parsed_template = output_from_parsed_template + gen_snippet(snippetObject['name'], snippetObject['snippet'].__dict__)

            if IdName != "":

                if not os.path.exists(IdName):

                    os.makedirs(IdName)

                os.chdir(IdName)

                fileName = IdName + '_' + '-'.join(aTemplate.configurationSnippetsNames) + '_' + aTemplate.deviceName

                if not os.path.isfile(fileName):
                    with open(fileName, "wb") as fh:
                        fh.write(output_from_parsed_template)
                else:
                    with open(fileName, "a") as fh:
                        fh.write(output_from_parsed_template)
                os.chdir("..")

            else:
                print output_from_parsed_template

            output_from_parsed_template = ""




if __name__ == "__main__":
    run()
