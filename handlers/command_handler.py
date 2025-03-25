import json
import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from config import BOT_NAME
from utils.player import MusicPlayer
from database.user_data import get_user_data, save_user_data
from database.playlist_data import get_queue
from utils.lyrics import get_lyrics_for_song

# Initialize the music player
music_player = MusicPlayer()

# Configure logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Start Command
async def start(update: Update, context: CallbackContext):
    """Send a welcome message when the /start command is used."""
    user = update.message.from_user
    user_id = user.id

    # Retrieve or create user data
    user_data = get_user_data(user_id)
    if not user_data:
        user_data = {"user_id": user_id, "preferences": {}}
        save_user_data(user_data)

    # Send welcome message
    welcome_message = f"Hello, {user.first_name}! Welcome to {BOT_NAME}, your personal music bot."
    await update.message.reply_text(welcome_message)

# Info Command
async def info(update: Update, context: CallbackContext):
    """Send bot information when the /info command is used."""
    info_message = (
        f"Welcome to {BOT_NAME}!\n\n"
        "I am your personal music bot that lets you play music in Telegram voice chats.\n"
        "🎵 *Features:*\n"
        "- High-quality voice chat streaming\n"
        "- Lyrics sync in real-time\n"
        "- Custom playlists\n"
        "- Admin-only mode\n"
        "- Voting system for song skipping\n\n"
        "Use /help to see available commands."
    )
    await update.message.reply_text(info_message, parse_mode="Markdown")

# Help Command
async def help_command(update: Update, context: CallbackContext):
    """Send the help message when the /help command is used."""
    help_message = (
        "Here are the available commands:\n\n"
        "🎵 *Music Commands:*\n"
        "/play <song name> - Play a song in the voice chat\n"
        "/pause - Pause the song\n"
        "/resume - Resume the song\n"
        "/skip - Skip to the next song\n"
        "/stop - Stop the music and leave the voice chat\n"
        "/queue - View the song queue\n"
        "/lyrics - Get the lyrics for the current song\n"
        "/sync_lyrics - Sync lyrics with the song\n\n"
        "⚙️ *Admin Commands:*\n"
        "/toggle_lyrics_sync - Toggle lyrics sync feature (Admins only)\n"
        "/skip_song - Skip a song (Admins only)\n"
        "/manage_playlists - Manage playlists (Admins only)\n\n"
        "For more information, type /info."
    )
    await update.message.reply_text(help_message, parse_mode="Markdown")

# Queue Command
async def queue(update: Update, context: CallbackContext):
    """Show the current song queue."""
    chat_id = update.message.chat_id
    song_queue = get_queue(chat_id)

    if song_queue:
        queue_message = "🎶 *Current Song Queue:*\n"
        for index, song in enumerate(song_queue, 1):
            queue_message += f"{index}. {song['title']} by {song['artist']}\n"
    else:
        queue_message = "🚫 The song queue is empty. Use /play to add songs."
    
    await update.message.reply_text(queue_message, parse_mode="Markdown")

# Stop Command
async def stop(update: Update, context: CallbackContext):
    """Stop the music and disconnect the bot from the voice chat."""
    chat_id = update.message.chat_id
    await music_player.stop_music(chat_id)
    await update.message.reply_text("⏹ Music stopped. Leaving the voice chat.")

# Current Song Command
async def current_song(update: Update, context: CallbackContext):
    """Show details of the currently playing song."""
    chat_id = update.message.chat_id
    current_song_details = await music_player.get_current_song(chat_id)

    if current_song_details:
        song_info = (
            f"🎵 *Currently Playing:*\n"
            f"🎶 Song: {current_song_details['title']}\n"
            f"🎤 Artist: {current_song_details['artist']}\n"
            f"⏳ Duration: {current_song_details['duration']}"
        )
    else:
        song_info = "🚫 No song is currently playing."
    
    await update.message.reply_text(song_info, parse_mode="Markdown")

# Lyrics Command
async def lyrics(update: Update, context: CallbackContext):
    """Fetch and display lyrics for the current song."""
    chat_id = update.message.chat_id
    current_song = await music_player.get_current_song(chat_id)

    if current_song:
        song_name = current_song['title']
        lyrics_text = get_lyrics_for_song(song_name)
        
        if lyrics_text:
            lyrics_message = f"🎵 *Lyrics for {song_name}:*\n\n{lyrics_text}"
        else:
            lyrics_message = "Lyrics not found for this song."
    else:
        lyrics_message = "No song is currently playing."
    
    await update.message.reply_text(lyrics_message, parse_mode="Markdown")

# Add command handlers to the bot
def add_command_handlers(dispatcher):
    """Add all command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("queue", queue))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("current_song", current_song))
    dispatcher.add_handler(CommandHandler("lyrics", lyrics))