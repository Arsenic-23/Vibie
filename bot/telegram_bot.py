import os
import asyncio
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackContext
from queue_manager import SongQueue
from downloader import download_audio
from config import BOT_TOKEN, BACKEND_API_URL

# Initialize bot and queue
queue = SongQueue()

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("Welcome to the Music Bot! Use /play <song_name> to start.")

async def play(update: Update, context: CallbackContext) -> None:
    if not context.args:
        await update.message.reply_text("Usage: /play <song name>")
        return
    
    song_name = " ".join(context.args)
    await update.message.reply_text(f"Searching for {song_name}...")
    
    song_url = download_audio(song_name)
    if song_url:
        queue.add_song(song_name, song_url)
        await update.message.reply_text(f"Added {song_name} to queue!")
        
        # Send to backend for streaming
        requests.post(f"{BACKEND_API_URL}/add_to_queue", json={"song_name": song_name, "song_url": song_url})
    else:
        await update.message.reply_text("Failed to download the song.")

async def skip(update: Update, context: CallbackContext) -> None:
    next_song = queue.next_song()
    if next_song:
        await update.message.reply_text(f"Skipping... Now playing {next_song['name']}!")
        requests.post(f"{BACKEND_API_URL}/skip", json={"song_name": next_song['name'], "song_url": next_song['url']})
    else:
        await update.message.reply_text("No more songs in the queue.")

async def stop(update: Update, context: CallbackContext) -> None:
    queue.clear()
    await update.message.reply_text("Stream ended.")
    requests.post(f"{BACKEND_API_URL}/stop")

# Initialize bot application
app = Application.builder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("play", play))
app.add_handler(CommandHandler("skip", skip))
app.add_handler(CommandHandler("stop", stop))

if __name__ == "__main__":
    print("Bot is running...")
    app.run_polling()
