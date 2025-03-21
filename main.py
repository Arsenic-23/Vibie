import os
import sys
import logging
import subprocess

from pyrogram import Client
from pytgcalls import PyTgCalls
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import music_handler, admin_handler, ai_chat_handler

# Step 1: Clone `relo` if it's missing
if not os.path.exists("relo_local"):
    subprocess.run(["git", "clone", "https://github.com/ldott/relo.git", "relo_local"], check=True)

# Step 2: Add `relo_local` to Python's module path
sys.path.append(os.path.abspath("relo_local"))

# Step 3: Now import Relo
from relo import Relo

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot client
app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# Import handlers
music_handler.register_handlers(app, call_py)
admin_handler.register_handlers(app, call_py)
ai_chat_handler.register_handlers(app)

# Start the bot
if __name__ == "__main__":
    logger.info("Starting the bot...")
    call_py.start()
    app.run()