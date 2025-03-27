#!/bin/bash 

nohup uv run fastapi run --host 0.0.0.0 main.py > log 2>&1 &
echo $! > pid
echo "API server running with PID $(cat pid). Logging in 'log'."

