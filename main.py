import threading
import asyncio
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handler import register_handlers

# Flask app initialization
web = Flask(__name__)

@web.route("/")
def home():
    return "Bot is running!"

# Pyrogram client initialization
app = Client(
    "teraboxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register your handlers
register_handlers(app)

# Function to run the Flask web server
def run_web():
    web.run(host="0.0.0.0", port=8080)

# Start Flask server in a separate thread
threading.Thread(target=run_web).start()

# Async function to run the Pyrogram client
async def start_bot():
    await app.start()
    print("Bot is running...")

# Run the bot in the asyncio event loop
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
