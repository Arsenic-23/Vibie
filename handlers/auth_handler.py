from pyrogram import Client, filters
from config import AUTH_USERS

# Command to authorize a user
@Client.on_message(filters.command("auth") & filters.user(AUTH_USERS))
async def authorize_user(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/auth <user_id>`")
    
    try:
        user_id = int(message.command[1])
        if user_id in AUTH_USERS:
            return await message.reply_text("User is already authorized.")
        
        AUTH_USERS.append(user_id)
        await message.reply_text(f"User `{user_id}` has been authorized!")
    except ValueError:
        await message.reply_text("Invalid user ID.")

# Command to remove authorization
@Client.on_message(filters.command("unauth") & filters.user(AUTH_USERS))
async def unauthorize_user(client, message):
    if len(message.command) < 2:
        return await message.reply_text("Usage: `/unauth <user_id>`")
    
    try:
        user_id = int(message.command[1])
        if user_id not in AUTH_USERS:
            return await message.reply_text("User is not authorized.")
        
        AUTH_USERS.remove(user_id)
        await message.reply_text(f"User `{user_id}` has been unauthorized!")
    except ValueError:
        await message.reply_text("Invalid user ID.")