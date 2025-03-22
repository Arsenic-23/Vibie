import asyncio
import logging
import datetime
import os
import ntplib  # Import ntplib for time sync
from pyrogram import Client, idle

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
    """Sync system time to avoid msg_id errors using ntplib."""
    try:
        # Use NTP to sync time
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org', version=3)
        synced_time = datetime.datetime.utcfromtimestamp(response.tx_time)
        print(f"[INFO] System Time Synced: {synced_time} UTC")
        
    except Exception as e:
        logger.warning(f"Time sync failed: {e}")
    
    await asyncio.sleep(2)  # Wait for time sync to take effect

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
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("Bot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")