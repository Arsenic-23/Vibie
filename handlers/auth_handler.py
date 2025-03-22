from pyrogram import Client, filters
import json

AUTH_FILE = "auth_users.json"

# Load authorized users from file
def load_auth_users():
    try:
        with open(AUTH_FILE, "r") as f:
            return set(json.load(f))
    except (FileNotFoundError, json.JSONDecodeError):
        return set()

# Save authorized users to file
def save_auth_users(auth_users):
    with open(AUTH_FILE, "w") as f:
        json.dump(list(auth_users), f)

# Initialize authorized users
AUTH_USERS = load_auth_users()

@Client.on_message(filters.command("auth") & filters.group)
async def authorize_user(client, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("🚫 You are not allowed to use this command.")

    if not message.reply_to_message:
        return await message.reply_text("**Usage:** Reply to a user with `/auth` to authorize them.")

    user_id = message.reply_to_message.from_user.id
    if user_id in AUTH_USERS:
        return await message.reply_text("✅ User is already authorized.")

    AUTH_USERS.add(user_id)
    save_auth_users(AUTH_USERS)
    await message.reply_text(f"✅ User `{user_id}` has been authorized!")

@Client.on_message(filters.command("unauth") & filters.group)
async def unauthorize_user(client, message):
    if message.from_user.id not in AUTH_USERS:
        return await message.reply_text("🚫 You are not allowed to use this command.")

    if not message.reply_to_message:
        return await message.reply_text("**Usage:** Reply to a user with `/unauth` to remove authorization.")

    user_id = message.reply_to_message.from_user.id
    if user_id not in AUTH_USERS:
        return await message.reply_text("⚠️ User is not authorized.")

    AUTH_USERS.remove(user_id)
    save_auth_users(AUTH_USERS)
    await message.reply_text(f"🚫 User `{user_id}` has been unauthenticated.")