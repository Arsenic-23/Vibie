import logging
from telegram import Update
from telegram.ext import CallbackContext
from utils.player import play_audio, stop_audio, pause_audio, resume_audio, skip_audio
from utils.downloader import MusicDownloader

# Initialize the downloader
music_downloader = MusicDownloader()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def play(update: Update, context: CallbackContext):
    """Play a song in the Telegram voice chat using PyTgCalls."""
    chat_id = update.message.chat_id
    song_name = " ".join(context.args)

    if not song_name:
        await update.message.reply_text("Please provide a song name or link.")
        return

    # Download the song
    song_file = music_downloader.download(song_name)
    
    if song_file:
        await play_audio(chat_id, song_file)
        await update.message.reply_text(f"Now playing: {song_name}")
    else:
        await update.message.reply_text("Could not find the song. Please try again.")

async def pause(update: Update, context: CallbackContext):
    """Pause the currently playing song."""
    chat_id = update.message.chat_id
    await pause_audio(chat_id)
    await update.message.reply_text("Music paused.")

async def resume(update: Update, context: CallbackContext):
    """Resume the paused song."""
    chat_id = update.message.chat_id
    await resume_audio(chat_id)
    await update.message.reply_text("Music resumed.")

async def skip(update: Update, context: CallbackContext):
    """Skip the current song and stop playback."""
    chat_id = update.message.chat_id
    await skip_audio(chat_id)
    await update.message.reply_text("Song skipped!")