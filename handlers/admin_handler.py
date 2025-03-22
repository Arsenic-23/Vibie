from pyrogram import Client, filters
from pyrogram.types import Message

OWNER_ID = 7212032106  # Replace with your actual Telegram user ID

# Dictionary to store banned users (Temporary, resets on restart)
banned_users = {}

async def get_admins(client, chat_id):
    """Fetch the list of admin IDs in a group."""
    try:
        admins = await client.get_chat_administrators(chat_id)
        return [admin.user.id for admin in admins]
    except Exception as e:
        print(f"Error fetching admins: {e}")
        return []

@Client.on_message(filters.command("mban") & filters.group)
async def ban_user(client, message: Message):
    """Ban a user from using the bot in a group."""
    if not message.from_user or message.from_user.id not in await get_admins(client, message.chat.id):
        return await message.reply_text("🚫 You need to be an admin to use this command.")

    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text("⚠ Reply to a user to ban them.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    banned_users.setdefault(chat_id, set()).add(user_id)
    await message.reply_text(f"✅ User {message.reply_to_message.from_user.mention} has been **banned** from using the bot!")

@Client.on_message(filters.command("unmban") & filters.group)
async def unban_user(client, message: Message):
    """Unban a user from using the bot in a group."""
    if not message.from_user or message.from_user.id not in await get_admins(client, message.chat.id):
        return await message.reply_text("🚫 You need to be an admin to use this command.")

    if not message.reply_to_message or not message.reply_to_message.from_user:
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
    """Ban all users in a group from using the bot (Only the owner can do this)."""
    if message.from_user.id != OWNER_ID:
        return await message.reply_text("🚫 You don't have permission to use this command.")

    chat_id = message.chat.id
    try:
        members = await client.get_chat_members(chat_id)
        banned_users[chat_id] = {member.user.id for member in members if not member.user.is_bot}
        await message.reply_text("🚨 **All users have been banned** from using the bot in this group!")
    except Exception as e:
        await message.reply_text(f"❌ Failed to ban all users: {e}")

# Export handlers for main.py
handlers = [ban_user, unban_user, ban_all_users]