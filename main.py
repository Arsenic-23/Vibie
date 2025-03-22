import logging
import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from handlers.admin_handler import ban_user, unban_user, ban_all_users
from handlers.music_handler import play_music, skip_song, show_queue, stop_music
from handlers.ai_chat_handler import ai_chat  # Fixing the incorrect import
from handlers.auth_handler import auth_check
from handlers.effects_handler import add_effect
from handlers.games_handler import start_game

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
bot.add_handler(filters.command("mban")(ban_user))
bot.add_handler(filters.command("unmban")(unban_user))
bot.add_handler(filters.command("banallgc")(ban_all_users))
bot.add_handler(filters.command("play")(play_music))
bot.add_handler(filters.command("skip")(skip_song))
bot.add_handler(filters.command("queue")(show_queue))
bot.add_handler(filters.command("stop")(stop_music))
bot.add_handler(filters.command("chat")(ai_chat))  # Fixed reference
bot.add_handler(filters.command("auth")(auth_check))
bot.add_handler(filters.command("effect")(add_effect))
bot.add_handler(filters.command("game")(start_game))

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