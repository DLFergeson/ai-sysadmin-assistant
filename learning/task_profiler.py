import json
from collections import Counter
from pathlib import Path

PROFILE_PATH = Path("data/user_profiles.json")

def update_profile(user_id, results):
    PROFILE_PATH.parent.mkdir(exist_ok=True)
    if PROFILE_PATH.exists():
        with open(PROFILE_PATH, "r") as f:
            profiles = json.load(f)
    else:
        profiles = {}

    if user_id not in profiles:
        profiles[user_id] = {
            "completed_tasks": [],
            "missed_tasks": [],
            "frequent_keywords": {}
        }

    for r in results:
        target = "completed_tasks" if r["valid"] else "missed_tasks"
        profiles[user_id][target].append(r["step"])

    all_steps = profiles[user_id]["completed_tasks"] + profiles[user_id]["missed_tasks"]
    word_counts = Counter(" ".join(all_steps).lower().split())
    profiles[user_id]["frequent_keywords"] = dict(word_counts.most_common(20))

    with open(PROFILE_PATH, "w") as f:
        json.dump(profiles, f, indent=2)

def get_profile(user_id):
    if PROFILE_PATH.exists():
        with open(PROFILE_PATH, "r") as f:
            profiles = json.load(f)
            return profiles.get(user_id, {})
    return {}
