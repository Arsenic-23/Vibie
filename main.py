import logging
import asyncio
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Import handlers (fixing incorrect imports)
from handlers.admin_handler import ban_user, unban_user, ban_all_users
from handlers.effects_handler import chipmunk_effect, deep_effect, echo_effect
from handlers.games_handler import puzzle_game, check_puzzle_answer
from handlers.music_handler import play_music, skip_song, show_queue, stop_music

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

# Register all handlers manually
bot.add_handler(ban_user)
bot.add_handler(unban_user)
bot.add_handler(ban_all_users)
bot.add_handler(chipmunk_effect)
bot.add_handler(deep_effect)
bot.add_handler(echo_effect)
bot.add_handler(puzzle_game)
bot.add_handler(check_puzzle_answer)
bot.add_handler(play_music)
bot.add_handler(skip_song)
bot.add_handler(show_queue)
bot.add_handler(stop_music)

async def start_bot():
    """ Starts the bot and keeps it running. """
    try:
        await bot.start()
        logger.info("Bot started successfully!")
        await bot.idle()
    except Exception as e:
        logger.error(f"Bot crashed! Restarting... Error: {e}")
        await asyncio.sleep(5)  # Wait before restart
        await start_bot()  # Restart bot

if __name__ == "__main__":
    asyncio.run(start_bot())