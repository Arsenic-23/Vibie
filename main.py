import asyncio
import logging
import datetime
import os
import time
from pyrogram import Client, idle

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize Pyrogram Bot
bot = Client(
    "music_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

async def sync_time():
    """Sync system time to avoid msg_id errors."""
    now = datetime.datetime.utcnow()
    print(f"[INFO] System Time Synced: {now} UTC")
    time.sleep(2)  # Wait for time sync before continuing

async def main():
    while True:
        try:
            await sync_time()  # Sync time before starting
            
            await bot.start()
            logger.info("Bot is running...")
            
            await idle()  # Keep bot running

        except Exception as e:
            logger.error(f"Bot crashed! Restarting in 5 seconds... Error: {e}")
            await bot.stop()  # Ensure bot is stopped before restarting
            await asyncio.sleep(5)  # Wait before restart
        finally:
            await bot.stop()
            logger.info("Bot stopped.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
    finally:
        loop.close()