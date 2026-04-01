import os
import asyncio
from flask import Flask
from threading import Thread
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# ================== إعدادات ==================
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "0"))

# ================== Flask ==================
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running 🔥"

@app.route("/health")
def health():
    return {"status": "alive"}

def run_web():
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

# ================== أوامر البوت ==================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 البوت شغال 24 ساعة!")

async def admin(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text("👑 انت الادمن")
    else:
        await update.message.reply_text("❌ مو مصرح")

# ================== تشغيل البوت ==================

async def run_bot():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("admin", admin))

    print("BOT STARTED 🔥")

    await application.run_polling()

# ================== التشغيل ==================

if __name__ == "__main__":
    # تشغيل السيرفر
    Thread(target=run_web).start()

    # تشغيل البوت
    asyncio.run(run_bot())
