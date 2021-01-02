SHELL := /bin/bash
## The Makefile includes instructions on environment setup and lint tests
# Create and activate a virtual environment
# Install dependencies in requirements.txt

localeExample1:
	( \
		source ~/pythonNetworkAutomation/bin/activate; \
		python main.py -yaml  ../pythonNetworkAutomation/Examples/example1.yml; \
	) 
localeExample2:
	( \
		source ~/pythonNetworkAutomation/bin/activate; \
		python main.py -yaml  ../pythonNetworkAutomation/Examples/example2.yml; \
	) 

localeExample3:
	( \
		source ~/pythonNetworkAutomation/bin/activate; \
		python main.py -yaml  ../pythonNetworkAutomation/Examples/example3.yml; \
	)
localeExample4:
	( \
		source ~/pythonNetworkAutomation/bin/activate; \
		python main.py -yaml  ../pythonNetworkAutomation/Examples/example4.yml; \
	)  
localSetupAndInstall:
	( \
		virtualenv -p python ~/pythonNetworkAutomation; \
		source ~/pythonNetworkAutomation/bin/activate; \
		pip install -r requirements.txt; \
	)

circleCiInstall:
	# This should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt

CircleCiExample1:
	python main.py -yaml  ../pythonNetworkAutomation/Examples/example1.yml

CircleCiExample2:
	python main.py -yaml  ../pythonNetworkAutomation/Examples/example2.yml

CircleCiExample3:
	python main.py -yaml  ../pythonNetworkAutomation/Examples/example3.yml

CircleCiExample4:
	python main.py -yaml  ../pythonNetworkAutomation/Examples/example4.yml
