from pyrogram import Client, filters
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.types.input_stream import AudioPiped
from config import is_authorized

queue = {}

def register_handlers(app: Client, call_py: PyTgCalls):
    @app.on_message(filters.command("play") & filters.group)
    async def play_command(client, message):
        if message.reply_to_message and message.reply_to_message.audio:
            file_id = message.reply_to_message.audio.file_id
            chat_id = message.chat.id
            if chat_id not in queue:
                queue[chat_id] = []
            queue[chat_id].append(file_id)

            if len(queue[chat_id]) == 1:
                await call_py.join_group_call(chat_id, AudioPiped(file_id), stream_type=StreamType().local_stream)
                await message.reply_text(f"🎵 Now playing: {message.reply_to_message.audio.title}")

    @app.on_message(filters.command("skip") & filters.group)
    async def skip_command(client, message):
        chat_id = message.chat.id
        if chat_id in queue and len(queue[chat_id]) > 1:
            queue[chat_id].pop(0)
            await call_py.leave_group_call(chat_id)
            await call_py.join_group_call(chat_id, AudioPiped(queue[chat_id][0]), stream_type=StreamType().local_stream)
            await message.reply_text("⏩ Skipped to next song!")
        else:
            await message.reply_text("⚠️ No next song in the queue!")

    @app.on_message(filters.command("stop") & filters.group)
    async def stop_command(client, message):
        chat_id = message.chat.id
        if chat_id in queue:
            queue.pop(chat_id)
            await call_py.leave_group_call(chat_id)
            await message.reply_text("🛑 Stopped playback!")
