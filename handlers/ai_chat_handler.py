import openai
from pyrogram import Client, filters
from config import OPENAI_API_KEY

# Set the OpenAI API key
openai.api_key = OPENAI_API_KEY  

def register_handlers(app: Client):
    @app.on_message(filters.text & filters.private)  # Responds only in private chats
    async def ai_chat(client, message):
        try:
            response = await openai.ChatCompletion.acreate(
                model="gpt-3.5-turbo",  # Use "gpt-4" if available
                messages=[{"role": "user", "content": message.text}]
            )
            reply_text = response["choices"][0]["message"]["content"]
            await message.reply_text(reply_text)
        except Exception as e:
            await message.reply_text(f"⚠️ AI Error: {str(e)}")