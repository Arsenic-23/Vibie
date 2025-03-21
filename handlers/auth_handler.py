from pyrogram import Client, filters
from config import is_admin

authorized_users = set()

def register_handlers(app: Client):
    @app.on_message(filters.command("auth") & filters.group)
    async def authorize_user(client, message):
        if not is_admin(message):
            return await message.reply_text("🚫 You don't have permission!")

        if message.reply_to_message:
            user_id = message.reply_to_message.from_user.id
            authorized_users.add(user_id)
            await message.reply_text(f"✅ Authorized {message.reply_to_message.from_user.mention}!")