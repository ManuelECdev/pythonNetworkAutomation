SHELL := /bin/bash
## The Makefile includes instructions on environment setup and lint tests
# Create and activate a virtual environment
# Install dependencies in requirements.txt
# (Optional) Build a simple integration test

example1:
	( \
		source ~/pythonNetworkAutomation/bin/activate; \
		python main.py -yaml  ../pythonNetworkAutomation/Examples/example1.yml; \
	) 

localSetupAndInstall:
	( \
		virtualenv -p python ~/pythonNetworkAutomation; \
		source ~/pythonNetworkAutomation/bin/activate; \
		pip install -r requirements.txt; \
	)
