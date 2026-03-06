📦 TeraBox Video Downloader Telegram Bot

A simple Telegram bot that downloads videos from TeraBox share links and sends them directly in Telegram.

---

🚀 Features

- 📥 Download video from TeraBox link
- 📤 Upload video directly to Telegram
- 🤖 Easy to use Telegram bot
- ⚡ Fast download and upload
- 🐳 Docker support

---

📁 Project Structure

AK/
dockerfile
README.md
main.py
bot.py
requirements.txt
config.py

---

⚙️ Requirements

- Python 3.8+
- Telegram Bot Token
- Telegram API ID
- Telegram API Hash

Get API credentials from:
https://my.telegram.org

---

🔧 Configuration

Edit config.py

API_ID = 123456
API_HASH = "YOUR_API_HASH"
BOT_TOKEN = "YOUR_BOT_TOKEN"

---

📦 Installation

Clone the repository:

git clone https://github.com/allentertainmentsstudio/Terabox-video/tree/main?
cd terabox-video

Install dependencies:

pip install -r requirements.txt

---

▶️ Run the Bot

python main.py

---

🐳 Run with Docker

Build Docker image:

docker build -t terabox-bot .

Run container:

docker run terabox-bot

---

📲 Usage

1. Start the bot in Telegram

/start

2. Send a TeraBox link

Example:

https://terabox.com/s/xxxxxx

3. The bot will download the video and upload it to Telegram.

---

⚠️ Disclaimer

This project is for educational purposes only.
The developer is not responsible for misuse of this bot.

---

⭐ Support

If you like this project, please star the repository.
