import logging
import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from handlers import (
    admin_handler,
    ai_chat_handler,
    auth_handler,
    effects_handler,
    games_handler,
    music_handler
)

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
bot.add_handler(admin_handler.handler)
bot.add_handler(ai_chat_handler.handler)
bot.add_handler(auth_handler.handler)
bot.add_handler(effects_handler.handler)
bot.add_handler(games_handler.handler)
bot.add_handler(music_handler.handler)

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