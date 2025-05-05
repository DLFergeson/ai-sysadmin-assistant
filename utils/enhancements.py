import requests
import subprocess
import platform
import unittest

# Robust Error Handling
def send_telegram_message(chat_id, message, token):
    try:
        response = requests.post(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data={"chat_id": chat_id, "text": message}
        )
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message: {e}")

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
        return None

# Modularity (Example OS Detection)
if platform.system() == "Linux":
    def platform_command():
        return run_command("ls -l")
elif platform.system() == "Windows":
    def platform_command():
        return run_command("dir")
else:  # macOS (Darwin)
    def platform_command():
        return run_command("ls -l")

# Testing
class TestRunCommand(unittest.TestCase):
    def test_run_command_success(self):
        result = run_command("echo Hello")
        self.assertEqual(result.strip(), "Hello")

    def test_run_command_failure(self):
        result = run_command("invalid_command")
        self.assertIsNone(result)

if __name__ == "__main__":
    unittest.main()