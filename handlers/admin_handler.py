import logging
from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from utils.player import MusicPlayer
from database import playlist_data

# Initialize the music player
music_player = MusicPlayer()

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Skip song command (admin only)
def skip_song(update: Update, context: CallbackContext):
    """Admin-only command to skip the current song."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    # Check if the user is an admin (you can implement more specific admin checks)
    if user_id in playlist_data.get_admins(chat_id):
        if music_player.skip(chat_id):
            update.message.reply_text("Song skipped!")
        else:
            update.message.reply_text("No more songs in the queue.")
    else:
        update.message.reply_text("You are not authorized to skip songs.")

# Add song to playlist command (admin only)
def add_to_playlist(update: Update, context: CallbackContext):
    """Admin-only command to add a song to the playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in playlist_data.get_admins(chat_id):
        song_name = " ".join(context.args)
        if song_name:
            playlist_data.add_song_to_playlist(chat_id, song_name)
            update.message.reply_text(f"Added {song_name} to the playlist.")
        else:
            update.message.reply_text("Please provide a song name.")
    else:
        update.message.reply_text("You are not authorized to add songs to the playlist.")

# Remove song from playlist command (admin only)
def remove_from_playlist(update: Update, context: CallbackContext):
    """Admin-only command to remove a song from the playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in playlist_data.get_admins(chat_id):
        song_name = " ".join(context.args)
        if song_name:
            if playlist_data.remove_song_from_playlist(chat_id, song_name):
                update.message.reply_text(f"Removed {song_name} from the playlist.")
            else:
                update.message.reply_text(f"Song {song_name} not found in the playlist.")
        else:
            update.message.reply_text("Please provide a song name.")
    else:
        update.message.reply_text("You are not authorized to remove songs from the playlist.")

# Set playlist as the active one (admin only)
def set_active_playlist(update: Update, context: CallbackContext):
    """Admin-only command to set the active playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in playlist_data.get_admins(chat_id):
        playlist_name = " ".join(context.args)
        if playlist_name:
            if playlist_data.set_active_playlist(chat_id, playlist_name):
                update.message.reply_text(f"Activated the playlist {playlist_name}.")
            else:
                update.message.reply_text(f"Playlist {playlist_name} not found.")
        else:
            update.message.reply_text("Please provide a playlist name.")
    else:
        update.message.reply_text("You are not authorized to set the active playlist.")

# View playlist command (admin only)
def view_playlist(update: Update, context: CallbackContext):
    """Admin-only command to view the current playlist."""
    chat_id = update.message.chat_id
    user_id = update.message.from_user.id

    if user_id in playlist_data.get_admins(chat_id):
        playlist = playlist_data.get_playlist(chat_id)
        if playlist:
            playlist_text = "\n".join([f"{idx + 1}. {song}" for idx, song in enumerate(playlist)])
            update.message.reply_text(f"Current Playlist:\n{playlist_text}")
        else:
            update.message.reply_text("The playlist is empty.")
    else:
        update.message.reply_text("You are not authorized to view the playlist.")

# Admin help command
def admin_help(update: Update, context: CallbackContext):
    """Admin command to display a list of admin-specific commands."""
    help_text = (
        "/skip - Skip the current song\n"
        "/add_to_playlist [song_name] - Add a song to the playlist\n"
        "/remove_from_playlist [song_name] - Remove a song from the playlist\n"
        "/set_active_playlist [playlist_name] - Set the active playlist\n"
        "/view_playlist - View the current playlist"
    )
    update.message.reply_text(help_text)

# Add admin commands to dispatcher
def add_admin_handlers(dispatcher):
    """Add admin-related command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("skip", skip_song))
    dispatcher.add_handler(CommandHandler("add_to_playlist", add_to_playlist))
    dispatcher.add_handler(CommandHandler("remove_from_playlist", remove_from_playlist))
    dispatcher.add_handler(CommandHandler("set_active_playlist", set_active_playlist))
    dispatcher.add_handler(CommandHandler("view_playlist", view_playlist))
    dispatcher.add_handler(CommandHandler("admin_help", admin_help))