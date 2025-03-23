import asyncio
import logging
import datetime
import os
import time
import sys
import ntplib
from pyrogram import Client, idle
from pyrogram.errors import FloodWait  # Import error handling

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

async def sync_time():
    """Synchronize system time using NTP servers and log sync events."""
    try:
        c = ntplib.NTPClient()
        response = c.request('pool.ntp.org')
        synced_time = datetime.datetime.fromtimestamp(response.tx_time, datetime.timezone.utc)
        logger.info(f"[INFO] Time synced: {synced_time}")
        return True
    except Exception as e:
        logger.warning(f"[WARNING] Time sync failed: {e}")
        return False

async def start_bot_with_retries():
    """Start the bot with retry mechanism."""
    retries = 5
    while retries > 0:
        try:
            # Start the bot
            await bot.start()
            logger.info("Bot is running...")
            await idle()  # Keep the bot running
            break
        except FloodWait as e:
            logger.warning(f"FloodWait: Sleeping for {e.x} seconds...")
            await asyncio.sleep(e.x)  # Async sleep instead of time.sleep
        except Exception as e:
            logger.error(f"Error: {e}")
            retries -= 1
            if retries == 0:
                logger.error("Max retries reached. Exiting.")
                sys.exit(1)  # Proper exit for async functions
            logger.info("Retrying in 5 seconds...")
            await asyncio.sleep(5)  # Async sleep instead of time.sleep

async def main():
    """Run the sync_time function before the bot starts."""
    sync_successful = await sync_time()
    if sync_successful:
        await asyncio.sleep(1)  # Wait for time to settle before starting bot
        await start_bot_with_retries()
    else:
        logger.error("Time synchronization failed. Bot will not start.")

if __name__ == "__main__":
    try:
        asyncio.run(main())  # Run the main function
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")