import asyncio
import logging
import datetime
from pyrogram import Client, idle
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
        await bot.start()
        logger.info("Bot is running...")

        await idle()  # Keep the bot running

    except Exception as e:
        logger.error(f"Bot crashed! Restarting in 5 seconds... Error: {e}")
        await asyncio.sleep(5)
        await main()  # Restart bot

    finally:
        await bot.stop()
        logger.info("Bot stopped.")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("\nBot stopped manually.")
    except Exception as e:
        logger.error(f"Unexpected Error: {e}")
    finally:
        loop.close()