#!/usr/bin/env bash

echo not to be executed as script
sleep 60000

# asdf language runtime version manager like sdk, but for many programming languages
brew install asdf
# steps to hook asdf to bash shell
# UPDATE: these steps are outdated, refer https://asdf-vm.com/guide/getting-started.html for up to date commands
echo -e "\n. \"$(brew --prefix asdf)/libexec/asdf.sh\"" >> ~/.bashrc
echo -e "\n. \"$(brew --prefix asdf)/etc/bash_completion.d/asdf.bash\"" >> ~/.bashrc

# reference (some commands are outdated) - https://dev.to/frost/how-i-set-up-my-python-projects-using-asdf-and-direnv-4o67
asdf plugin-add python
asdf plugin-add direnv
# use direnv installed in the system
# as mentioned in https://github.com/asdf-community/asdf-direnv
asdf direnv setup --shell bash --version system
# asdf python plugin uses python-build plugin of "pyenv" under the hood, so need to install dependencies of pyenv for this plugin
# reference - https://github.com/asdf-community/asdf-python and https://github.com/pyenv/pyenv/wiki#suggested-build-environment
dnf install make gcc patch zlib-devel bzip2 bzip2-devel readline-devel sqlite sqlite-devel openssl-devel tk-devel libffi-devel xz-devel libuuid-devel gdbm-libs libnsl2 
# list available python versions
asdf list all python
# use system python by default
asdf global python system
cat ~/.tool-versions 
# output: python system
# list latest stable version
asdf latest python
# latest version was 3.12.3 as of May 2024
# install python
asdf install python $(asdf latest python)
# or use below command if code written is not working
asdf install python 3.12.3
# Update one day later - had to use a lower version to avoid package mixup with system python
# not sure if this fixed the problem as system python was still in version 3.12.2
# asdf install python 3.12.2
# asdf uninstall python 3.12.2
asdf install python 3.11.9
# list installed version and confirm
asdf list python
# output: 
# 3.12.1
# 3.12.3
cd ~/MyFiles/Personal/learning/python/
asdf local python 3.11.9
cat .tool-versions
# output: python 3.11.9
which python
# output: ~/.asdf/shims/python
python --version
# output: Python 3.11.9
which pip
# output: ~/.asdf/shims/pip
pip --version
# output: pip 24.0 from /home/mbhatb/.asdf/installs/python/3.11.9/lib/python3.11/site-packages/pip (python 3.11)
# for using jupyter notebook
pip install ipykernel -U --user

# executed for system python, in /tmp directory
asdf which pip
# output: /home/mbhatb/.local/bin/pip

# In another shell with global asdf python, I had to reinstall csvkit after installing asdf
# install csvkit command line python tool
# python -m ensurepip --upgrade
# python -m pip install --upgrade pip
# pip3.11 install csvkit
# UPDATE: it seems like it is better to install csvkit via brew, otherwise package will get lost when brew python is upgraded
# execute on a global python shell
python -m pip install pip3-autoremove
pip3-autoremove csvkit
brew install csvkit
# cleanup csvkit installed in asdf local python version
cd ~/MyFiles/Personal/learning/python/
python -m pip install pip3-autoremove
~/.asdf/shims/pip3-autoremove csvkit
