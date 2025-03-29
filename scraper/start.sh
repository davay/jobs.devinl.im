#!/bin/bash

if [[ "$ENVIRONMENT" == "production" ]]; then
  read -rsp "[Scraper] Sudo password to setup Systemd service: " PASS
  echo
  (
    export ANSIBLE_BECOME_PASS="$PASS"
    ansible-playbook ../playbooks/scraper.yml
  )
else
  read -rsp "[Scraper] Please enter your Anthropic API Key: " KEY
  echo
  ANTHROPIC_API_KEY=$KEY nohup uv run main.py > log 2>&1 &
  sleep 1
  (lsof -i :5173 | awk 'NR>1 {print $2}' | head -n 1) > pid
  echo "[Scraper] Running with PID $(cat pid). Logging in 'log'."
fi
