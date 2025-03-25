import os
import logging
from telegram import Update, ParseMode
from telegram.ext import CommandHandler, CallbackContext
from utils.player import MusicPlayer
from utils.downloader import MusicDownloader
from config import BOT_TOKEN
from database import playlist_data

# Initialize the music player and downloader
music_player = MusicPlayer()
music_downloader = MusicDownloader()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Play music command
def play(update: Update, context: CallbackContext):
    """Play a song in the voice chat."""
    chat_id = update.message.chat_id
    song_name = " ".join(context.args)

    if not song_name:
        update.message.reply_text("Please provide the song name or link.")
        return

    # Download the song if not already downloaded
    song_file = music_downloader.download(song_name)
    
    if song_file:
        # Add song to the queue
        music_player.add_to_queue(song_file)
        music_player.play(chat_id, song_file)
        update.message.reply_text(f"Now playing: {song_name}")
    else:
        update.message.reply_text("Could not find the song. Please try again.")

# Pause music command
def pause(update: Update, context: CallbackContext):
    """Pause the currently playing song."""
    chat_id = update.message.chat_id
    if music_player.is_playing(chat_id):
        music_player.pause(chat_id)
        update.message.reply_text("Music paused.")
    else:
        update.message.reply_text("No music is currently playing.")

# Resume music command
def resume(update: Update, context: CallbackContext):
    """Resume the paused song."""
    chat_id = update.message.chat_id
    if not music_player.is_playing(chat_id):
        music_player.resume(chat_id)
        update.message.reply_text("Music resumed.")
    else:
        update.message.reply_text("The music is already playing.")

# Skip music command
def skip(update: Update, context: CallbackContext):
    """Skip the current song and play the next in the queue."""
    chat_id = update.message.chat_id
    if music_player.skip(chat_id):
        update.message.reply_text("Song skipped!")
    else:
        update.message.reply_text("No more songs in the queue.")

# Show current queue command
def queue(update: Update, context: CallbackContext):
    """Show the current song queue."""
    chat_id = update.message.chat_id
    queue = music_player.get_queue(chat_id)
    if queue:
        queue_text = "\n".join([f"{idx + 1}. {song}" for idx, song in enumerate(queue)])
        update.message.reply_text(f"Current Queue:\n{queue_text}")
    else:
        update.message.reply_text("The queue is currently empty.")

# Volume control command
def volume(update: Update, context: CallbackContext):
    """Set the volume for music playback."""
    chat_id = update.message.chat_id
    if context.args:
        try:
            volume_level = int(context.args[0])
            if 0 <= volume_level <= 100:
                music_player.set_volume(chat_id, volume_level)
                update.message.reply_text(f"Volume set to {volume_level}%.")
            else:
                update.message.reply_text("Please provide a volume level between 0 and 100.")
        except ValueError:
            update.message.reply_text("Please provide a valid volume level (0-100).")
    else:
        update.message.reply_text("Please provide a volume level (0-100).")

# Lyrics sync command
def lyrics(update: Update, context: CallbackContext):
    """Show lyrics for the current song."""
    chat_id = update.message.chat_id
    current_song = music_player.get_current_song(chat_id)
    
    if current_song:
        lyrics = music_player.get_lyrics(current_song)
        if lyrics:
            update.message.reply_text(lyrics, parse_mode=ParseMode.MARKDOWN)
        else:
            update.message.reply_text("Lyrics not found for this song.")
    else:
        update.message.reply_text("No song is currently playing.")

# Help command
def help_command(update: Update, context: CallbackContext):
    """Provide a list of available commands."""
    help_text = (
        "/play [song_name or URL] - Play a song\n"
        "/pause - Pause the current song\n"
        "/resume - Resume the paused song\n"
        "/skip - Skip to the next song\n"
        "/queue - View the current song queue\n"
        "/volume [level] - Adjust the volume\n"
        "/lyrics - View the lyrics of the current song"
    )
    update.message.reply_text(help_text)

# Add handlers to dispatcher
def add_music_handlers(dispatcher):
    """Add music-related command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("pause", pause))
    dispatcher.add_handler(CommandHandler("resume", resume))
    dispatcher.add_handler(CommandHandler("skip", skip))
    dispatcher.add_handler(CommandHandler("queue", queue))
    dispatcher.add_handler(CommandHandler("volume", volume))
    dispatcher.add_handler(CommandHandler("lyrics", lyrics))
    dispatcher.add_handler(CommandHandler("help", help_command))