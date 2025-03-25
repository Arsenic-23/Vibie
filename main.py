import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from handlers.music_handler import play_music, pause_music, skip_music, queue_music, show_playlist, vote_skip
from handlers.admin_handler import manage_playlist, skip_song, authorize_user
from handlers.lyrics_handler import sync_lyrics, fetch_lyrics
from handlers.command_handler import start, help_command

# Enable logging to track errors and bot activity
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Start command: Initializes the bot and greets users
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I am Vibie, your music bot. Type /help to see the available commands.")

# Help command: Shows available commands and usage
def help_command(update: Update, context: CallbackContext) -> None:
    help_text = (
        "/play <song_name> - Play a song\n"
        "/pause - Pause the song\n"
        "/skip - Skip the song\n"
        "/queue - Show the current song queue\n"
        "/playlist - Manage your playlist\n"
        "/lyrics - Show lyrics of the song\n"
        "/help - Show this message\n"
        "/skip_song - Skip the current song (Admin only)\n"
        "/authorize_user - Authorize a user to manage playlists (Admin only)\n"
        "/vote_skip - Vote to skip a song (3 votes required)"
    )
    update.message.reply_text(help_text)

def main():
    """Start the bot and initialize the handlers."""
    # Initialize Updater with your bot's token
    updater = Updater("YOUR_BOT_TOKEN")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Command Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("play", play_music))
    dispatcher.add_handler(CommandHandler("pause", pause_music))
    dispatcher.add_handler(CommandHandler("skip", skip_music))
    dispatcher.add_handler(CommandHandler("queue", queue_music))
    dispatcher.add_handler(CommandHandler("playlist", show_playlist))

    # Admin-specific Handlers
    dispatcher.add_handler(CommandHandler("skip_song", skip_song))
    dispatcher.add_handler(CommandHandler("authorize_user", authorize_user))

    # Lyrics-related Handlers
    dispatcher.add_handler(CommandHandler("lyrics", fetch_lyrics))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, sync_lyrics))  # Sync lyrics with the music

    # Voting to Skip Handler
    dispatcher.add_handler(CommandHandler("vote_skip", vote_skip))

    # Start polling for updates from users
    updater.start_polling()

    # Run the bot until manually stopped
    updater.idle()

if __name__ == '__main__':
    main()