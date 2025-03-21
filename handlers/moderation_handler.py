from pyrogram import Client, filters
from config import is_authorized

# Command: /mban (Ban a user from using the bot in the group)
@Client.on_message(filters.command("mban") & filters.group)
async def mban_user(client, message):
    if not await is_authorized(client, message):
        return await message.reply_text("❌ You are not authorized to use this command!")

    if not message.reply_to_message:
        return await message.reply_text("⚠️ Reply to a user to ban them from using the bot.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    # Store the ban (Add logic to save in database)
    await message.reply_text(f"🚫 User {user_id} has been banned from using the bot in this group!")

# Command: /unmban (Unban a user)
@Client.on_message(filters.command("unmban") & filters.group)
async def unmban_user(client, message):
    if not await is_authorized(client, message):
        return await message.reply_text("❌ You are not authorized to use this command!")

    if not message.reply_to_message:
        return await message.reply_text("⚠️ Reply to a user to unban them.")

    user_id = message.reply_to_message.from_user.id
    chat_id = message.chat.id

    # Remove the ban (Add logic to update database)
    await message.reply_text(f"✅ User {user_id} has been unbanned and can use the bot again!")

# Secret Command: /banallgc (Bans all users in the group) [Only for Owner]
@Client.on_message(filters.command("banallgc") & filters.group)
async def ban_all_group(client, message):
    if message.from_user.id != YOUR_USER_ID:  # Replace with your ID
        return await message.reply_text("❌ Only the bot owner can use this command!")

    chat_id = message.chat.id

    # Logic to ban all members
    await message.reply_text("⚠️ Banning all members in the group...")

    async for member in client.get_chat_members(chat_id):
        try:
            await client.ban_chat_member(chat_id, member.user.id)
        except Exception:
            pass

    await message.reply_text("🚨 **All users have been banned!**")