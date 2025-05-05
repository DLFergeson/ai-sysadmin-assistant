import subprocess
import os

def execute_script(path):
    if not os.path.exists(path):
        return "Script not found.", False

    try:
        if path.endswith(".py"):
            result = subprocess.run(["python3", path], capture_output=True, text=True)
        elif path.endswith(".ps1"):
            result = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", path],
                                    capture_output=True, text=True)
        else:
            return "Unsupported script type.", False

        output = result.stdout + "\n" + result.stderr
        return output, result.returncode == 0
    except Exception as e:
        return str(e), False
