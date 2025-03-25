import json
import os
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.player import MusicPlayer
from lyrics.lyrics_data import get_lyrics_for_song
from database.playlist_data import get_current_song

# Initialize the music player
music_player = MusicPlayer()

# Path to store lyrics data
LYRICS_PATH = "lyrics/lyrics_data.json"

# Function to fetch lyrics for the currently playing song
def fetch_lyrics(song_name):
    """Fetch lyrics for the given song."""
    lyrics = get_lyrics_for_song(song_name)
    return lyrics if lyrics else "Lyrics not found."

# Function to sync lyrics with the song
def sync_lyrics(chat_id, update: Update, context: CallbackContext):
    """Synchronize lyrics with the currently playing song."""
    # Get the current song being played in the voice chat
    current_song = get_current_song(chat_id)
    
    if current_song:
        song_name = current_song['name']
        lyrics = fetch_lyrics(song_name)
        
        # Send the lyrics in a nice format
        update.message.reply_text(f"Lyrics for {song_name}:\n\n{lyrics}")
    else:
        update.message.reply_text("No song is currently playing.")

# Function to show lyrics in sync with song (advanced feature)
def show_lyrics_in_chat(chat_id, update: Update, context: CallbackContext):
    """Send lyrics in sync with the song at intervals."""
    current_song = get_current_song(chat_id)
    
    if current_song:
        song_name = current_song['name']
        lyrics = fetch_lyrics(song_name)
        
        # Example: You can split the lyrics into lines or segments
        lyrics_lines = lyrics.split("\n")
        
        # Sending lyrics in intervals (example: 1 line every 10 seconds)
        for line in lyrics_lines:
            update.message.reply_text(line)
            time.sleep(10)  # Wait 10 seconds before sending the next line
    else:
        update.message.reply_text("No song is currently playing.")

# Admin command to enable or disable lyrics sync
def toggle_lyrics_sync(update: Update, context: CallbackContext):
    """Admin command to toggle lyrics sync with song."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    # Check if the user is an admin
    if user_id in get_admins(chat_id):
        # Toggle functionality (for example: store state in a database or a variable)
        if toggle_lyrics_sync_state(chat_id):
            update.message.reply_text("Lyrics sync is now enabled.")
        else:
            update.message.reply_text("Lyrics sync is now disabled.")
    else:
        update.message.reply_text("You are not authorized to use this command.")

# Function to manage sync state
def toggle_lyrics_sync_state(chat_id):
    """Enable or disable lyrics sync for the chat."""
    # This could be stored in a database or a config file
    state_file = f"cache/lyrics_sync_{chat_id}.json"
    
    if os.path.exists(state_file):
        with open(state_file, 'r') as file:
            state = json.load(file)
        
        # Toggle state
        new_state = not state.get("enabled", False)
        
        # Save the new state
        with open(state_file, 'w') as file:
            json.dump({"enabled": new_state}, file)
        
        return new_state
    else:
        # Create default state if it doesn't exist
        with open(state_file, 'w') as file:
            json.dump({"enabled": True}, file)
        
        return True

# Function to get admin IDs (can be implemented in a database file)
def get_admins(chat_id):
    """Return a list of admin user IDs for the given chat."""
    # This should fetch admins from a database or config file
    return [123456789, 987654321]  # Example admin user IDs

# Add the lyrics sync handler to the bot
def add_lyrics_handlers(dispatcher):
    """Add lyrics-related command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("sync_lyrics", sync_lyrics))
    dispatcher.add_handler(CommandHandler("show_lyrics_in_chat", show_lyrics_in_chat))
    dispatcher.add_handler(CommandHandler("toggle_lyrics_sync", toggle_lyrics_sync))