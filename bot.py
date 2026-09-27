from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8642345808:AAF6WX3_LSe3uKF3Lxl1z5Cur6nfknZecK8"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
  await update.message.reply_text("hi 👋")


if __name__ == "__main__":
  app = ApplicationBuilder().token(TOKEN).build()
  app.add_handler(CommandHandler("start", start))
  print("Bot is running...")
  app.run_polling()
