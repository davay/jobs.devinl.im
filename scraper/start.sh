read -rsp "Enter your Anthropic API: " KEY
echo
ANTHROPIC_API_KEY=$KEY nohup uv run main.py > log 2>&1 &
sleep 1
(lsof -i :5173 | awk 'NR>1 {print $2}' | head -n 1) > pid
echo "Scraper running with PID $(cat pid). Logging in 'log'."
