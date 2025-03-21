from pyrogram import Client, filters
from pytgcalls import PyTgCalls
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped
import os

# Initialize PyTgCalls
app = Client("music_bot")
pytgcalls = PyTgCalls(app)

@app.on_message(filters.command("play"))
async def play_song(client, message):
    if not message.reply_to_message or not message.reply_to_message.audio:
        await message.reply_text("Reply to an audio file to play.")
        return

    file_path = await message.reply_to_message.download()
    
    try:
        await pytgcalls.start()
        await pytgcalls.join_group_call(
            message.chat.id,
            AudioPiped(file_path)
        )
        await message.reply_text("🔊 Playing music!")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

@app.on_message(filters.command("stop"))
async def stop_song(client, message):
    try:
        await pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("⏹ Stopped playing music.")
    except Exception as e:
        await message.reply_text(f"❌ Error: {str(e)}")

pytgcalls.run()