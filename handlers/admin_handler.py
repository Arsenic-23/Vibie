from pyrogram import Client, filters
from config import AUTH_USERS
from database import ban_user, unban_user, is_banned

# Restrict admin commands to authorized users
def is_admin(_, __, message):
    return message.from_user.id in AUTH_USERS

admin_filter = filters.create(is_admin)

@Client.on_message(filters.command("mban") & admin_filter)
async def ban_member(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to ban them!")
    
    user_id = message.reply_to_message.from_user.id
    ban_user(user_id)
    await message.reply_text(f"User {user_id} has been banned from using the bot.")

@Client.on_message(filters.command("unmban") & admin_filter)
async def unban_member(client, message):
    if not message.reply_to_message:
        return await message.reply_text("Reply to a user to unban them!")
    
    user_id = message.reply_to_message.from_user.id
    unban_user(user_id)
    await message.reply_text(f"User {user_id} has been unbanned.")

@Client.on_message(filters.command("skip") & admin_filter)
async def skip_song(client, message):
    # Logic to skip the current song
    await message.reply_text("Song skipped!")

@Client.on_message(filters.command("end") & admin_filter)
async def end_music(client, message):
    # Logic to stop music playback
    await message.reply_text("Music playback ended!")

@Client.on_message(filters.command("banallgc") & admin_filter)
async def ban_all_group(client, message):
    chat_id = message.chat.id
    async for member in client.get_chat_members(chat_id):
        if not member.user.is_bot:
            ban_user(member.user.id)
    await message.reply_text("All group members have been banned from using the bot!")