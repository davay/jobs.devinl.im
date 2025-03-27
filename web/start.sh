#!/bin/bash

nohup pnpm run dev > log 2>&1 &
sleep 2
(lsof -i :5173 | awk 'NR>1 {print $2}' | head -n 1) > pid
echo "Web server running with PID $(cat pid). Logging in 'log'."
