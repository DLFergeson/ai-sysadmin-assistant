# AI Sysadmin Assistant

## Detailed Setup Guides

### Configuring the Telegram Bot
1. **Create a Telegram Bot**:
   - Open Telegram, search for "BotFather," and use `/newbot` to create a bot.
   - Follow the prompts to name your bot and receive an **API token**.
2. **Add the Bot to Your Chat**:
   - Find your bot in Telegram and start a chat.
3. **Store the API Token**:
   - Create a `.env` file in the project root and add:
     ```
     TELEGRAM_BOT_TOKEN=your_token_here
     ```
4. **Enable the Bot**:
   - Ensure `telegram_bot.py` reads the token from `.env`.

### Setting Up Notification Channels
- **Email Notifications**:
  1. Configure email settings in `config.py`:
     ```python
     EMAIL_CONFIG = {
         'sender': 'your_email@example.com',
         'password': 'your_password',
         'smtp_server': 'smtp.example.com',
         'port': 587
     }
     ```
- **Discord Webhooks**:
  1. Create a webhook in your Discord server settings.
  2. Add the URL to `config.py`:
     ```python
     DISCORD_WEBHOOK_URL = 'your_webhook_url_here'
     ```

### Installation on Different OS Platforms
- **Linux**:
  1. Ensure Python 3.8+ is installed.
  2. Clone and install:
     ```bash
     git clone https://github.com/DLFergeson/ai-sysadmin-assistant.git
     cd ai-sysadmin-assistant
     pip install -r requirements.txt
     ```
- **macOS**:
  1. Install Homebrew: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
  2. Install Python: `brew install python`
  3. Follow Linux steps.
- **Windows**:
  1. Install Python 3.8+ from [python.org](https://www.python.org/downloads/).
  2. Clone or download the ZIP, then:
     ```bash
     pip install -r requirements.txt
     ```

## Usage Scenarios

### Monitoring a New Server
1. Add the server to `config.py`:
   ```python
   MONITORED_SERVERS = ['192.168.1.100', 'server.example.com']
   ```
2. Start monitoring:
   ```bash
   python monitor.py
   ```
3. Check metrics via console or Telegram.

### Setting Up Alerts for High CPU Usage
1. Define thresholds in `config.py`:
   ```python
   ALERT_THRESHOLDS = {
       'cpu': 80,
       'memory': 90,
       'disk': 85
   }
   ```
2. Enable notifications (e.g., Telegram, email).
3. Alerts trigger automatically when thresholds are exceeded.

### Restarting a Service via Telegram
1. Send: `/restart_service apache2`
2. Bot responds:
   ```
   Service apache2 restarted successfully.
   ```

## Troubleshooting

- **Telegram Bot Not Responding**:
  - Verify the token in `.env` and ensure the bot is started in Telegram.
- **API Connection Failures**:
  - Check internet connection and API keys in config files.
- **Permission Errors**:
  - Run with elevated privileges (e.g., `sudo` on Linux/macOS).