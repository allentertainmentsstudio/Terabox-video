from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handler import register_handlers

app = Client(
    "teraboxbot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

register_handlers(app)

app.run()
