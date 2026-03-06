import requests
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("teraboxbot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)


def get_direct_link(url):
    api = f"https://terabox-dl-api.vercel.app/api?url={url}"
    r = requests.get(api).json()
    return r["download_link"]


@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply("👋 Send TeraBox Link")


@app.on_message(filters.text)
async def download(client, message):

    url = message.text

    if "terabox" not in url:
        await message.reply("❌ Send valid TeraBox link")
        return

    msg = await message.reply("⏳ Downloading...")

    try:
        link = get_direct_link(url)

        r = requests.get(link, stream=True)

        with open("video.mp4", "wb") as f:
            for chunk in r.iter_content(1024 * 1024):
                f.write(chunk)

        await msg.edit("📤 Uploading...")

        await message.reply_video("video.mp4")

    except:
        await msg.edit("❌ Failed to fetch video")


app.run()
