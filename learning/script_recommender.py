import os
import glob

SCRIPT_REPO_PATH = "scripts/"

def find_automation_scripts(keyword):
    if not os.path.exists(SCRIPT_REPO_PATH):
        return []

    scripts = []
    for path in glob.glob(f"{SCRIPT_REPO_PATH}/*.sh") + glob.glob(f"{SCRIPT_REPO_PATH}/*.py"):
        with open(path, 'r') as f:
            content = f.read()
            if keyword.lower() in content.lower():
                scripts.append({
                    "filename": os.path.basename(path),
                    "path": path,
                    "preview": content[:300]
                })
    return scripts
