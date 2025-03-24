from pyrogram import Client, filters
from pytube import YouTube
import os

# Dictionary to store the music queue
MUSIC_QUEUE = {}

@Client.on_message(filters.command("play"))
async def play_music(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/play <song name or YouTube link>`")

    chat_id = message.chat.id
    query = " ".join(message.command[1:])

    # Download audio from YouTube
    try:
        yt = YouTube(query) if "youtube.com" in query or "youtu.be" in query else YouTube(f"https://www.youtube.com/results?search_query={query}")
        audio_stream = yt.streams.filter(only_audio=True).first()
        file_path = audio_stream.download(filename="music.mp3")

        # Add to queue
        if chat_id not in MUSIC_QUEUE:
            MUSIC_QUEUE[chat_id] = []
        MUSIC_QUEUE[chat_id].append(file_path)

        await message.reply_text(f"🎶 Added **{yt.title}** to the queue!")

        # If nothing is playing, start playing
        if len(MUSIC_QUEUE[chat_id]) == 1:
            await start_playback(client, message, chat_id)

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

async def start_playback(client, message, chat_id):
    if MUSIC_QUEUE.get(chat_id):
        file_path = MUSIC_QUEUE[chat_id][0]

        # Play the music (pseudo-code, needs actual playback handling)
        await message.reply_voice(file_path, caption="🎵 Now Playing!")

        # Remove from queue after playing
        MUSIC_QUEUE[chat_id].pop(0)

        # If more songs in queue, play next
        if MUSIC_QUEUE[chat_id]:
            await start_playback(client, message, chat_id)

@Client.on_message(filters.command("skip"))
async def skip_music(client, message):
    chat_id = message.chat.id
    if chat_id in MUSIC_QUEUE and MUSIC_QUEUE[chat_id]:
        MUSIC_QUEUE[chat_id].pop(0)  # Remove current song
        await message.reply_text("⏭ Skipping to the next song...")
        await start_playback(client, message, chat_id)
    else:
        await message.reply_text("❌ No songs in the queue.")

@Client.on_message(filters.command("queue"))
async def show_queue(client, message):
    chat_id = message.chat.id
    if chat_id in MUSIC_QUEUE and MUSIC_QUEUE[chat_id]:
        queue_text = "\n".join([f"{idx+1}. {os.path.basename(song)}" for idx, song in enumerate(MUSIC_QUEUE[chat_id])])
        await message.reply_text(f"🎵 **Current Queue:**\n{queue_text}")
    else:
        await message.reply_text("🎶 The queue is empty!")

@Client.on_message(filters.command("end"))
async def stop_music(client, message):
    chat_id = message.chat.id
    MUSIC_QUEUE[chat_id] = []
    await message.reply_text("🛑 Music playback stopped.")