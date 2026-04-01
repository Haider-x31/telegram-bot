import os
from flask import Flask, request
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔐 Environment Variables
TOKEN = os.getenv("BOT_TOKEN")
URL = os.getenv("RENDER_URL")

app = Flask(__name__)

# 🤖 Telegram App
telegram_app = Application.builder().token(TOKEN).build()

# 🟢 Start Command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    
    text = f"""
👋 أهلاً {user.first_name}

🤖 بوت تحميل احترافي

📥 أرسل رابط من:
- TikTok
- Instagram
- YouTube

وسيتم التحميل مباشرة 🔥
"""
    await update.message.reply_text(text)

# ➕ تسجيل الهاندلر
telegram_app.add_handler(CommandHandler("start", start))

# 🌐 Webhook Endpoint
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    try:
        update = Update.de_json(request.get_json(force=True), telegram_app.bot)
        telegram_app.update_queue.put_nowait(update)
    except Exception as e:
        print("Webhook Error:", e)
    return "ok"

# 🏠 Home Route
@app.route("/")
def home():
    return "Bot is running 🔥"

# 🚀 تشغيل
if __name__ == "__main__":
    print("Starting bot...")

    telegram_app.initialize()
    telegram_app.bot.set_webhook(url=f"{URL}/{TOKEN}")

    app.run(host="0.0.0.0", port=10000)
