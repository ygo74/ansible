# Ansible Code quality

## Ansible lint
| Site | Link |
|------|------|
| Ansible style guide | https://docs.ansible.com/ansible-lint/ |
| Github ansible-lint | https://github.com/ansible/ansible-lint |
| Open Contrail Infra | http://logs.tungsten.io/static/infra-doc/rfc/ansible-style-guide.html | Whitecloud Ansible style | https://github.com/whitecloud/ansible-styleguide |


### Installation
```bash
# Install version 4.1.0 used in the current venv
pip install ansible-lint==4.1.0
```

### Usage

Default rules are in : lib/python2.7/site-packages/ansiblelint/rules

| Goal | Command |
|------|------|
| Seel all rules | ansible-lint -L |
| lint a role | ansible-lint windows_features -v |



