import os
import logging
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Function that talks to Francessa on Poe.com
async def ask_francessa(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_input = ' '.join(context.args)
    if not user_input:
        await update.message.reply_text("Ask something after the command. Example: /ask Hello Francessa!")
        return

    # Simulated response for now
    # Replace with Poe API logic once available or using Poe web scraping
    response = f"Francessa says: I received your message – '{user_input}'."

    await update.message.reply_text(response)

# Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I’m Francessa, your AI assistant. Use /ask <your question>.")

def main():
    token = os.getenv("TELEGRAM_TOKEN")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ask", ask_francessa))

    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
