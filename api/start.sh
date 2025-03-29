#!/bin/bash 

if [[ "$ENVIRONMENT" == "production" ]]; then
  read -rsp "[API] Sudo password to setup Systemd service: " PASS
  echo
  (
    export ANSIBLE_BECOME_PASS="$PASS"
    ansible-playbook ../playbooks/api.yml
  )
else
  nohup uv run fastapi run --host 0.0.0.0 main.py > log 2>&1 &
  echo $! > pid
  echo "[API] Running with PID $(cat pid). Logging in 'log'."
fi
