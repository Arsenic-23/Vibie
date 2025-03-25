from telegram import Update
from telegram.ext import CommandHandler, CallbackContext
from database.user_data import get_user_data, save_user_data
from config import BOT_NAME


# Command for starting the bot
def start(update: Update, context: CallbackContext):
    """Send a welcome message when the /start command is used."""
    user = update.message.from_user
    user_id = user.id
    
    # Get or create user data
    user_data = get_user_data(user_id)
    if not user_data:
        user_data = {"user_id": user_id, "preferences": {}}
        save_user_data(user_data)
    
    # Send welcome message
    welcome_message = f"Hello, {user.first_name}! Welcome to {BOT_NAME}, your personal music bot."
    update.message.reply_text(welcome_message)


# Command to show bot information
def info(update: Update, context: CallbackContext):
    """Send bot information when the /info command is used."""
    info_message = (
        f"Welcome to {BOT_NAME}!\n\n"
        "I am your personal music bot that lets you play music in Telegram voice chats.\n"
        "Commands available:\n"
        "/start - Start interacting with the bot\n"
        "/help - Get a list of all commands\n"
        "/info - Get information about the bot\n"
        "/sync_lyrics - Sync lyrics with the song playing in the voice chat\n"
        "/toggle_lyrics_sync - Enable or disable lyrics sync (Admin only)"
    )
    update.message.reply_text(info_message)


# Command to display help information
def help_command(update: Update, context: CallbackContext):
    """Send the help message when the /help command is used."""
    help_message = (
        "Here are the available commands:\n\n"
        "Music Commands:\n"
        "/play <song name> - Play a song in the voice chat\n"
        "/pause - Pause the song\n"
        "/skip - Skip to the next song\n"
        "/stop - Stop the music and leave the voice chat\n"
        "/queue - View the song queue\n"
        "/lyrics - Get the lyrics for the current song\n"
        "/sync_lyrics - Sync lyrics with the song\n\n"
        "Admin Commands:\n"
        "/toggle_lyrics_sync - Toggle lyrics sync feature (Admins only)\n"
        "/skip_song - Skip a song (Admins only)\n"
        "/manage_playlists - Manage playlists (Admins only)\n\n"
        "For more information, type /info."
    )
    update.message.reply_text(help_message)


# Command to show the bot's current song queue
def queue(update: Update, context: CallbackContext):
    """Show the current song queue."""
    user_id = update.message.from_user.id
    # Retrieve playlist or queue from the database (to be implemented)
    # Assuming `get_queue_for_user` fetches the current song queue
    song_queue = get_queue_for_user(user_id)
    
    if song_queue:
        queue_message = "Current Song Queue:\n"
        for index, song in enumerate(song_queue, 1):
            queue_message += f"{index}. {song['title']} by {song['artist']}\n"
    else:
        queue_message = "The song queue is empty. Use /play to add songs."
    
    update.message.reply_text(queue_message)


# Command to stop the music and remove bot from voice chat
def stop(update: Update, context: CallbackContext):
    """Stop the music and disconnect the bot from the voice chat."""
    user_id = update.message.from_user.id
    # Stop music function needs to be implemented in player.py
    music_player.stop_music(update.message.chat_id)
    update.message.reply_text("Music stopped and I am leaving the voice chat.")


# Command to show current song details
def current_song(update: Update, context: CallbackContext):
    """Show details of the currently playing song."""
    user_id = update.message.from_user.id
    # Retrieve current song details (implemented in player.py)
    current_song_details = music_player.get_current_song(update.message.chat_id)
    
    if current_song_details:
        song_info = (
            f"Currently playing:\n"
            f"Song: {current_song_details['title']}\n"
            f"Artist: {current_song_details['artist']}\n"
            f"Duration: {current_song_details['duration']}"
        )
    else:
        song_info = "No song is currently playing."
    
    update.message.reply_text(song_info)


# Function to get the user's data (this will be used to track preferences, etc.)
def get_user_data(user_id):
    """Get user data from the database."""
    try:
        with open(f"database/user_data.json", "r") as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {}

    return users_data.get(str(user_id))


# Function to save user data
def save_user_data(user_data):
    """Save user data to the database."""
    try:
        with open(f"database/user_data.json", "r") as file:
            users_data = json.load(file)
    except FileNotFoundError:
        users_data = {}

    users_data[str(user_data["user_id"])] = user_data

    with open(f"database/user_data.json", "w") as file:
        json.dump(users_data, file, indent=4)


# Add the command handlers to the bot
def add_command_handlers(dispatcher):
    """Add all command handlers to the dispatcher."""
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("info", info))
    dispatcher.add_handler(CommandHandler("queue", queue))
    dispatcher.add_handler(CommandHandler("stop", stop))
    dispatcher.add_handler(CommandHandler("current_song", current_song))