
## Sample Ansible Playbook for Cisco IOS Discovery ##

The playbooks contained within this repository are examples only.  They are intended to illustrate some basic usage as well as the evolution of a playbook from:
- an initial playbook with embedded credentials suitable for a lab environment
- a playbook more suitable for a production environment which uses constructs which anticipate the structured data returned and how it might be used at a later time
- a playbook more suitable for a production environment which uses Ansible Vault to protect credentials (Note: this is an interactive playbook)
- a playbook more suitable for a production environment which ensures structured data, uses Ansible Vault, and modularizes the list of show commands so that a simple YAML text file containing the desired show commands to run against each target can be modified rather than modifying the playbook itself. This approach allows the playbook to be locked down while allowing flexibility in the payload to send to the target.  This playbook also introduces "ignore_errors" which should be used carefully.
- an interactive playbook to showcase including credentials as part of the command line and limiting the target hosts

These playbooks execute a set of show commands on the designated group and save the output to a file.

Note:  This is a working repository and so some playbooks may still be a work in progress.

