import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if exists)
load_dotenv()

# Telegram API credentials
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your API Hash

# Bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# OpenAI API Key (for AI chat features)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# MongoDB connection (for storing user data, playlists, etc.)
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri")

# Authorized users (Admin List)
AUTH_USERS = [int(user) for user in os.getenv("AUTH_USERS", "").split() if user.isdigit()]

# Music settings
MAX_QUEUE_SIZE = 50  # Max number of songs in the queue per chat

# Logging (for debugging)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

def is_admin(user_id):
    """Check if a user is an admin."""
    admin_ids = [123456789]  # Add your admin user IDs
    return user_id in admin_ids
