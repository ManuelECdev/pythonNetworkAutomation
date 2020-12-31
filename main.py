#/usr/bin/env python
import sys
from helper import *
from playbooks import *
from group_vars import *

def run():

    #
    #
    #Variable initialization
    #
    #
    
    yamlFileName = ""
    input = {}

    #
    #
    # Check the input arguments.
    #

    try:

        argslen = len(sys.argv)
        
        if argslen > 1:
            index = 1
            for index in range(argslen):

                if sys.argv[index] == "-yaml":

                    if index == argslen -1:
                        print ("Error in the arguments. Usage: -yaml <inputFile>")
                        sys.exit()
                    else:
                        yamlFileName = sys.argv[index + 1]

    except IndexError:
        print ("An error happened, exiting ... ")
        sys.exit()

    #
    #
    # Read the input data
    #
    #
    
    try:
        input = get_config(yamlFileName)
    except IOError:
        print('No such file or directory, exiting ...')
        sys.exit()
    except yaml.scanner.ScannerError:
        print('Malformed input, exiting ...')
        sys.exit()

        
    #
    #
    # Extract playbooks from input
    #
    #        
    
    inputPlaybooks = input
    if 'playbooks' in inputPlaybooks:
        inputPlaybooks = input['playbooks']
    else:
        print ("Error: playbooks key not provided in input file")
        sys.exit()

    #
    #
    #Process the lines
    #
    #
    
    renderedPlaybooks = []
    
    for inputPlaybook in inputPlaybooks:
        if 'playbookName' in inputPlaybook:
            playbook = getPlaybook(inputPlaybook['playbookName'])
            if playbook:
                renderedPlaybooks.append(runPlaybook(playbook, inputPlaybook, hostName2GroupVar))
            else:
                print ("Error: playbookName value not valid, exiting ...")
                sys.exit()
        else:
            print ("Error: playbookName key not provided in playbook input, exiting ...")
            sys.exit()
    #
    #
    #Process the output
    #
    #
    
    for renderedPlaybook in renderedPlaybooks:
        for renderedTask in renderedPlaybook:
            if renderedTask['printHostName']:
                print(printHostName(renderedTask['hostName']))
            
            print(renderedTask['renderedSnippet'] + "\n")
        
        
if __name__ == "__main__":
    run()
