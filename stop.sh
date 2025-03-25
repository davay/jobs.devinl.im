cd api
if [ -f api.pid ]; then
  kill "$(cat api.pid)" && rm api.pid && echo "FastAPI server stopped"
else
  echo "FastAPI server not found"
fi

