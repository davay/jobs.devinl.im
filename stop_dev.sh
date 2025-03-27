#!/bin/bash

find_running_services() {
  pid_services=$(find . -type f -name "pid" -print0 | xargs -0 dirname | sort | uniq | xargs -n1 basename)
  docker_services=$(find . -type f -name "compose.yml" -print0 | xargs -0 dirname | sort | uniq | xargs -n1 basename | while read -r dir; do
    if (cd "$dir" && docker-compose ps --quiet | grep -q .); then
      echo "$dir"
    fi
  done)

  echo "$pid_services"
  echo "$docker_services"
}

stop_service() {
  local service="$1"

  if [ -f "$service/compose.yml" ]; then
    (cd "$service" && docker-compose down)
    echo "Stopped $service (Docker)"
  elif [ -f "$service/pid" ]; then
    pid=$(cat "$service/pid")
    kill "$pid" 2>/dev/null || true
    rm "$service/pid"
    echo "Stopped $service (PID: $pid)"
  else
    echo "$service not found"
  fi

}

# https://stackoverflow.com/questions/26479562/what-does-ifs-do-in-this-bash-loop-cat-file-while-ifs-read-r-line-do
services=()
while IFS= read -r line; do
  services+=("$line")
done < <(find_running_services)

if [ ${#services[@]} -eq 0 ]; then
  echo "No running services found."
  exit 0
fi

echo "Running services:"
for i in "${!services[@]}"; do
  service_name="${services[$i]}"

  if [ -f "$service_name/compose.yml" ]; then
    echo "  $((i+1)). $service_name (Docker)"
  else
    pid=$(cat "${services[$i]}/pid")
    echo "  $((i+1)). $service_name (PID: $pid)"
  fi
done

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
