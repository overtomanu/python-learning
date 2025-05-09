#!/usr/bin/env bash

echo not to be executed as script
sleep 60000

# reference:
# Python Virtual Environment and pip for Beginners - YouTube
# https://www.youtube.com/watch?v=eDe-z2Qy9x4

# NOTE: if you are getting pip command not found, then just use "python -m pip"
# it is too much of trouble to setup pip for python installed by brew and get it shimmed by asdf version manager
# but if pip command is anyways needed, execute below two commands
# python3 and python can point to different interpreters because of brew or asdf setting.
# so always install module in correct python/pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip

# show available commands for pip
pip --help

# show options for a pip command
pip install --help

# list global packages
pip list

# install a specific version of a package
pip install requests==2.30.0

# install or upgrade a package, --upgrade also works
pip install -U requests

# show info and dependencies for python module "requests"
pip show requests

# library to test python code style
pip install pylint

# run pylint to get code quality report and score
# -r y for report yes
pylint myexample.py -r y

# notedown dependencies in a text file
pip freeze > requirements.txt

# uninstalling a package, below command uninstalls pip itself
python -m pip uninstall pip

# packages installed at some point of time
pip install pip3-autoremove
pip install requests
pip install python-dotenv
pip install pylint
pip install send2trash
pip install lxml
pip install bs4
# pillow and tqdm only installed in asdf python v3.11.9
pip install pillow
pip install tqdm
pip install PyPDF2
pip install imap-tools
pip install tabulate
# only installed in system python
pip install fire
pip install pexpect # requirement was already satisfied

# last time I checked, playwright was not fully supported by microsoft on fedora
pip install playwright

# Jupyter notebook related
pip install ipykernel -U --user
pip install ipywidgets
