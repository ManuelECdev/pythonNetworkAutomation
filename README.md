## Project summary

The project's scope is to automatize the development of configurations for Routers and Switches.
This version automatize the development of configurations in a Fabricpath deployment with Cisco Nexus devices:

* New vrf creation
* New subnet creation.
* New ospf configurarion and a L3out towards a Firewall.

## Files

Ansible network Automation.pdf:
This is the target architecture to automate the development of configurations.

tests.py:
Automated tests done in circleci CI/CD pipeline.

inputTemplates
Templates for the input variables for each configuration.


## How to install it.

You can have a look at .circleci/config.yml. In this file it is automated the process of installing the package in a linux VM.

## How to run it.

Please have a look at the foler Examples. There are 4 examples available.

* Create a new vrf:

make circleCiExample1

* Configure ospf and L3out towards a FW:

make circleCiExample2

* Configure a new subnet:

make circleCiExample3



