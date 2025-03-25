import os
import logging
import asyncio
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types import AudioPiped
from config import API_ID, API_HASH, BOT_TOKEN
from pyrogram import Client

# Initialize Pyrogram client and PyTgCalls
app = Client("VibieMusicBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
pytgcalls = PyTgCalls(app)

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to manage chat-specific playback
playing_chats = {}

async def start_pytgcalls():
    """Start the PyTgCalls client"""
    await app.start()
    await pytgcalls.start()

async def stop_pytgcalls():
    """Stop PyTgCalls"""
    await pytgcalls.stop()
    await app.stop()

async def play_audio(chat_id: int, song_file: str):
    """Plays the song in the Telegram voice chat."""
    try:
        if chat_id in playing_chats:
            await pytgcalls.leave_group_call(chat_id)

        await pytgcalls.join_group_call(
            chat_id,
            AudioPiped(song_file, stream_type=StreamType().local_stream),
        )
        playing_chats[chat_id] = song_file
        logger.info(f"Playing {song_file} in chat {chat_id}")

    except Exception as e:
        logger.error(f"Error playing audio: {e}")

async def stop_audio(chat_id: int):
    """Stops the currently playing song."""
    try:
        if chat_id in playing_chats:
            await pytgcalls.leave_group_call(chat_id)
            del playing_chats[chat_id]
            logger.info(f"Stopped playback in chat {chat_id}")
        else:
            logger.info(f"No active playback in chat {chat_id}")

    except Exception as e:
        logger.error(f"Error stopping audio: {e}")

async def pause_audio(chat_id: int):
    """Pauses the audio (leaves the chat)."""
    await stop_audio(chat_id)

async def resume_audio(chat_id: int, song_file: str):
    """Resumes audio playback by replaying the last song."""
    await play_audio(chat_id, song_file)

async def skip_audio(chat_id: int):
    """Skips the current song and stops playback."""
    await stop_audio(chat_id)

# Start PyTgCalls when the script starts
asyncio.run(start_pytgcalls())