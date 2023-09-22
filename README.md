Ansible Role: ssh
=========
Ansible role ssh

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/kilip/ansible-role-ssh/.github/workflows/testing.yml?branch=main&style=flat-square)](https://github.com/kilip/ansible-role-ssh/actions/workflows/testing.yml)
[![GitHub release (latest SemVer)](https://img.shields.io/github/v/release/kilip/ansible-role-ssh?style=flat-square)](https://github.com/kilip/ansible-role-ssh/releases)
[![GitHub](https://img.shields.io/github/license/kilip/ansible-role-ssh?style=flat-square)](https://github.com/kilip/ansible-role-ssh/blob/main/LICENSE)

Role Variables
--------------
Here's role variables with default values:
```yaml
ssh_user: "" # required and must be set
ssh_user_group: "{{ ssh_user }}"
ssh_dir: "/home/{{ ssh_user }}/.ssh"
ssh_private_key: "ssh/id_rsa"
ssh_public_key: "{{ ssh_private_key }}.pub"
```

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: ssh }

License
-------

MIT

Author Information
------------------

This role was created in 2023 by [Anthonius Munthi](https://itstoni.com).
