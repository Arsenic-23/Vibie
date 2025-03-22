from pyrogram import Client, filters
from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

@Client.on_message(filters.command("ask"))
async def ai_chat(client, message):
    if len(message.command) < 2:
        return await message.reply_text("❓ Please ask a question. Example: `/ask What is AI?`")

    query = " ".join(message.command[1:])
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}]
        )
        answer = response["choices"][0]["message"]["content"]
        await message.reply_text(f"🤖 **Casa:** {answer}")
    
    except Exception as e:
        await message.reply_text(f"⚠️ AI error: {e}")
