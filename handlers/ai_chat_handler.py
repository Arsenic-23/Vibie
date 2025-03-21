import openai
from pyrogram import Client, filters
from openai import ChatGPT
from config import OPENAI_API_KEY

chat_gpt = ChatGPT(OPENAI_API_KEY)

def register_handlers(app: Client):
    @app.on_message(filters.text & filters.private)
    async def ai_chat(client, message):
        response = chat_gpt.ask(message.text)
        await message.reply_text(response)