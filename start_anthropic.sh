#!/bin/bash

# use env variable so it only asks once
# use subshell so it cleans up automatically and never exposes the pass
read -s -p "Sudo password: " PASS
echo
(
  export ANSIBLE_BECOME_PASS="$PASS"
  ansible-playbook ./playbooks/scraper.yml
)
