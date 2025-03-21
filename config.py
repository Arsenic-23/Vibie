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

# Authorized users (Admin List)
AUTH_USERS = [int(user) for user in os.getenv("AUTH_USERS", "").split() if user.isdigit()]

# Music settings
MAX_QUEUE_SIZE = 50  # Max number of songs in the queue per chat

# Logging (for debugging)
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"