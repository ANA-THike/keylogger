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
