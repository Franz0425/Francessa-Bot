import os
from telegram.ext import Application, CommandHandler
from flask import Flask
import threading

# Set up Flask app to keep Render happy
web = Flask(__name__)

@web.route('/')
def home():
    return "Francessa Bot is running."

# Start Flask in a background thread
def start_web():
    port = int(os.environ.get('PORT', 10000))
    web.run(host='0.0.0.0', port=port)

# Telegram bot
BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Hello! I am Francessa 🤖")

def main():
    threading.Thread(target=start_web).start()
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == "__main__":
    main()
