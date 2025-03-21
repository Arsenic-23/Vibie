import os
import sys
import subprocess
import logging
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import music_handler, admin_handler, ai_chat_handler

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Install PyTgCalls manually (fix for Koyeb)
try:
    from pytgcalls import PyTgCalls
except ImportError:
    logger.info("Installing PyTgCalls...")
    subprocess.run([sys.executable, "-m", "pip", "install", "py-tgcalls"], check=True)
    from pytgcalls import PyTgCalls

# Initialize bot client
app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# Register handlers
music_handler.register_handlers(app, call_py)
admin_handler.register_handlers(app, call_py)
ai_chat_handler.register_handlers(app)

# Start the bot
if __name__ == "__main__":
    logger.info("Starting the bot...")
    call_py.start()
    app.run()