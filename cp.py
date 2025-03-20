import logging
import psutil
import time
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Bot start time
START_TIME = time.time()

# Logging setup
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# Replace with your bot token
TOKEN = "7823259730:AAH17oUrAdJHVjgzZQ88hhdD706fPtz9DH4"

# Dummy storage for total users
user_data = set()

async def start(update: Update, context: CallbackContext):
    """Handles the /start command"""
    user_id = update.effective_user.id
    user_data.add(user_id)  # Store user ID
    await update.message.reply_text("Hello! I'm alive. Use /status to check my status.")

async def status(update: Update, context: CallbackContext):
    """Handles the /status command"""
    uptime = time.time() - START_TIME
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    total_users = len(user_data)

    status_text = (
        f"🤖 *Bot Status*\n"
        f"⏳ Uptime: {int(uptime)} seconds\n"
        f"👥 Users: {total_users}\n"
        f"💾 CPU: {cpu_usage}%\n"
        f"🧠 RAM: {memory_usage}%"
    )

    await update.message.reply_text(status_text, parse_mode="Markdown")

def main():
    """Starts the bot"""
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("status", status))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
