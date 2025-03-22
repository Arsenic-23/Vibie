import asyncio
import logging
import datetime
from pyrogram import Client
import os

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

async def main():
    try:
        # Sync system time to avoid msg_id error
        now = datetime.datetime.now(datetime.UTC)
        print(f"[INFO] System Time Synced: {now} UTC")

        # Start the bot
        async with bot:
            logger.info("Bot is running...")
            await idle()  # Keep the bot running
    except Exception as e:
        logger.error(f"Bot crashed! Restarting in 5 seconds... Error: {e}")
        await asyncio.sleep(5)
        await main()  # Restart bot

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nBot stopped manually.")