import os
import asyncio
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

app_flask = Flask(__name__)

@app_flask.route("/")
def home():
    return "Bot is running 🔥"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 البوت شغال 24 ساعة!")

async def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("BOT STARTED 🔥")

    await app.initialize()
    await app.start()

    # تشغيل Flask داخل asyncio
    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: app_flask.run(host="0.0.0.0", port=10000))

if __name__ == "__main__":
    asyncio.run(main())
