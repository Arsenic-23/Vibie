import logging
import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.admin_handler import admin_handler
from handlers.auth_handler import authorize_user, unauthorize_user
from handlers.effects_handler import effects_handler
from handlers.games_handler import games_handler
from handlers.music_handler import music_handler
from handlers.ai_chat_handler import ai_chat  # Correctly importing ai_chat

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize bot client
bot = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Register handlers
bot.add_handler(filters.command("auth")(authorize_user))
bot.add_handler(filters.command("unauth")(unauthorize_user))
bot.add_handler(filters.command("ask")(ai_chat))  # Correctly adding AI chat handler
bot.add_handler(admin_handler)
bot.add_handler(effects_handler)
bot.add_handler(games_handler)
bot.add_handler(music_handler)

async def restart_bot():
    """ Restarts the bot automatically if it crashes. """
    while True:
        try:
            await bot.start()
            await bot.idle()
        except Exception as e:
            logger.error(f"Bot crashed! Restarting... Error: {e}")
            await asyncio.sleep(5)  # Wait before restart

if __name__ == "__main__":
    asyncio.run(restart_bot())