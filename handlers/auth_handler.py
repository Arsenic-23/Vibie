from pyrogram import Client, filters
from config import AUTH_USERS

@Client.on_message(filters.command("auth"))
async def authorize_user(client, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("🚫 You are not allowed to use this command.")

    if len(message.command) < 2 or not message.reply_to_message:
        return await message.reply_text("**Usage:** Reply to a user with `/auth` to authorize them.")

    user_id = message.reply_to_message.from_user.id
    if user_id in AUTH_USERS:
        return await message.reply_text("✅ User is already authorized.")

    AUTH_USERS.append(user_id)
    await message.reply_text(f"✅ User `{user_id}` has been authorized!")

@Client.on_message(filters.command("unauth"))
async def unauthorize_user(client, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("🚫 You are not allowed to use this command.")

    if len(message.command) < 2 or not message.reply_to_message:
        return await message.reply_text("**Usage:** Reply to a user with `/unauth` to remove authorization.")

    user_id = message.reply_to_message.from_user.id
    if user_id not in AUTH_USERS:
        return await message.reply_text("⚠️ User is not authorized.")

    AUTH_USERS.remove(user_id)
    await message.reply_text(f"🚫 User `{user_id}` has been unauthenticated.")
