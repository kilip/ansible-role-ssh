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
ssh_key_group: "{{ ssh_key_user }}"
ssh_key_filename: "id_rsa"
ssh_key_type: rsa
ssh_key_size: 4096
ssh_key_dir: "/home/{{ ssh_key_user }}/.ssh"
ssh_key_passphrase: ""
ssh_key_force: false
ssh_backup_dir: "files/ssh-keys/"

# github_token values required to upload ssh key to github
github_username: "test"
github_token: ""
github_key_title: "Ansible Uploaded Key"
github_public_key_src: "{{ ssh_key_dir }}/id_rsa.pub"
github_temp_dir: "/tmp/github"
github_key_url: "https://api.github.com/user/keys"
github_list_keys: "{{ github_temp_dir }}/keys.json"
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

