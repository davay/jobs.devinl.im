#!/bin/bash

source ./scripts/shared_functions.sh

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
