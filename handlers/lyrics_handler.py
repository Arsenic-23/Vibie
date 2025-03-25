import json
import os
import time
import logging
from telegram import Update, ChatMember
from telegram.ext import CommandHandler, CallbackContext, JobQueue
from utils.player import MusicPlayer
from lyrics.lyrics_data import get_lyrics_for_song
from database.playlist_data import get_current_song

# Initialize the music player
music_player = MusicPlayer()

# Path to store lyrics sync state
LYRICS_SYNC_STATE_PATH = "cache/lyrics_sync_state.json"

# Configure logging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Function to fetch lyrics for the currently playing song
def fetch_lyrics(song_name):
    """Fetch lyrics for the given song."""
    lyrics = get_lyrics_for_song(song_name)
    return lyrics if lyrics else "Lyrics not found."

# Function to sync lyrics with the song
def sync_lyrics(update: Update, context: CallbackContext):
    """Synchronize lyrics with the currently playing song."""
    chat_id = update.effective_chat.id
    current_song = get_current_song(chat_id)

    if current_song:
        song_name = current_song["title"]
        lyrics = fetch_lyrics(song_name)

        # Send lyrics in a formatted way
        update.message.reply_text(f"🎵 *Lyrics for {song_name}:*\n\n{lyrics}", parse_mode="Markdown")
    else:
        update.message.reply_text("🚫 No song is currently playing.")

# Function to show lyrics in sync with song (non-blocking)
def show_lyrics_in_chat(update: Update, context: CallbackContext):
    """Send lyrics line-by-line in sync with the song."""
    chat_id = update.effective_chat.id
    current_song = get_current_song(chat_id)

    if current_song:
        song_name = current_song["title"]
        lyrics = fetch_lyrics(song_name)

        if lyrics == "Lyrics not found.":
            update.message.reply_text("🚫 Lyrics not found for this song.")
            return

        lyrics_lines = lyrics.split("\n")

        # Use job queue to send lyrics at intervals
        for i, line in enumerate(lyrics_lines):
            context.job_queue.run_once(send_lyrics_line, i * 10, context={"chat_id": chat_id, "line": line})
    else:
        update.message.reply_text("🚫 No song is currently playing.")

def send_lyrics_line(context: CallbackContext):
    """Send a single line of lyrics in the chat."""
    job_data = context.job.context
    chat_id = job_data["chat_id"]
    line = job_data["line"]

    context.bot.send_message(chat_id, text=line)

# Admin command to enable or disable lyrics sync
def toggle_lyrics_sync(update: Update, context: CallbackContext):
    """Admin command to toggle lyrics sync with song."""
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id

    # Check if the user is an admin
    if user_id in get_admins(update):
        new_state = toggle_lyrics_sync_state(chat_id)
        update.message.reply_text(f"✅ Lyrics sync is now {'enabled' if new_state else 'disabled'}.")
    else:
        update.message.reply_text("❌ You are not authorized to use this command.")

# Function to manage sync state
def toggle_lyrics_sync_state(chat_id):
    """Enable or disable lyrics sync for the chat."""
    state_file = LYRICS_SYNC_STATE_PATH

    # Load or create state file
    if os.path.exists(state_file):
        with open(state_file, "r") as file:
            try:
                state = json.load(file)
            except json.JSONDecodeError:
                state = {}
    else:
        state = {}

    # Toggle state
    new_state = not state.get(str(chat_id), False)
    state[str(chat_id)] = new_state

    with open(state_file, "w") as file:
        json.dump(state, file, indent=4)

    return new_state

# Function to get admin IDs dynamically
def get_admins(update: Update):
    """Return a list of admin user IDs for the chat."""
    chat = update.effective_chat
    bot = update.effective_user.bot

    try:
        admins = [admin.user.id for admin in chat.get_administrators()]
        return admins
    except Exception as e:
        logger.error(f"Error fetching admins: {e}")
        return []

# Add the lyrics sync handler to the bot
def add_lyrics_handlers(dispatcher):
    """Add lyrics-related command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("sync_lyrics", sync_lyrics))
    dispatcher.add_handler(CommandHandler("show_lyrics_in_chat", show_lyrics_in_chat))
    dispatcher.add_handler(CommandHandler("toggle_lyrics_sync", toggle_lyrics_sync))