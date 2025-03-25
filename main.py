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
        "/authorize <user_id> - Authorize a user to control the bot\n"
        "/deauthorize <user_id> - Remove authorization\n"
        "/adminhelp - Show admin commands\n"
    )
    await update.message.reply_text(help_text)

async def main():
    """Initialize the bot and PyTgCalls."""
    application = Application.builder().token(BOT_TOKEN).build()

    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("play", play))
    application.add_handler(CommandHandler("pause", pause))
    application.add_handler(CommandHandler("resume", resume))
    application.add_handler(CommandHandler("skip", skip))
    application.add_handler(CommandHandler("queue", queue))
    application.add_handler(CommandHandler("stop", stop))
    application.add_handler(CommandHandler("lyrics", get_lyrics))
    application.add_handler(CommandHandler("authorize", authorize_user))
    application.add_handler(CommandHandler("deauthorize", deauthorize_user))
    application.add_handler(CommandHandler("adminhelp", admin_help))

    # Start Pyrogram client for PyTgCalls
    await app.start()

    # Start PyTgCalls
    await start_pytgcalls()

    logger.info("🚀 Vibie Bot is now running...")
    await application.run_polling()

# Run the bot with asyncio
if __name__ == '__main__':
    asyncio.run(main())