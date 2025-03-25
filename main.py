import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from handlers.music_handler import play_music, pause_music, skip_music, queue_music, show_playlist, vote_skip
from handlers.admin_handler import manage_playlist, skip_song, authorize_user
from handlers.lyrics_handler import sync_lyrics, fetch_lyrics
from handlers.command_handler import start, help_command
from config import BOT_TOKEN  # ✅ Import token from config.py

# ✅ Enable logging for debugging and monitoring
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# ✅ Define start command (greets users)
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("🎵 Hello! I am Vibie, your music bot. Type /help to see the available commands.")

# ✅ Help command (lists available commands)
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "🎶 *Music Commands:*\n"
        "/play <song_name> - Play a song\n"
        "/pause - Pause the song\n"
        "/skip - Skip the current song\n"
        "/queue - Show the song queue\n"
        "/playlist - Manage your playlist\n"
        "/lyrics - Show lyrics of the current song\n"
        "/vote_skip - Vote to skip a song (3 votes needed)\n\n"
        "⚙️ *Admin Commands:*\n"
        "/skip_song - Force skip the current song (Admins only)\n"
        "/authorize_user - Give a user playlist control (Admins only)\n\n"
        "ℹ️ Type a command to use it!"
    )
    update.message.reply_text(help_text, parse_mode="Markdown")

# ✅ Main function to start the bot
def main():
    """Initialize the bot and command handlers."""
    # ✅ Use Updater with the bot token from config.py
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # ✅ Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("play", play_music))
    dispatcher.add_handler(CommandHandler("pause", pause_music))
    dispatcher.add_handler(CommandHandler("skip", skip_music))
    dispatcher.add_handler(CommandHandler("queue", queue_music))
    dispatcher.add_handler(CommandHandler("playlist", show_playlist))

    # ✅ Admin commands
    dispatcher.add_handler(CommandHandler("skip_song", skip_song))
    dispatcher.add_handler(CommandHandler("authorize_user", authorize_user))

    # ✅ Lyrics commands
    dispatcher.add_handler(CommandHandler("lyrics", fetch_lyrics))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, sync_lyrics))

    # ✅ Voting system
    dispatcher.add_handler(CommandHandler("vote_skip", vote_skip))

    # ✅ Error handling
    def error_handler(update: Update, context: CallbackContext):
        logger.error(f"⚠️ Error occurred: {context.error}")

    dispatcher.add_error_handler(error_handler)

    # ✅ Start the bot
    logger.info("🚀 Vibie Bot is now running...")
    updater.start_polling()
    updater.idle()

# ✅ Run the bot
if __name__ == '__main__':
    main()