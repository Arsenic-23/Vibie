import os
from pyrogram import Client
from pytgcalls import PyTgCalls

API_ID = int(os.getenv("API_ID", 123456))  
API_HASH = os.getenv("API_HASH", "your_api_hash")  
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")  

ADMINS = list(map(int, os.getenv("ADMINS", "7212032106").split()))  
AUTHORIZED_USERS = list(map(int, os.getenv("AUTHORIZED_USERS", "123456789").split()))  

app = Client("VibieMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

MUSIC_DIR = "music"  
CACHE_DIR = "cache"   

YTDL_OPTIONS = {
    'format': 'bestaudio/best',
    'extractaudio': True,
    'outtmpl': os.path.join(MUSIC_DIR, '%(id)s.%(ext)s'),
    'restrictfilenames': True,
    'noplaylist': True,
    'quiet': True
}

LYRICS_SYNC = os.getenv("LYRICS_SYNC", "True") == "True"  
ENABLE_LYRICS = os.getenv("ENABLE_LYRICS", "True") == "True"  
ENABLE_PLAYLIST = os.getenv("ENABLE_PLAYLIST", "True") == "True"  
ENABLE_VOTING = os.getenv("ENABLE_VOTING", "True") == "True"  

POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 5))  
MAX_PLAYLIST_LENGTH = int(os.getenv("MAX_PLAYLIST_LENGTH", 50))  

BOT_NAME = "Vibie"
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", "INFO")  
LOG_FILE = "bot.log"  

SPOTIFY_API_KEY = os.getenv("SPOTIFY_API_KEY", "your_spotify_api_key_here")  
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "your_youtube_api_key_here")  

SONG_THUMBNAILS_DIR = "assets/song_thumbnails"  
LYRICS_DATA_FILE = "lyrics/lyrics_data.json"  
PLAYLIST_DATA_FILE = "database/playlist_data.json"  
USER_DATA_FILE = "database/user_data.json"