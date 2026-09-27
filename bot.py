import asyncio
import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Replace with your actual token
TOKEN = "8642345808:AAF6WX3_LSe3uKF3Lxl1z5Cur6nfknZecK8"

# 1. Mini Web Server for Cloud Health Checks
web_app = Flask(__name__)


@web_app.route("/")
def home():
  return "Bot is alive!"


def run_web():
  port = int(os.environ.get("PORT", 8080))
  web_app.run(host="0.0.0.0", port=port)


# 2. Telegram Bot Logic
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("hi 👋")


def main():
  # Start the web server in a separate background thread
  threading.Thread(target=run_web, daemon=True).start()

  # Start the bot
  app = ApplicationBuilder().token(TOKEN).build()
  app.add_handler(CommandHandler("start", start))
  print("Bot is running...")
  app.run_polling()


if __name__ == "__main__":
  main()
