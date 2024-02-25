# Unit Tests with Molecule

## Information Sources
| Topic | Link |
| ----- | ---- |
Official website | https://molecule.readthedocs.io/en/latest/
Test ansible role with Molecule | https://www.digitalocean.com/community/tutorials/how-to-test-ansible-roles-with-molecule-on-ubuntu-16-04

## Molecule Installation



### Ubuntu Installation
```bash
#Ensure repositories are up-to-date
sudo apt-get update
#Install pip
sudo apt-get install -y python-pip
#Install Virtualenv python module
sudo python -m pip install virtualenv
#Create  and activate the virtual environment
python -m virtualenv my_env
source my_env/bin/activate

#Install molecule and docker using pip
pip install --upgrade setuptools
pip install --user "molecule[docker,lint]"
pip install "molecule-azure"

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt install docker-ce

pip install docker-py
```

Remark : If you are in a git repository, add my_env to .gitignore

## Usage

### Create new role
```bash
molecule init role -r ansible-apache -d docker
```

### Add to en existing role
```bash
cd roles/windows_bootstrap
molecule init scenario --role-name windows_bootstrap --driver-name docker
molecule init scenario --role-name windows_bootstrap --driver-name docker --scenario-name windows
molecule init scenario --role-name windows_features --driver-name azure --scenario-name azure
```
