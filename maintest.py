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
#from templatesv1 import *
from templates import *


def run():

    #
    #
    #Variable initialization
    #
    #
    fileName = ""
    IdName = ""
    debug = 0
    headersCheck = 0
    output_from_parsed_template = ""
    templateindex = 0
    deviceindex = 0
    templateArray = []

    print 'hello'

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
                        configfile = 'INC.yaml'
                        yaml = get_config(configfile)
                        print yaml

                elif sys.argv[index] == "-d":
                    debug = 1

    except IndexError:
        print "A bug happened, It will be fixed asap... exiting"
        sys.exit()


run()



# Task: 3 - ANY ( server network )
# Local Input Larameters Assistant

#########################
#
# ospfProcess
#
# Suggested values
#
# if vrfname == MNG
#   ospfProcess = oam
# else
#   ospfProcess = service
#

- task:
    SetTasks: 3 - ANY ( server network )
    vrfName: MNG-MNG-M1-IA-02
    ospfArea: 0.6.5.2
    vlanId2: 2147
    hsrpId: 3156
    ospfProcess: oam
    ipMask1: 10.179.143.0/24
    devicesNames:
      - de1dsw241ego-1
      - de1dsw241ego-2
      #- de1dsw26903n-1
      #- de1dsw26903n-2
    configurationSnippetsNames :
      - dswX
