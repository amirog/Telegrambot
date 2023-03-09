import requests
import json

# Your bot token
bot_token = "5934179946:AAFmJR5QatmUKhhUzBV3XQBHjuBXiCGkfg8"

# The chat ID of the channel the post is in
chat_id = "@YOUR_CHANNEL_NAME"

# The URL for the Telegram Bot API's "sendChatAction" method
url = f"https://api.telegram.org/bot{bot_token}/sendChatAction"

# Define a function to handle user input
def handle_input(update):
    # Get the chat ID and user input
    chat_id = update["message"]["chat"]["id"]
    text = update["message"]["text"]
    
    # Split the user input into the reaction and number of reactions
    reaction, num_reactions = text.split()
    num_reactions = int(num_reactions)

    # Loop through the number of reactions and send each one individually
    for i in range(num_reactions):
        # The payload for the request, including the chat ID, action, and message ID
        payload = {
            "chat_id": chat_id,
            "action": "react",
            "message_id": message_id,
            "emoji": reaction
        }

        # Send the request to the Telegram Bot API
        response = requests.post(url, json=payload)

        # Print the response from the API
        print(response.json())

# Define a function to listen for updates from Telegram
def listen_for_updates():
    # The URL for the Telegram Bot API's "getUpdates" method
    url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
    
    # Start an infinite loop to listen for updates
    while True:
        # Send a request to the Telegram Bot API to get updates
        response = requests.get(url)

        # Parse the JSON response
        updates = json.loads(response.content)["result"]

        # Loop through the updates and handle each one
        for update in updates:
            handle_input(update)

# Start listening for updates
listen_for_updates()
