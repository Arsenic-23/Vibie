import os
from pyrogram import Client
from pytgcalls import PyTgCalls

# --- TELEGRAM API CONFIGURATION ---
API_ID = int(os.getenv("API_ID", 123456))  # Replace with actual API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with actual API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")  # Replace with actual Bot Token

# --- BOT & USER PERMISSIONS ---
ADMINS = list(map(int, os.getenv("ADMINS", "7212032106").split()))  # Admins as list
AUTHORIZED_USERS = list(map(int, os.getenv("AUTHORIZED_USERS", "123456789").split()))  # Authorized users list

# --- PYROGRAM & PYTGCALL CLIENTS ---
app = Client("VibieMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# --- MUSIC & STREAMING SETTINGS ---
MUSIC_DIR = "music"  # Directory for storing downloaded music files
CACHE_DIR = "cache"   # Temporary cache for ongoing music streams

# --- YOUTUBE MUSIC DOWNLOAD CONFIGURATION ---
YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': os.path.join(MUSIC_DIR, '%(id)s.%(ext)s'),
    'restrictfilenames': True,
    'noplaylist': True,
    'quiet': True
}

# --- BOT FEATURES CONFIGURATION ---
LYRICS_SYNC = os.getenv("LYRICS_SYNC", "True") == "True"  # Set to True to enable lyrics sync
ENABLE_LYRICS = os.getenv("ENABLE_LYRICS", "True") == "True"  # Enable/Disable lyrics feature
ENABLE_PLAYLIST = os.getenv("ENABLE_PLAYLIST", "True") == "True"  # Enable/Disable playlist management
ENABLE_VOTING = os.getenv("ENABLE_VOTING", "True") == "True"  # Enable/Disable song voting system

# --- BOT POLLING & SETTINGS ---
POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 5))  # Time in seconds between polling requests
MAX_PLAYLIST_LENGTH = int(os.getenv("MAX_PLAYLIST_LENGTH", 50))  # Max playlist length

# --- LOGGING CONFIGURATION ---
BOT_NAME = "Vibie"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "bot.log"  # Log file for the bot

# --- SPOTIFY/YOUTUBE API KEYS (OPTIONAL) ---
SPOTIFY_API_KEY = os.getenv("SPOTIFY_API_KEY", "your_spotify_api_key_here")  # Spotify API key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "your_youtube_api_key_here")  # YouTube API key

# --- FILE STORAGE CONFIGURATION ---
SONG_THUMBNAILS_DIR = "assets/song_thumbnails"  # Directory to store song thumbnails
LYRICS_DATA_FILE = "lyrics/lyrics_data.json"  # Lyrics data storage file
PLAYLIST_DATA_FILE = "database/playlist_data.json"  # Playlist data file
USER_DATA_FILE = "database/user_data.json"  # User data storage file