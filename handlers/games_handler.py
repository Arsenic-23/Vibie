from pyrogram import Client, filters
import random

games = {
    "trivia": ["What is 2+2?", "Who wrote Hamlet?", "What is the capital of Japan?"],
    "puzzle": ["🧩 Solve this: 5 + (3×2) = ?", "🧠 What is the missing number? 2, 4, ?, 8"]
}

def register_handlers(app: Client):
    @app.on_message(filters.command("game") & filters.group)
    async def start_game(client, message):
        category = random.choice(list(games.keys()))
        question = random.choice(games[category])
        await message.reply_text(f"🎮 **{category.upper()} GAME**\n{question}")