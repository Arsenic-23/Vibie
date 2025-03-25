import os

# Telegram Bot Configuration
API_TOKEN = "7575567291:AAH8yaPhRofVfAFrDPiEqddelnqszgQ5Ru8"  # Replace with your Telegram Bot API token

# Admins and Authorized Users
ADMINS = [123456789, 987654321]  # Replace with your admin user IDs
AUTHORIZED_USERS = [123456789]  # Replace with authorized users for playlist management

# Music Configuration
MUSIC_DIR = "music"  # Directory for storing downloaded music files
CACHE_DIR = "cache"   # Temporary cache for ongoing music streams

# YouTube Download Configuration (for downloading music)
YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': MUSIC_DIR + '/%(id)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'quiet': True
}

# FFmpeg Configuration (for playing music)
FFMPEG_BIN = "/usr/bin/ffmpeg"  # Path to FFmpeg binary, adjust if necessary

# MPV Player Configuration
MPV_BIN = "/usr/bin/mpv"  # Path to MPV player binary, adjust if necessary

# Lyrics Sync Configuration
LYRICS_SYNC = True  # Set to True to enable lyrics sync

# Bot Settings
BOT_NAME = "Vibie"
LOGGING_LEVEL = "INFO"  # Options: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = "bot.log"  # Log file for the bot

# Spotify/YouTube API Keys (for fetching songs and lyrics)
SPOTIFY_API_KEY = "YOUR_SPOTIFY_API_KEY"  # Replace with your Spotify API key
YOUTUBE_API_KEY = "YOUR_YOUTUBE_API_KEY"  # Replace with your YouTube API key

# Enable/Disable Features
ENABLE_LYRICS = True  # Set to False if you don't want lyrics features
ENABLE_PLAYLIST = True  # Set to False if you don't want playlist management
ENABLE_VOTING = True  # Enable/disable song voting system

# Bot Polling and Server Settings
POLLING_INTERVAL = 5  # Time in seconds between each polling request
MAX_PLAYLIST_LENGTH = 50  # Max number of songs allowed in a playlist

# Other Configurations
SONG_THUMBNAILS_DIR = "assets/song_thumbnails"  # Directory to store song thumbnails
LYRICS_DATA_FILE = "lyrics/lyrics_data.json"  # Lyrics data storage file
PLAYLIST_DATA_FILE = "database/playlist_data.json"  # Playlist data file
USER_DATA_FILE = "database/user_data.json"  # User data storage file