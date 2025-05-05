import json
from datetime import datetime
from pathlib import Path

LOG_PATH = Path("data/usage_log.json")

def log_activity(event, data):
    LOG_PATH.parent.mkdir(exist_ok=True)
    if LOG_PATH.exists():
        with open(LOG_PATH, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append({
        "timestamp": datetime.now().isoformat(),
        "event": event,
        "data": data
    })

    with open(LOG_PATH, "w") as f:
        json.dump(logs, f, indent=2)
