import platform
import subprocess
import logging
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def platform_command():
    """Return system name (e.g., Windows, Linux)"""
    return platform.system()

def run_command(cmd):
    """Execute a shell command safely"""
    try:
        result = subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode().strip()
    except subprocess.CalledProcessError as e:
        logging.error(f"Command failed: {e}")
        return e.stderr.decode().strip()

def send_telegram_message(chat_id=TELEGRAM_CHAT_ID, message="Test alert", token=TELEGRAM_BOT_TOKEN):
    """Send a Telegram message using a bot"""
    if not chat_id or not token:
        return "Missing token or chat_id"
    try:
        import requests
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {"chat_id": chat_id, "text": message}
        response = requests.post(url, data=data)
        return response.status_code == 200
    except Exception as e:
        logging.error(f"Telegram send error: {e}")
        return False
