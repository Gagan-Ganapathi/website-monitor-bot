import requests
from bs4 import BeautifulSoup
import time

# Replace with your actual bot token
BOT_TOKEN = "7668312391:AAETbt5wsPRsMGhaWzP2IghH8uzSdc-aPG8"

# Replace with your group's Chat ID (must start with -)
GROUP_CHAT_ID = "-1002363365966"  

# Website URL to monitor
URL = "https://shop.royalchallengers.com/ticket"  # Change this to the real URL you want to track
previous_content = None

def send_group_message(message):
    """Sends a message to the Telegram group."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    data = {"chat_id": GROUP_CHAT_ID, "text": message}
    response = requests.post(url, data=data)
    print(response.json())  # Optional: Check response for debugging

def check_website():
    """Checks the website for changes and sends a notification if detected."""
    global previous_content
    headers = {"User-Agent": "Mozilla/5.0"}  # Prevents getting blocked
    response = requests.get(URL, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        current_content = soup.get_text()

        if previous_content and previous_content != current_content:
            send_group_message("🚨 Alert! The website has changed!")
        previous_content = current_content
    else:
        print(f"Error: Unable to access {URL}. Status code: {response.status_code}")

# Run the script continuously, checking every 60 seconds
while True:
    check_website()
    time.sleep(60)  # Wait 1 minute before checking again
