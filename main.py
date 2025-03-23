import asyncio
import logging
import os
import sys
from flask import Flask
from threading import Thread
from pyrogram import Client, idle
from pyrogram.errors import FloodWait, RPCError

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Initialize Pyrogram Bot
bot = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Flask Web Server (for UptimeRobot)
app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

def run_web_server():
    app.run(host="0.0.0.0", port=8080, debug=False)

Thread(target=run_web_server, daemon=True).start()

async def start_bot_with_retries():
    """Start the bot with retry mechanism."""
    retries = 5
    while retries > 0:
        try:
            await bot.start()
            logger.info("Bot is running...")
            await idle()  # Keep the bot running
            return
        except FloodWait as e:
            logger.warning(f"FloodWait: Sleeping for {e.x} seconds...")
            await asyncio.sleep(e.x)
        except RPCError as e:
            logger.error(f"RPCError: {e}")
            retries -= 1
            if retries == 0:
                logger.error("Max retries reached. Exiting.")
                sys.exit(1)
            logger.info("Retrying in 5 seconds...")
            await asyncio.sleep(5)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            sys.exit(1)

async def main():
    """Run the bot"""
    await start_bot_with_retries()

if __name__ == "__main__":
    try:
        asyncio.run(main())  
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")