import logging
from pyrogram import Client, filters
from yt_dlp import YoutubeDL
from main import stream_audio  # Import the new streaming function

# Enable logging
logger = logging.getLogger(__name__)

# Configure YouTube Downloader
ydl_opts = {
    "format": "bestaudio/best",
    "noplaylist": True,
    "quiet": True,
    "extractaudio": True,
    "default_search": "ytsearch"
}

def get_audio_url(query):
    """Fetches the best audio URL from YouTube."""
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query, download=False)
        if "entries" in info:
            info = info["entries"][0]  # Get first result from search
        return info["url"]

def register_handlers(app_client):
    """Registers all music-related handlers."""

    @app_client.on_message(filters.command("play"))
    async def play_song(client, message):
        """Handles /play command to stream music."""
        chat_id = message.chat.id

        if len(message.command) < 2:
            await message.reply_text("❌ Please provide a song name or link!")
            return

        query = " ".join(message.command[1:])
        try:
            audio_url = get_audio_url(query)
            stream_audio(chat_id, audio_url)  # Call new function to stream

            await message.reply_text(f"🎵 Now playing: **{query}**")
        except Exception as e:
            logger.error(f"❌ Error playing song: {e}")
            await message.reply_text("❌ Failed to play this song!")

logger.info("✅ Music handler loaded!")