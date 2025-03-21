from pyrogram import Client, filters
from pytgcalls import PyTgCalls

def register_handlers(app: Client, call_py: PyTgCalls):
    @app.on_message(filters.command("chipmunk") & filters.group)
    async def chipmunk_effect(client, message):
        chat_id = message.chat.id
        await call_py.change_stream(chat_id, "chipmunk")
        await message.reply_text("🐿️ **Chipmunk effect applied!**")