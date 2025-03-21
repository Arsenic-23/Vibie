from pyrogram import Client, filters
import subprocess
import logging
from config import is_authorized

# Logger initialization
logger = logging.getLogger(__name__)

# AI Jukebox Mode: Automatically selects songs based on group mood
jukebox_mode = {}

@Client.on_message(filters.command("jukebox") & filters.group)
async def jukebox_command(client, message):
    chat_id = message.chat.id
    
    if not is_authorized(message.from_user.id):
        return await message.reply_text("🚫 You are not authorized to use Jukebox mode!")

    if chat_id in jukebox_mode:
        del jukebox_mode[chat_id]
        await message.reply_text("🛑 AI Jukebox Mode **disabled**!")
    else:
        jukebox_mode[chat_id] = True
        await message.reply_text("🎵 AI Jukebox Mode **enabled**! I will now play music based on the group conversation.")

# Function to play AI-generated music suggestions
async def play_jukebox(client, chat_id):
    if chat_id in jukebox_mode:
        song_url = await get_ai_suggested_song(chat_id)  # Fetch AI-suggested song
        await stream_audio(chat_id, song_url)  # Start streaming with FFmpeg
        await client.send_message(chat_id, f"🎶 AI Jukebox is now playing: {song_url}")

async def get_ai_suggested_song(chat_id):
    # Placeholder function to get AI-powered song recommendations
    # Replace this with an actual recommendation system or service
    return "https://example.com/song.mp3"  # Example song URL

def stream_audio(chat_id, audio_url):
    """Streams audio using FFmpeg"""
    logger.info(f"🎵 Streaming {audio_url} in chat {chat_id}")

    # FFmpeg command for streaming
    ffmpeg_command = [
        "ffmpeg",
        "-re",  # Read input in real-time
        "-i", audio_url,  # Input URL or file path
        "-ac", "2",  # Set audio channels (stereo)
        "-f", "s16le",  # Output format (16-bit PCM)
        "-ar", "48000",  # Audio sampling rate (48 kHz)
        "-acodec", "pcm_s16le",  # Audio codec (PCM signed 16-bit little-endian)
        "-"  # Output to stdout (for streaming)
    ]
    
    try:
        # Run FFmpeg command to stream the audio
        subprocess.Popen(ffmpeg_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        logger.info(f"✅ Started streaming in chat {chat_id} successfully!")
    except Exception as e:
        logger.error(f"❌ Failed to start streaming: {e}")