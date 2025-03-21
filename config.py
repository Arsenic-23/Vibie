import os
from dotenv import load_dotenv

# Load environment variables from a .env file (if exists)
load_dotenv()

# Telegram API credentials
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your API Hash

# Bot token from BotFather
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# MongoDB connection (for storing user data, playlists, etc.)
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri")

# AI Chat API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")  # OpenAI API Key for AI chat

# Authorized users (Admin List)
AUTH_USERS = [
    int(user) for user in os.getenv("AUTH_USERS", "").split(",") if user.strip().isdigit()
]

# Bot Owner (for full control)
OWNER_ID = int(os.getenv("OWNER_ID", "123456789"))  # Replace with actual owner ID

# Music settings
MAX_QUEUE_SIZE = 50  # Max number of songs in the queue per chat

# Logging (for debugging)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Admin Check Function
def is_admin(user_id):
    return user_id == OWNER_ID or user_id in AUTH_USERS