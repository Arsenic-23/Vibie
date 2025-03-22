from pyrogram import Client, filters
from config import is_admin

def register_handlers(app: Client):
    @app.on_message(filters.command("mban") & filters.group)
    async def ban_command(client, message):
        if not is_admin(message):
            return await message.reply_text("🚫 You don't have permission!")
        if not message.reply_to_message:
            return await message.reply_text("⚠️ Reply to a user to ban!")
        
        user_id = message.reply_to_message.from_user.id
        app.mban_list.add(user_id)
        await message.reply_text(f"🔨 Banned {message.reply_to_message.from_user.mention} from using the bot!")

    @app.on_message(filters.command("unmban") & filters.group)
    async def unban_command(client, message):
        if not is_admin(message):
            return await message.reply_text("🚫 You don't have permission!")
        if not message.reply_to_message:
            return await message.reply_text("⚠️ Reply to a user to unban!")

        user_id = message.reply_to_message.from_user.id
        if user_id in app.mban_list:
            app.mban_list.remove(user_id)
            await message.reply_text(f"✅ Unbanned {message.reply_to_message.from_user.mention}!")
        else:
            await message.reply_text("⚠️ User is not banned!")

    # You can add more admin-related commands here (e.g., kick, warn, etc.)