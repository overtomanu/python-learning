#!/usr/bin/env bash

echo not to be executed as script
sleep 60000

# reference:
# Python Virtual Environment and pip for Beginners - YouTube
# https://www.youtube.com/watch?v=eDe-z2Qy9x4

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