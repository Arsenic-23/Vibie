import os
import sys
import logging
import threading
import subprocess
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Debugging: Print current working directory and files
print("📂 Current directory:", os.getcwd())
print("📁 Files in workspace:", os.listdir())

# Check if handlers folder exists
if os.path.exists("handlers"):
    print("📂 Handlers folder found. Contents:", os.listdir("handlers"))
else:
    print("❌ Handlers folder is missing!")

# Import handlers AFTER debugging file paths
try:
    from handlers import music_handler, admin_handler, ai_chat_handler
    print("✅ Handlers imported successfully!")
except ModuleNotFoundError as e:
    print(f"❌ Error importing handlers: {e}")
    sys.exit(1)  # Stop execution if handlers are missing

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Health check web server for Koyeb
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running", 200

def run_health_check():
    app.run(host="0.0.0.0", port=8080)

# Clone `relo` if it's missing
if not os.path.exists("relo"):
    subprocess.run(["git", "clone", "https://github.com/ldott/relo.git"], check=True)

# Add `relo` to Python's module path
sys.path.append(os.path.abspath("relo"))
from relo import Relo  # Import after adding to path

# Initialize bot client
try:
    app_client = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    logger.info("✅ Telegram bot initialized successfully!")
except Exception as e:
    logger.error(f"❌ Failed to initialize bot: {e}")
    sys.exit(1)  # Exit to avoid infinite restart loops

# Register handlers
music_handler.register_handlers(app_client)
admin_handler.register_handlers(app_client)
ai_chat_handler.register_handlers(app_client)

if __name__ == "__main__":
    logger.info("🚀 Starting the bot...")

    # Start health check server
    threading.Thread(target=run_health_check, daemon=True).start()
    
    # Start bot
    try:
        app_client.run()
    except Exception as e:
        logger.error(f"❌ Bot failed to start: {e}")
        sys.exit(1)  # Exit to prevent restart loops