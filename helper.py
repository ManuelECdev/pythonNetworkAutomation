#!/usr/bin/env python
""" jinja2-nxos-config

    Accepts arguments from YAML config file
    and generates a Jinja2 configuration
	import yaml
"""

#TODO: Consider use of the leading underscore
#from ucstools import storage
#from jinja2 import Environment, FileSystemLoader
import jinja2
from ipaddress import *
import re
import yaml


loader=  FileSystemLoader(".")

ENV = Environment(loader=loader)

def get_config(configfile):
    """Pulls YAML configuration from file and returns dict object"""
    with open(configfile) as _:
        return yaml.load(_)

def gen_snippet(snippet, config):
    """Renders a config snippet.
    "config" represents the portion of the YAML
    file applicable to this snippet"""

    template = ENV.get_template('/snippets/configuration/' + snippet + ".j2")
    return template.render(config)
    
def supportedInputKeys(inputKeys, supportedInputKeys):

	for inputKey in inputKeys:

		try:
			supportedInputKeys.index(inputKey)
		except ValueError:
			return -1

	return 1
	
def buildIpAddress(subnet,deviceNameOrder,ipOffset ):
    return str( ipaddress.ip_network(subnet).network_address + deviceNameOrder + ipOffset )
    
def buildPrefixlen(subnet):
    return str( ipaddress.ip_network(subnet).prefixlen )

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def isOspfArea(str):

	if not isInt(str):
		splitedOspfArea = str.split(".")
		if len(splitedOspfArea) == 4:
			for OspfAreaBits in splitedOspfArea:
				if not isInt(OspfAreaBits):
					return False
		else:
			return False

	return True

def isSubnet(str):
	try:
		ip_network(str)
		return True
	except (AddressValueError, NetmaskValueError):
		return False
	except ValueError:
		return False
	
