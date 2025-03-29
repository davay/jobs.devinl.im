#!/bin/bash

find_services() {
  # only search one level deep (excluding root so it doesn't find itself)
  find . -maxdepth 2 -mindepth 2 -type f -name "start.sh" -print0 | xargs -0 dirname | sort | uniq | xargs -n1 basename
}

check_service_status() {
  local service="$1"
  
  # systemd
  if [[ "$ENVIRONMENT" == "production" ]]; then
    if systemctl is-active --quiet "$service"; then
      echo "Started (systemd)"
      return 0  
    else
      echo "Stopped"
      return 1  
    fi
  else
    # docker
    if [ -f "$service/compose.yml" ]; then
      if (cd "$service" && docker-compose ps --quiet | grep -q .); then
        echo "Started (Docker)"
        return 0
      else
        echo "Stopped"
        return 1  
      fi
    # pid
    else
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
  fi
}

start_service() {
  local service="$1"
  
  if check_service_status "$service" > /dev/null; then
    echo "$service is already running"
  else
    echo "Starting $service..."
    (cd "$service" && ./start.sh)
  fi
}

# TODO: commenting out start all for now, there's a dependency between services so can't start all in random order
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

echo
echo "Select service to start:"
# echo "  a. Start all services"
echo "  q. Quit without starting any service"
echo

read -rp "Enter your choice [1-${#services[@]}/a/q]: " choice
case "$choice" in
  [1-9]|[1-9][0-9])
    if [ "$choice" -le "${#services[@]}" ]; then
      index=$((choice-1))
      start_service "${services[$index]}"
    else
      echo "Invalid choice"
    fi
    ;;
  # a|A)
  #   for service in "${services[@]}"; do
  #     start_service "${service}"
  #   done
  #   ;;
  q|Q)
    ;;
  *)
    echo "Invalid choice"
    ;;
esac
