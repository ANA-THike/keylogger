# Keylogger with Telegram Bot Integration

This Python program functions as a keylogger, capturing keystrokes from the system and sending the captured data to your Telegram bot at a set interval (default: every 30 minutes). The program can be compiled into an executable (.exe) and runs in the background.

## Features

- Captures keystrokes from the system.
- Sends captured data to your Telegram bot every 30 minutes (adjustable).
- Runs in the background.
- Can be compiled into an executable (.exe).

## Requirements

Before using the program, ensure you have the following:

- Python 3.x installed on your system.
- `pyTelegramBotAPI` library installed for interacting with the Telegram bot.
- `pynput` library for capturing keystrokes.
- `pyinstaller` library to convert the Python script into an executable.

You can install the required libraries using pip:

```bash
pip install pyTelegramBotAPI pynput pyinstaller
