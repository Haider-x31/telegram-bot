import os
import asyncio
import threading
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

async def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    print("BOT STARTED 🔥")

    await app.initialize()
    await app.start()

    while True:
        await asyncio.sleep(10)

def start_bot():
    asyncio.run(run_bot())

if __name__ == "__main__":
    t = threading.Thread(target=start_bot)
    t.start()

    app_flask.run(host="0.0.0.0", port=10000)
