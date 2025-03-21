import os
import asyncio
import subprocess
from pyrogram import Client, filters
from config import BOT_TOKEN

# Function to play audio using FFmpeg
async def play_audio(client: Client, chat_id: int, audio_url: str):
    try:
        process = subprocess.Popen(
            ["ffmpeg", "-re", "-i", audio_url, "-f", "s16le", "-ac", "2", "-ar", "48000", "pipe:1"],
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL
        )

        async for chunk in process.stdout:
            await client.send_voice(chat_id, chunk, caption="🎵 Now playing...")

    except Exception as e:
        print(f"Error playing audio: {e}")

# /play command to fetch and play a song
@Client.on_message(filters.command("play"))
async def play_music(client, message):
    if len(message.command) < 2:
        await message.reply_text("❌ Please provide a YouTube link or song name!")
        return

    audio_url = message.text.split(" ", 1)[1]  # Extract song URL
    chat_id = message.chat.id

    await message.reply_text(f"🔄 **Fetching song:** {audio_url}...")
    await play_audio(client, chat_id, audio_url)  # Play using FFmpeg

# /skip command to stop the current song
@Client.on_message(filters.command("skip"))
async def skip_music(client, message):
    await message.reply_text("⏭ Skipping current song...")
    os.system("pkill -9 ffmpeg")  # Kill FFmpeg process to stop audio

# /stop command to stop all playback
@Client.on_message(filters.command("stop"))
async def stop_music(client, message):
    await message.reply_text("🛑 Stopping playback...")
    os.system("pkill -9 ffmpeg")  # Kill FFmpeg to stop playback

# /pause command to pause music (Currently not supported via FFmpeg)
@Client.on_message(filters.command("pause"))
async def pause_music(client, message):
    await message.reply_text("⏸ Pause is not supported yet with FFmpeg streaming.")

# /resume command to resume music (Currently not supported via FFmpeg)
@Client.on_message(filters.command("resume"))
async def resume_music(client, message):
    await message.reply_text("▶ Resume is not supported yet with FFmpeg streaming.")