from pyrogram import Client, filters
from config import AUTH_USERS
from handlers.music_handler import stop_music, skip_music

# Admin-only commands
@Client.on_message(filters.command(["skip", "end"]) & filters.user(AUTH_USERS))
async def admin_controls(client, message):
    chat_id = message.chat.id
    command = message.command[0]

    if command == "skip":
        await skip_music(chat_id)
        await message.reply_text("⏩ Skipped to the next track.")
    elif command == "end":
        await stop_music(chat_id)
        await message.reply_text("🛑 Stopped the music.")
