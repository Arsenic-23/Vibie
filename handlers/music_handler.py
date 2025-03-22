from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio
import logging

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Dictionary to store the queue for each chat
music_queues = {}
currently_playing = {}  # Tracks active playback per chat

@Client.on_message(filters.command("play"))
async def play_music(client, message: Message):
    """Handles the /play command to add songs to the queue and start playback."""
    if len(message.command) < 2:
        return await message.reply_text("🎵 Please provide a song name or reply to an audio file to play.")

    chat_id = message.chat.id
    song_name = " ".join(message.command[1:])

    # Add to queue
    if chat_id not in music_queues:
        music_queues[chat_id] = []
    music_queues[chat_id].append(song_name)

    await message.reply_text(f"✅ Added **{song_name}** to queue!")

    # If nothing is currently playing, start playback
    if chat_id not in currently_playing:
        await play_next_song(client, chat_id)

async def play_next_song(client, chat_id):
    """Plays the next song in the queue."""
    if chat_id in music_queues and music_queues[chat_id]:
        currently_playing[chat_id] = True  # Mark as playing
        current_song = music_queues[chat_id].pop(0)

        logger.info(f"Playing song: {current_song} in chat {chat_id}")

        await client.send_message(chat_id, f"🎶 Now Playing: **{current_song}**")

        # Simulate song playing (replace with actual audio playback logic)
        await asyncio.sleep(5)  # Simulate song playing for 5 seconds
        
        currently_playing.pop(chat_id, None)  # Mark as not playing
        await play_next_song(client, chat_id)  # Play the next song

    else:
        currently_playing.pop(chat_id, None)  # No more songs left, reset playing state

@Client.on_message(filters.command("skip"))
async def skip_song(client, message: Message):
    """Skips the currently playing song and moves to the next in queue."""
    chat_id = message.chat.id
    if chat_id in music_queues and music_queues[chat_id]:
        await message.reply_text("⏭ Skipping song...")
        currently_playing.pop(chat_id, None)  # Allow next song to start
        await play_next_song(client, chat_id)
    else:
        await message.reply_text("⚠ No songs in queue!")

@Client.on_message(filters.command("queue"))
async def show_queue(client, message: Message):
    """Displays the current music queue."""
    chat_id = message.chat.id
    if chat_id in music_queues and music_queues[chat_id]:
        queue_text = "\n".join(f"🎵 {idx+1}. {song}" for idx, song in enumerate(music_queues[chat_id]))
        await message.reply_text(f"📜 **Current Queue:**\n{queue_text}")
    else:
        await message.reply_text("🚫 No songs in queue!")

@Client.on_message(filters.command("stop"))
async def stop_music(client, message: Message):
    """Stops all music and clears the queue."""
    chat_id = message.chat.id
    if chat_id in music_queues:
        music_queues[chat_id] = []  # Clear the queue
        currently_playing.pop(chat_id, None)  # Stop playing
        await message.reply_text("⏹ Music stopped!")
    else:
        await message.reply_text("⚠ No music is playing!")