import logging
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN
import handlers.admin_handler as admin_handler
import handlers.ai_chat_handler as ai_chat_handler
import handlers.auth_handler as auth_handler
import handlers.effects_handler as effects_handler
import handlers.games_handler as games_handler
import handlers.music_handler as music_handler

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
bot.add_handler(admin_handler.ban_user)
bot.add_handler(admin_handler.unban_user)
bot.add_handler(admin_handler.ban_all_users)

bot.add_handler(ai_chat_handler.some_ai_handler)  # Replace with actual handler

bot.add_handler(auth_handler.authorize_user)
bot.add_handler(auth_handler.unauthorize_user)

bot.add_handler(effects_handler.some_effect_handler)  # Replace with actual handler
bot.add_handler(games_handler.some_game_handler)  # Replace with actual handler
bot.add_handler(music_handler.some_music_handler)  # Replace with actual handler

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