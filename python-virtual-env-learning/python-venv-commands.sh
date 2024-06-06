#!/usr/bin/env bash

# reference:
# Python Virtual Environment and pip for Beginners - YouTube
# https://www.youtube.com/watch?v=eDe-z2Qy9x4

cd ~/MyFiles/Personal/learning/python-learning/python-virtual-env-learning || exit

# create a virtual environment in current folder
# below command creates a subfolder named ".venv" to store scripts and dependencies
python -m venv .venv

# activate virtual environment, must be sourced and should not be called directly
# after executing the below command, shell prompt will have "(.venv)""
# shellcheck source=/dev/null
source ./.venv/bin/activate

# install package in the python virtual environment
pip install requests
pip install python-dotenv

echo ".venv" > .gitignore
echo ".env" >> .gitignore

# get API key from https://home.openweathermap.org/api_keys and add it to .env file
echo "API_KEY=PASTE_API_KEY_HERE_WITHOUT_ANY_QUOTES"

# in vs code/codium install "Python Environment Manager"
# to see existing virtual environments, open the parent folder of .venv in a separate vs codium workspace/window
# click on the python icon in the sidebar
# Under GLOBAL ENVIRONMENTS accordion, expand Venv and click on star icon of the first entry
# to activate the virtual environment