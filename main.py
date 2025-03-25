import logging
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from config import BOT_TOKEN
from handlers.music_handler import play, pause, resume, skip, queue, stop
from handlers.admin_handler import admin_help, authorize_user, deauthorize_user
from handlers.lyrics_handler import get_lyrics
from handlers.command_handler import start  # Use the existing start command from command_handler.py
from utils.player import app, start_pytgcalls  # Ensure Pyrogram client is started

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "/play <song_name> - Play a song\n"
        "/pause - Pause the song\n"
        "/resume - Resume the song\n"
        "/skip - Skip the current song\n"
        "/queue - Show the song queue\n"
        "/stop - Stop music playback\n"
        "/lyrics <song_name> - Get song lyrics\n"
        "/authorize <user_id> - Grant admin permissions\n"
        "/deauthorize <user_id> - Remove admin permissions\n"
    )
    await update.message.reply_text(help_text)

def main():
    """Start the bot and register command handlers."""
    app = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("play", play))
    app.add_handler(CommandHandler("pause", pause))
    app.add_handler(CommandHandler("resume", resume))
    app.add_handler(CommandHandler("skip", skip))
    app.add_handler(CommandHandler("queue", queue))
    app.add_handler(CommandHandler("stop", stop))
    app.add_handler(CommandHandler("lyrics", get_lyrics))
    app.add_handler(CommandHandler("authorize", authorize_user))
    app.add_handler(CommandHandler("deauthorize", deauthorize_user))

    # Start PyTgCalls for voice functionality
    asyncio.run(start_pytgcalls())

    # Start the bot
    logger.info("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
