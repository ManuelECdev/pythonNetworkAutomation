#!/usr/bin/env python
""" jinja2-nxos-config

    Accepts arguments from YAML config file
    and generates a Jinja2 configuration
	import yaml
"""

#TODO: Consider use of the leading underscore
#from ucstools import storage
from jinja2 import Environment, FileSystemLoader
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

def stringToArrayOfString(string,debug,split):

	arrayofString = []

	if debug == 1:
		print type(string)
		print string

	for splitedstring in string.split(split):
		if debug == 1:
			print splitedstring
			print type(splitedstring)

		arrayofString.append(splitedstring)

	if debug == 1:
		print arrayofString

	return arrayofString

def stringToArrayOfJSON(string,debug):

	arrayofJson = []

	if debug == 1:
		print type(string)
		print string

	for jsonstring in string.split('-'):
		if debug == 1:
			print jsonstring
			print type(jsonstring)

		arrayofJson.append(ast.literal_eval(jsonstring))

	if debug == 1:
		print arrayofJson

	return arrayofJson

def parseHeaders(headers,debug):

	# TO DO
	# Detect duplicate in headers

	supported = ['vrfName','ospfArea','VlanId1','VlanId2','InterfaceNumber','hsrpId','hsrpVip','deviceName','IpMasks','ospfProcess','IpMasks1','IpMasks2','hsrpPriority','template','VlanId3','asNumber','IpMasks3','IpMasks4','prefixListName','ospfPassword']


	if debug == 1:
		print len(headers)
		print len(supported)

	if len(headers) != 18:
		return -1

	for header in headers:

		try:
			supported.index(header)
		except ValueError:
			return -1


	return 0

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

def isIpMask(str):
	try:
		ip_network(str)
		return True
	except (AddressValueError, NetmaskValueError):
		return False
	except ValueError:
		return False
		
def task
