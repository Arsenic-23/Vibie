import logging
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.admin_handler import handlers as admin_handlers
from handlers.auth_handler import authorize_user, unauthorize_user
from handlers.effects_handler import handlers as effects_handlers
from handlers.games_handler import handlers as games_handlers
from handlers.music_handler import handlers as music_handlers
from handlers.ai_chat_handler import ai_chat  # Correct import

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
bot.add_handler(authorize_user)
bot.add_handler(unauthorize_user)
bot.add_handler(ai_chat)  # Correct AI chat handler

# Register all grouped handlers
for handler in (
    admin_handlers + effects_handlers + games_handlers + music_handlers
):
    bot.add_handler(handler)

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