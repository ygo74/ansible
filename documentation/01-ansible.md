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



## Ansible rulebook

<https://ansible.readthedocs.io/projects/rulebook/en/stable/installation.html>

1. Java prerequisites

    sudo apt install -y openjdk-17-jre
    export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
    export PATH=$PATH:~/.local/bin

1. install rulebook

    pip3 install ansible ansible-rulebook ansible-runner

1. Check usage

    ansible-rulebook --version

1. Collections

    <https://github.com/ansible/event-driven-ansible/tree/main>

    ``` bash
    ansible-galaxy collection install ansible.eda

    # requires to systemd-python packages
    sudo apt-get install pkg-config
    sudo apt-get install libsystemd-dev
    sudo apt-get install python3-dev

    # install requirements
    pip install -r https://raw.githubusercontent.com/ansible/event-driven-ansible/main/requirements.txt ---> Error

    ```

