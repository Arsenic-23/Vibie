import os

API_ID = os.getenv("API_ID")  # Set in Railway Environment Variables
API_HASH = os.getenv("API_HASH")  # Set in Railway Environment Variables
BOT_TOKEN = os.getenv("BOT_TOKEN")  # Set in Railway Environment Variables
OWNER_ID = int(os.getenv("OWNER_ID", 0))  # Set in Railway Environment Variables

MUSIC_QUALITY = "high"  # Options: low, medium, high
AUTO_RESTART = True  # Auto-restart bot on crash

# Database (for playlists, user settings)
DB_URL = os.getenv("DB_URL", None)  # Optional database for storing playlists

# Admin & Auth Users
AUTH_USERS = [OWNER_ID]  # Add user IDs who can control the bot
BANNED_USERS = []  # Users who are banned from using the bot

# AI Features
ENABLE_AI_JUKEBOX = True  # AI-based song recommendations
ENABLE_VOICE_COMMANDS = True  # Hands-free control via voice