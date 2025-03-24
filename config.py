import os
from dotenv import load_dotenv

# Load environment variables from .env file (if exists)
load_dotenv()

# Telegram API credentials
API_ID = int(os.getenv("API_ID", "123456"))  # Replace with your API ID
API_HASH = os.getenv("API_HASH", "your_api_hash")  # Replace with your API Hash
BOT_TOKEN = os.getenv("BOT_TOKEN", "your_bot_token")

# MongoDB for storing data
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri")

# OpenAI API for AI chat & features
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

# Admin Users
AUTH_USERS = [int(user) for user in os.getenv("AUTH_USERS", "").split() if user.isdigit()]

# Music Settings
MAX_QUEUE_SIZE = 50  # Max number of songs in queue per chat

# Restart Settings
AUTO_RESTART = os.getenv("AUTO_RESTART", "True").lower() == "true"

# Debug Mode
DEBUG_MODE = os.getenv("DEBUG_MODE", "False").lower() == "true"

# Function to check if user is admin
def is_admin(user_id):
    return user_id in AUTH_USERS