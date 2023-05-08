#!/usr/bin/env bash

#upgrade pyhton pip
python3 -m pip install --upgrade pip

# Uninstall Fabric
pip3 uninstall -y Fabric

# Install dependencies
sudo apt-get install -y libffi-dev
sudo apt-get install -y libssl-dev
sudo apt-get install -y build-essential
sudo apt-get install -y python3.4-dev
sudo apt-get install -y libpython3-dev

# Install Python packages
pip3 install pyparsing
pip3 install appdirs
pip3 install setuptools==40.1.0
pip3 install cryptography==2.8
pip3 install bcrypt==3.1.7
pip3 install PyNaCl==1.3.0
pip3 install Fabric3==1.14.post1
