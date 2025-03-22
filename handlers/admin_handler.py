from pyrogram import Client, filters
from pyrogram.types import Message

# Dictionary to store banned users
banned_users = {}

@Client.on_message(filters.command("mban") & filters.group)
async def ban_user(client, message: Message):
    if not message.from_user or not message.from_user.id in await get_admins(client, message.chat.id):
        return await message.reply_text("🚫 You need to be an admin to use this command.")

    if not message.reply_to_message:
        return await message.reply_text("⚠ Reply to a user to ban them from using the bot.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    if chat_id not in banned_users:
        banned_users[chat_id] = set()

    banned_users[chat_id].add(user_id)
    await message.reply_text(f"✅ User {message.reply_to_message.from_user.mention} has been **banned** from using the bot!")

@Client.on_message(filters.command("unmban") & filters.group)
async def unban_user(client, message: Message):
    if not message.from_user or not message.from_user.id in await get_admins(client, message.chat.id):
        return await message.reply_text("🚫 You need to be an admin to use this command.")

    if not message.reply_to_message:
        return await message.reply_text("⚠ Reply to a user to unban them.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    if chat_id in banned_users and user_id in banned_users[chat_id]:
        banned_users[chat_id].remove(user_id)
        await message.reply_text(f"✅ User {message.reply_to_message.from_user.mention} has been **unbanned**!")
    else:
        await message.reply_text("⚠ This user is not banned.")

@Client.on_message(filters.command("banallgc") & filters.group)
async def ban_all_users(client, message: Message):
    if message.from_user.id != OWNER_ID:  # Only the bot owner can use this command
        return await message.reply_text("🚫 You don't have permission to use this command.")

    chat_id = message.chat.id
    banned_users[chat_id] = {member.user.id for member in await client.get_chat_members(chat_id)}
    
    await message.reply_text("🚨 **All users have been banned** from using the bot in this group!")

async def get_admins(client, chat_id):
    admins = await client.get_chat_members(chat_id, filter="administrators")
    return [admin.user.id for admin in admins]