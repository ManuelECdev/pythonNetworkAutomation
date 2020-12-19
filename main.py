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

    ##extract playbooks from input
    inputPlaybooks = input
    if 'playbooks' in inputPlaybooks:
        inputPlaybooks = input['playbooks']
    else:
        print 'Error: playbooks not provided in inputTemplate file'
        sys.exit()

    #
    #
    #Process the lines
    #
    #
    for inputPlaybook in inputPlaybooks:

        if Global['debug'] == 1:
            print inputPlaybooks
        
        playbook = getPlaybook(inputPlaybook['playbookName'])
        if playbook:
            runPlaybook(playbook, inputPlaybook)
            
  

if __name__ == "__main__":
    run()
