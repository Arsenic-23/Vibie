from pyrogram import Client, filters
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from config import BOT_TOKEN, API_ID, API_HASH, is_authorized
import asyncio

# Initialize bot client
app = Client("music_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)
call_py = PyTgCalls(app)

# Queue system
queue = {}

# Function to play music in a chat
async def play_music(client, message, url):
    chat_id = message.chat.id
    if chat_id not in queue:
        queue[chat_id] = []

    queue[chat_id].append(url)
    
    if len(queue[chat_id]) == 1:
        await start_playback(client, chat_id)

async def start_playback(client, chat_id):
    if chat_id in queue and queue[chat_id]:
        url = queue[chat_id][0]
        await call_py.join_group_call(chat_id, AudioPiped(url), stream_type=StreamType().local_stream)

# Command: /play
@app.on_message(filters.command("play") & filters.group)
async def play_command(client, message):
    if message.reply_to_message and message.reply_to_message.audio:
        file_id = message.reply_to_message.audio.file_id
        await play_music(client, message, file_id)
        await message.reply_text(f"🎵 Now playing: {message.reply_to_message.audio.title}")
    elif len(message.command) > 1:
        url = message.text.split(None, 1)[1]
        await play_music(client, message, url)
        await message.reply_text(f"🎶 Added to queue: {url}")
    else:
        await message.reply_text("⚠️ Please provide an audio file or a URL!")

# Command: /skip
@app.on_message(filters.command("skip") & filters.group)
async def skip_command(client, message):
    chat_id = message.chat.id
    if chat_id in queue and len(queue[chat_id]) > 1:
        queue[chat_id].pop(0)
        await start_playback(client, chat_id)
        await message.reply_text("⏩ Skipped to next song!")
    else:
        await message.reply_text("⚠️ No next song in the queue!")

# Command: /stop
@app.on_message(filters.command("stop") & filters.group)
async def stop_command(client, message):
    chat_id = message.chat.id
    if chat_id in queue:
        queue.pop(chat_id)
        await call_py.leave_group_call(chat_id)
        await message.reply_text("🛑 Stopped playback!")
    else:
        await message.reply_text("⚠️ No music is playing!")

# Start the bot
@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("🎵 **Music Bot is Online!**\nUse `/play` to start playing music.")

@app.on_message(filters.command("help"))
async def help(client, message):
    await message.reply_text("🎵 **Music Commands:**\n/play - Play a song\n/skip - Skip to next song\n/stop - Stop playback")

# Run the bot
if __name__ == "__main__":
    call_py.start()
    app.run()