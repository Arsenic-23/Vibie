import os

# Get API credentials from environment variables or set manually
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash_here")  # Replace with your API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token_here")  # Replace with your bot token

# MongoDB for storing user data and playlists
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri_here")

# Admins and authorized users
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  # Replace with your Telegram ID
AUTHORIZED_USERS = [OWNER_ID]  # List of users allowed to use admin commands

# Music settings
MUSIC_QUALITY = os.getenv("MUSIC_QUALITY", "high")  # Options: low, medium, high
MAX_QUEUE_LENGTH = int(os.getenv("MAX_QUEUE_LENGTH", "50"))  # Maximum songs in queue

# AI settings
AI_ENABLED = os.getenv("AI_ENABLED", "True").lower() == "true"  # Enable AI chat?
VOICE_EFFECTS_ENABLED = os.getenv("VOICE_EFFECTS_ENABLED", "True").lower() == "true"  # Enable voice filters?
DJ_MODE = os.getenv("DJ_MODE", "False").lower() == "true"  # Enable DJ fade transitions?

# Logging settings
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-100123456789"))  # Replace with your log channel ID
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Deployment settings
DEPLOYMENT = os.getenv("DEPLOYMENT", "koyeb")  # Options: koyeb, railway, local

# Function to check if a user is authorized
def is_authorized(user_id):
    return user_id in AUTHORIZED_USERS or user_id == OWNER_ID