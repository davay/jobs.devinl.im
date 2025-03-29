#!/bin/bash

if [ ! -f ./.env ]; then
  read -rp "Is this a production environment? (y/N): " production_choice
  if [[ "${production_choice,,}" =~ ^(y|yes)$ ]]; then
    echo "ENVIRONMENT=production" > ./.env
    echo "Created .env with ENVIRONMENT=production"
  else
    # not technically checked, we default to dev mode in absence of production
    # still creating .env so it stops asking
    echo "ENVIRONMENT=development" > ./.env
    echo "Created .env with ENVIRONMENT=development"
  fi
fi

export "$(grep -v '^#' ./.env | xargs)"
echo "Using ENVIRONMENT=$ENVIRONMENT"

find_services() {
  # only search one level deep (excluding root so it doesn't find itself)
  find . -maxdepth 2 -mindepth 2 -type f -name "start.sh" -print0 | xargs -0 dirname | sort | uniq | xargs -n1 basename
}

check_service_status() {
  local service="$1"
  
  # docker -- the only docker service is db which is identical for production or dev
  if [ -f "$service/compose.yml" ]; then
    if (cd "$service" && docker-compose ps --quiet | grep -q .); then
      echo "Started (Docker)"
      return 0
    else
      echo "Stopped"
      return 1  
    fi
  # systemd
  elif [[ "$ENVIRONMENT" == "production" ]]; then
    if systemctl is-active --quiet "$service.service"; then
        echo "Started (Systemd)"
        return 0
    elif systemctl is-active --quiet "$service.timer"; then
        echo "Started (Systemd with timer)"
        return 0
    else
      echo "Stopped"
      return 1
    fi
  else
    # pid
    if [ -f "$service/pid" ]; then
      pid=$(cat "$service/pid")
      if ps -p "$pid" > /dev/null; then
        echo "Started (PID: $pid)"
        return 0  
      else
        echo "Stopped (stale PID file)"
        return 1  
      fi
    else
      echo "Stopped"
      return 1  
    fi
  fi
}

# https://stackoverflow.com/questions/26479562/what-does-ifs-do-in-this-bash-loop-cat-file-while-ifs-read-r-line-do
services=()
while IFS= read -r line; do
  services+=("$line")
done < <(find_services)

echo "Services:"
for i in "${!services[@]}"; do
  service_name="${services[$i]}"
  status=$(check_service_status "$service_name")
  echo "  $((i+1)). $service_name - $status"
done

