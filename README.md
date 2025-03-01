
# Keylogger with Telegram Bot Integration

This Python program functions as a keylogger, capturing keystrokes from the system and sending the captured data to your Telegram bot at a set interval (default: every 30 minutes). The program can be compiled into an executable (.exe) and runs in the background.

> **Disclaimer**: This project is for educational purposes only. Unauthorized use of keyloggers is illegal and unethical. Do not use it without explicit consent.

## Features

- Captures keystrokes from the system.
- Sends captured data to your Telegram bot every 30 minutes (interval adjustable).
- Runs in the background.
- Can be compiled into an executable (.exe).

## Requirements

Before using the program, ensure you have the following:

- **Python 3.x**: The programming language for the script.
- **`pyTelegramBotAPI`**: Library for interacting with the Telegram bot.
- **`pynput`**: Library for capturing keystrokes.
- **`pyinstaller`**: Tool to convert the Python script into an executable.

You can install the required libraries using pip:

```bash
pip install pyTelegramBotAPI pynput pyinstaller
```

## Setup

1. Clone or download the repository containing the script.

2. Open the `config.py` file and set the following variables:

   - `TELEGRAM_BOT_TOKEN`: Your Telegram bot token from [BotFather](https://core.telegram.org/bots#botfather).
   - `TELEGRAM_CHAT_ID`: Your Telegram chat ID where the keystroke logs will be sent.
   - `LOG_INTERVAL`: The interval in seconds for sending captured logs. The default is 1800 seconds (30 minutes).

   Example `config.py`:

   ```python
   TELEGRAM_BOT_TOKEN = 'your-bot-token'
   TELEGRAM_CHAT_ID = 'your-chat-id'
   LOG_INTERVAL = 1800  # Interval in seconds (default: 30 minutes)
   ```

3. The program will capture keystrokes for the specified interval, then send the logs to your Telegram bot. The default interval is 30 minutes (`1800` seconds), but you can modify this value by setting `LOG_INTERVAL` to any number of seconds.

### Example for 15-minute interval:
```python
LOG_INTERVAL = 900  # Capture for 15 minutes
```

## Running the Script

To run the script, execute the following command:

```bash
python keylogger.py
```

Once the script is running, it will capture keystrokes and send the data to your Telegram bot at the specified interval.

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
