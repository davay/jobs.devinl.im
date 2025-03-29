#!/bin/bash

#!/bin/bash 

if [[ "$ENVIRONMENT" == "production" ]]; then
  read -rsp "[Web] Sudo password to setup Systemd service: " PASS
  echo
  (
    export ANSIBLE_BECOME_PASS="$PASS"
    ansible-playbook ../playbooks/web.yml
  )
else
  nohup pnpm run dev --host > log 2>&1 &
  sleep 3
  (lsof -i :5173 | awk 'NR>1 {print $2}' | head -n 1) > pid
  echo "[Web] Running with PID $(cat pid). Logging in 'log'."
fi
