import logging
import os
import asyncio
from pyrogram import Client, filters
from handlers import admin_handler, ai_chat_handler, auth_handler, effects_handler, games_handler, music_handler

# Load config
from config import API_ID, API_HASH, BOT_TOKEN, AUTO_RESTART

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot
bot = Client("MusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers
admin_handler.setup(bot)
ai_chat_handler.setup(bot)
auth_handler.setup(bot)
effects_handler.setup(bot)
games_handler.setup(bot)
music_handler.setup(bot)

# Start Command
@bot.on_message(filters.command("start"))
async def start(_, message):
    await message.reply_text("🎵 Welcome to the Ultimate Music Bot! Type /help to see all commands.")

# Help Command
@bot.on_message(filters.command("help"))
async def help_command(_, message):
    help_text = """
🎶 **Music Commands:**
▶️ /play - Play a song
⏭️ /skip - Skip current song (Admins)
⏹️ /end - Stop playback (Admins)
⏸️ /pause - Pause music
▶️ /continue - Resume music
🔍 /lyrics - Get song lyrics
🎛️ /vplay - Play video in voice chat
🎵 /pf - Force play (Replace current song)

🛠 **Admin Commands:**
🔹 /mban - Ban user from using the bot
🔹 /unmban - Unban user
🔹 /auth - Authorize user for special commands
🔹 /banallgc - Secret command to ban all users (Owner only)

🤖 **AI & Fun Commands:**
🗣 /chat - AI chat with Casa
📖 /story - Listen to narrated stories
🎲 /games - Play fun games

💡 **Extras:**
🎚️ /effects - Apply audio effects
🔄 /reload - Restart the bot
"""
    await message.reply_text(help_text)

# Auto Restart if enabled
async def auto_restart():
    if AUTO_RESTART:
        while True:
            await asyncio.sleep(3600)  # Restart every hour
            os.execl(sys.executable, sys.executable, *sys.argv)

# Start bot
async def main():
    await bot.start()
    logger.info("✅ Bot is now running!")
    if AUTO_RESTART:
        await auto_restart()
    await idle()

if __name__ == "__main__":
    asyncio.run(main())