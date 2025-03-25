#!/bin/bash

cd api
nohup uv run fastapi run --host 0.0.0.0 main.py > api.log 2>&1 &
echo $! > api.pid
echo "FastAPI server running with PID $(cat api.pid). Log at api.log."
