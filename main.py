import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from handlers.music_handler import play, pause, resume, skip
from config import BOT_TOKEN
from utils.player import start_pytgcalls

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🎵 Hello! I am Vibie, your music bot.")

def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "/play <song_name> - Play a song\n"
        "/pause - Pause the song\n"
        "/resume - Resume the song\n"
        "/skip - Skip the current song\n"
    )
    update.message.reply_text(help_text)

def main():
    """Initialize the bot and PyTgCalls."""
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("pause", pause))
    dispatcher.add_handler(CommandHandler("resume", resume))
    dispatcher.add_handler(CommandHandler("skip", skip))

    # Start PyTgCalls
    start_pytgcalls()

    logger.info("🚀 Vibie Bot is now running...")
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()