#!/usr/bin/env bash

echo "Not to be executed as a script"; sleep 999999;

# New python project using venv and asdf version manager

asdf install python 3.12.7

# youtube-playlist-download is project name
_PROJECT_FOLDER_NAME="youtube-playlist-download"
cd ${HOME}/MyFiles/Personal/learning/
mkdir -p "${_PROJECT_FOLDER_NAME}"
cd "${_PROJECT_FOLDER_NAME}"
python -m venv .venv

# create .envrc file in the project directory and paste below uncommented lines

# .envrc BEGIN
# Python · direnv/direnv Wiki
# https://github.com/direnv/direnv/wiki/Python
# seems to create python executable under .direnv directory inside the current directory, which we don't really want while using asdf
# UPDATE: exporting VIRTUAL_ENV variable fixes this
export VIRTUAL_ENV=."venv"
layout python

# just sourcing activate script also seems to work
#source ./.venv/bin/activate

# .envrc END

echo ".venv" > .gitignore
# .env file is used by python dotenv library, uncomment if using that
#echo ".env" >> .gitignore
echo ".envrc" >> .gitignore