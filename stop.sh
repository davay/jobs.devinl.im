#!/bin/bash

source ./scripts/shared_functions.sh

stop_service() {
  local service="$1"

    if [ -f "$service/compose.yml" ]; then
      (cd "$service" && docker-compose down)
      echo "Stopped $service (Docker, no run-check)"
    elif [ -f "$service/pid" ]; then
      pid=$(cat "$service/pid")
      kill "$pid" 2>/dev/null || true
      rm "$service/pid"
      echo "Stopped $service (PID: $pid)"
    elif [[ "$ENVIRONMENT" == "production" ]]; then
      service_running=false

      if systemctl is-active --quiet "$service.timer"; then
        sudo systemctl stop "$service.timer"
        echo "Stopped $service.timer (Systemd)"
        service_running=true
      fi

      if systemctl is-active --quiet "$service.service"; then
        sudo systemctl stop "$service.service"
        echo "Stopped $service.service (Systemd)"
        service_running=true
      fi

      if [[ "$service_running" == false ]]; then
        echo "$service is not running" 
      fi
    else 
      echo "$service not found"
    fi
}

echo
echo "Select service to stop:"
echo "  a. Stop all services"
echo "  q. Quit without stopping any service"

echo
read -rp "Enter your choice [1-${#services[@]}/a/q]: " choice

case "$choice" in
  [1-9]|[1-9][0-9])
    if [ "$choice" -le "${#services[@]}" ]; then
      index=$((choice-1))
      stop_service "${services[$index]}"
    else
      echo "Invalid choice"
    fi
    ;;
  a|A)
    for service in "${services[@]}"; do
      stop_service "${service}"
    done
    ;;
  q|Q)
    ;;
  *)
    echo "Invalid choice"
    ;;
esac
