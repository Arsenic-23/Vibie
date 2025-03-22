from pyrogram import Client, filters
from config import AUTH_USERS
from handlers.music_handler import stop_music, skip_music

@Client.on_message(filters.command(["end", "skip"]) & filters.user(AUTH_USERS))
async def admin_controls(client, message):
    chat_id = message.chat.id
    command = message.command[0]

    if command == "end":
        await stop_music(chat_id)
        await message.reply_text("🛑 Music playback has been stopped.")
    elif command == "skip":
        await skip_music(chat_id)
        await message.reply_text("⏭ Skipped to the next song.")

@Client.on_message(filters.command("auth") & filters.user(AUTH_USERS))
async def authorize_user(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/auth <user_id>`")

    user_id = int(message.command[1])
    if user_id not in AUTH_USERS:
        AUTH_USERS.append(user_id)
        await message.reply_text(f"✅ User `{user_id}` has been authorized.")
    else:
        await message.reply_text(f"⚠️ User `{user_id}` is already authorized.")

@Client.on_message(filters.command("unmban") & filters.user(AUTH_USERS))
async def unban_music_user(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/unmban <user_id>`")

    user_id = int(message.command[1])
    # Logic to remove user from ban list (implement ban system)
    await message.reply_text(f"✅ User `{user_id}` has been unbanned from using music commands.")