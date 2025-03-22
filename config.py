import os

# Telegram API credentials
API_ID = int(os.getenv("API_ID", 0))  # Default to 0 if not provided
API_HASH = os.getenv("API_HASH")  # No default placeholder

# Bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN")  # No default placeholder

# OpenAI API Key (for AI chat features)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # No default placeholder

# MongoDB connection (for storing user data, playlists, etc.)
MONGO_URI = os.getenv("MONGO_URI")  # No default placeholder

# Authorized users (Admin List)
AUTH_USERS = list(map(int, os.getenv("AUTH_USERS", "").split(","))) if os.getenv("AUTH_USERS") else []

# Music settings
MAX_QUEUE_SIZE = int(os.getenv("MAX_QUEUE_SIZE", 50))  # Ensure it's an integer

# Logging (for debugging)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").strip().lower() == "true"

def is_admin(user_id):
    """Check if a user is an admin."""
    return user_id in AUTH_USERS  # Uses dynamic list instead of hardcoded values