Ansible Role: SSH
=========
Configure SSH Key

![GitHub Workflow Status](https://img.shields.io/github/workflow/status/kilip/ansible-role-ssh/CI?style=flat-square)

Requirements
------------
None.

Role Variables
--------------
```yaml
ssh_key_user: "root"
ssh_key_type: rsa
ssh_key_size: 4096
ssh_key_dir: "/home/{{ ssh_key_user }}/.ssh"
ssh_key_filename: "id_rsa"
ssh_key_passphrase: ""
ssh_key_force: false
```

Dependencies
------------
None.

Example Playbook
----------------
Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: all
      roles:
         - role: kilip.ssh

License
-------

MIT

Author Information
------------------
This role was created in 2022 by [Anthonius Munthi](https://itstoni.com)

