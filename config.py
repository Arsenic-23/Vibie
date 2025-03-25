import os
from pyrogram import Client
from pytgcalls import PyTgCalls

# --- TELEGRAM API CONFIGURATION ---
API_ID = 123456  # Replace with your API ID from my.telegram.org
API_HASH = "your_api_hash"  # Replace with your API Hash from my.telegram.org
API_TOKEN = "your_bot_token_here"  # Replace with your Telegram Bot API token

# --- BOT & USER PERMISSIONS ---
ADMINS = [7212032106]  # Replace with your admin user IDs
AUTHORIZED_USERS = [123456789]  # Replace with authorized users for playlist management

# --- PYROGRAM & PYTGCALL CLIENTS ---
app = Client("VibieMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=API_TOKEN)
pytgcalls = PyTgCalls(app)

# --- MUSIC & STREAMING SETTINGS ---
MUSIC_DIR = "music"  # Directory for storing downloaded music files
CACHE_DIR = "cache"   # Temporary cache for ongoing music streams

# --- YOUTUBE MUSIC DOWNLOAD CONFIGURATION ---
YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': MUSIC_DIR + '/%(id)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'quiet': True
}

# --- BOT FEATURES CONFIGURATION ---
LYRICS_SYNC = True  # Set to True to enable lyrics sync
ENABLE_LYRICS = True  # Enable/Disable lyrics feature
ENABLE_PLAYLIST = True  # Enable/Disable playlist management
ENABLE_VOTING = True  # Enable/Disable song voting system

# --- BOT POLLING & SETTINGS ---
POLLING_INTERVAL = 5  # Time in seconds between each polling request
MAX_PLAYLIST_LENGTH = 50  # Max number of songs allowed in a playlist

# --- LOGGING CONFIGURATION ---
BOT_NAME = "Vibie"
LOGGING_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "bot.log"  # Log file for the bot

# --- SPOTIFY/YOUTUBE API KEYS (OPTIONAL) ---
SPOTIFY_API_KEY = "your_spotify_api_key_here"  # Replace with your Spotify API key
YOUTUBE_API_KEY = "your_youtube_api_key_here"  # Replace with your YouTube API key

# --- FILE STORAGE CONFIGURATION ---
SONG_THUMBNAILS_DIR = "assets/song_thumbnails"  # Directory to store song thumbnails
LYRICS_DATA_FILE = "lyrics/lyrics_data.json"  # Lyrics data storage file
PLAYLIST_DATA_FILE = "database/playlist_data.json"  # Playlist data file
USER_DATA_FILE = "database/user_data.json"  # User data storage file