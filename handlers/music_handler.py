from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Dictionary to store the queue for each chat
music_queues = {}

@Client.on_message(filters.command("play"))
async def play_music(client, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("🎵 Please provide a song name or reply to an audio file to play.")

    chat_id = message.chat.id
    song_name = " ".join(message.command[1:])

    # Add to queue
    if chat_id not in music_queues:
        music_queues[chat_id] = []
    music_queues[chat_id].append(song_name)

    if len(music_queues[chat_id]) == 1:
        await play_next_song(client, chat_id)

    await message.reply_text(f"✅ Added **{song_name}** to queue!")

async def play_next_song(client, chat_id):
    if chat_id in music_queues and music_queues[chat_id]:
        current_song = music_queues[chat_id].pop(0)
        await client.send_message(chat_id, f"🎶 Now Playing: **{current_song}**")
        
        # Simulate song playing (replace with actual audio playback logic)
        await asyncio.sleep(5)  # Simulate a song playing for 5 seconds
        await play_next_song(client, chat_id)

@Client.on_message(filters.command("skip"))
async def skip_song(client, message: Message):
    chat_id = message.chat.id
    if chat_id in music_queues and music_queues[chat_id]:
        await message.reply_text("⏭ Skipping song...")
        await play_next_song(client, chat_id)
    else:
        await message.reply_text("⚠ No songs in queue!")

@Client.on_message(filters.command("queue"))
async def show_queue(client, message: Message):
    chat_id = message.chat.id
    if chat_id in music_queues and music_queues[chat_id]:
        queue_text = "\n".join(f"🎵 {song}" for song in music_queues[chat_id])
        await message.reply_text(f"📜 **Current Queue:**\n{queue_text}")
    else:
        await message.reply_text("🚫 No songs in queue!")

@Client.on_message(filters.command("stop"))
async def stop_music(client, message: Message):
    chat_id = message.chat.id
    if chat_id in music_queues:
        music_queues[chat_id] = []  # Clear the queue
        await message.reply_text("⏹ Music stopped!")
    else:
        await message.reply_text("⚠ No music is playing!")

@Client.on_voice_chat_started()
async def voice_chat_started(client, chat: VoiceChatStarted):
    await client.send_message(chat.chat.id, "🎤 Voice chat started! You can now play music.")

@Client.on_voice_chat_ended()
async def voice_chat_ended(client, chat: VoiceChatEnded):
    await client.send_message(chat.chat.id, "📴 Voice chat ended! Music playback stopped.")
