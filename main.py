import os
import sys
import logging
import threading
import subprocess
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Health check web server for Koyeb
app = Flask(__name__)

@app.route('/')
def health_check():
    return "Bot is running", 200

def run_health_check():
    app.run(host="0.0.0.0", port=8080)

# Ensure Python detects 'handlers/' directory
HANDLERS_PATH = os.path.join(os.path.dirname(__file__), "handlers")
if HANDLERS_PATH not in sys.path:
    sys.path.append(HANDLERS_PATH)
    logger.info(f"📂 Added 'handlers/' to sys.path: {HANDLERS_PATH}")

# Debugging: Print available files in the 'handlers/' folder
logger.info("🔍 Checking handlers directory contents...")
try:
    logger.info(f"Contents: {os.listdir(HANDLERS_PATH)}")
except FileNotFoundError:
    logger.error("❌ 'handlers/' directory not found! Check deployment.")

# Initialize bot client
try:
    app_client = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
    logger.info("✅ Telegram bot initialized successfully!")
except Exception as e:
    logger.error(f"❌ Failed to initialize bot: {e}")
    sys.exit(1)

# Function to stream audio in voice chat using FFmpeg (without pytgcalls)
def stream_audio(chat_id, audio_url):
    logger.info(f"🎵 Streaming {audio_url} in chat {chat_id}")
    
    ffmpeg_command = [
        "ffmpeg",
        "-re",  # Read input in real-time
        "-i", audio_url,  # Input URL
        "-ac", "2",  # Set audio channels
        "-f", "s16le",  # Output format
        "-ar", "48000",  # Audio sampling rate
        "-acodec", "pcm_s16le",  # Audio codec
        "-"  # Output to stdout
    ]
    
    try:
        subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info("✅ Audio streaming started successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to start streaming: {e}")

# Register handlers
def register_handlers():
    from handlers import music_handler, admin_handler, ai_chat_handler
    
    # Passing the correct argument to the handler's register_handlers method
    # Based on the error, admin_handler.register_handlers() might require `call_py` as a parameter
    call_py = None  # Add or modify this line based on how 'call_py' is used in your handler
    
    music_handler.register_handlers(app_client)
    admin_handler.register_handlers(app_client, call_py)  # Correcting the missing argument here
    ai_chat_handler.register_handlers(app_client)

if __name__ == "__main__":
    logger.info("🚀 Starting the bot...")

    # Start health check server
    threading.Thread(target=run_health_check, daemon=True).start()

    # Register handlers after bot client is initialized
    register_handlers()

    # Start the bot
    try:
        app_client.start()
        logger.info("🎶 Bot is now running! Use /play to stream music.")
        app_client.idle()  # Keep the bot running
    except Exception as e:
        logger.error(f"❌ Bot failed to start: {e}")
        sys.exit(1)  # Exit to prevent restart loops