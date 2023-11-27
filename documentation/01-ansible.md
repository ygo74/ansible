# Ansible

# Install Ansible

## Install ansible from scratch

python3 -m venv ansible_2.10_p36
source ansible_2.10_p36/bin/activate
pip install wheel
pip install --upgrade pip
pip install 'ansible'


## Install ansible from requirements

python3 -m venv ansible_2.10_p36
source ansible_2.10_p36/bin/activate
pip install wheel
pip install --upgrade pip
pip install -r ansible_venvs/ansible_2.10_p36.txt


## Ansible Collections

ansible-galaxy collection install community.general

