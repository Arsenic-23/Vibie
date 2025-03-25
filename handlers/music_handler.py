import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext, ContextTypes
from utils.player import play_audio, stop_audio, pause_audio, resume_audio, skip_audio
from utils.downloader import MusicDownloader

# Initialize the downloader
music_downloader = MusicDownloader()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Play a song in the Telegram voice chat using PyTgCalls."""
    chat_id = update.message.chat_id

    if not context.args:
        await update.message.reply_text("❌ Please provide a song name or link.")
        return

    song_name = " ".join(context.args)

    # Download the song
    try:
        song_file = await music_downloader.download(song_name)  # Ensure download function supports async
        if song_file:
            await play_audio(chat_id, song_file)
            await update.message.reply_text(f"🎵 Now playing: *{song_name}*", parse_mode="Markdown")
        else:
            await update.message.reply_text("🚫 Could not find the song. Please try again.")
    except Exception as e:
        logger.error(f"Error downloading/playing song: {e}")
        await update.message.reply_text("❌ An error occurred while trying to play the song.")

async def pause(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Pause the currently playing song."""
    chat_id = update.message.chat_id
    try:
        await pause_audio(chat_id)
        await update.message.reply_text("⏸ Music paused.")
    except Exception as e:
        logger.error(f"Error pausing audio: {e}")
        await update.message.reply_text("❌ Could not pause the music.")

async def resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Resume the paused song."""
    chat_id = update.message.chat_id
    try:
        await resume_audio(chat_id)
        await update.message.reply_text("▶ Music resumed.")
    except Exception as e:
        logger.error(f"Error resuming audio: {e}")
        await update.message.reply_text("❌ Could not resume the music.")

async def skip(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Skip the current song."""
    chat_id = update.message.chat_id
    try:
        await skip_audio(chat_id)
        await update.message.reply_text("⏭ Song skipped!")
    except Exception as e:
        logger.error(f"Error skipping audio: {e}")
        await update.message.reply_text("❌ Could not skip the song.")

async def stop(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Stop the currently playing music."""
    chat_id = update.message.chat_id
    try:
        await stop_audio(chat_id)
        await update.message.reply_text("⏹ Music stopped.")
    except Exception as e:
        logger.error(f"Error stopping audio: {e}")
        await update.message.reply_text("❌ Could not stop the music.")

# Add the music handlers to the bot
def add_music_handlers(dispatcher):
    """Add music command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("play", play))
    dispatcher.add_handler(CommandHandler("pause", pause))
    dispatcher.add_handler(CommandHandler("resume", resume))
    dispatcher.add_handler(CommandHandler("skip", skip))
    dispatcher.add_handler(CommandHandler("stop", stop))  # Added stop command