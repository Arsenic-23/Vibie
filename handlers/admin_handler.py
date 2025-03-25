import logging
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from utils.player import MusicPlayer
from database.playlist_data import get_admins, add_song_to_playlist, remove_song_from_playlist, set_active_playlist, get_playlist

# Initialize the music player
music_player = MusicPlayer()

# Configure logging
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Skip song command (admin only)
async def skip_song(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin-only command to skip the current song."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in get_admins(chat_id):
        if music_player.skip(chat_id):
            await update.message.reply_text("🎵 Song skipped!")
        else:
            await update.message.reply_text("⚠️ No more songs in the queue.")
    else:
        await update.message.reply_text("❌ You are not authorized to skip songs.")

# Add song to playlist command (admin only)
async def add_to_playlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin-only command to add a song to the playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in get_admins(chat_id):
        song_name = " ".join(context.args)
        if song_name:
            add_song_to_playlist(chat_id, song_name)
            await update.message.reply_text(f"✅ Added **{song_name}** to the playlist.")
        else:
            await update.message.reply_text("⚠️ Please provide a song name.")
    else:
        await update.message.reply_text("❌ You are not authorized to add songs.")

# Remove song from playlist command (admin only)
async def remove_from_playlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin-only command to remove a song from the playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in get_admins(chat_id):
        song_name = " ".join(context.args)
        if song_name:
            if remove_song_from_playlist(chat_id, song_name):
                await update.message.reply_text(f"🗑 Removed **{song_name}** from the playlist.")
            else:
                await update.message.reply_text(f"⚠️ Song **{song_name}** not found in the playlist.")
        else:
            await update.message.reply_text("⚠️ Please provide a song name.")
    else:
        await update.message.reply_text("❌ You are not authorized to remove songs.")

# Set playlist as active
async def set_active_playlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin-only command to set the active playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in get_admins(chat_id):
        playlist_name = " ".join(context.args)
        if playlist_name:
            if set_active_playlist(chat_id, playlist_name):
                await update.message.reply_text(f"✅ Activated playlist: **{playlist_name}**")
            else:
                await update.message.reply_text(f"⚠️ Playlist **{playlist_name}** not found.")
        else:
            await update.message.reply_text("⚠️ Please provide a playlist name.")
    else:
        await update.message.reply_text("❌ You are not authorized to set the active playlist.")

# View current playlist
async def view_playlist(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin-only command to view the current playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in get_admins(chat_id):
        playlist = get_playlist(chat_id)
        if playlist:
            playlist_text = "\n".join([f"🎶 {idx + 1}. {song}" for idx, song in enumerate(playlist)])
            await update.message.reply_text(f"🎵 **Current Playlist:**\n{playlist_text}")
        else:
            await update.message.reply_text("📭 The playlist is empty.")
    else:
        await update.message.reply_text("❌ You are not authorized to view the playlist.")

# Admin help command
async def adminhelp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Admin command to display a list of admin-specific commands."""
    help_text = (
        "🎵 **Admin Commands:**\n"
        "/skip - Skip the current song\n"
        "/add_to_playlist [song_name] - Add a song to the playlist\n"
        "/remove_from_playlist [song_name] - Remove a song from the playlist\n"
        "/set_active_playlist [playlist_name] - Set the active playlist\n"
        "/view_playlist - View the current playlist"
    )
    await update.message.reply_text(help_text)

# Add admin commands to application
def add_admin_handlers(application):
    """Add admin-related command handlers to the bot."""
    application.add_handler(CommandHandler("skip", skip_song))
    application.add_handler(CommandHandler("add_to_playlist", add_to_playlist))
    application.add_handler(CommandHandler("remove_from_playlist", remove_from_playlist))
    application.add_handler(CommandHandler("set_active_playlist", set_active_playlist))
    application.add_handler(CommandHandler("view_playlist", view_playlist))
    application.add_handler(CommandHandler("adminhelp", adminhelp))