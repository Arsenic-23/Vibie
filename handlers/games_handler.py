from pyrogram import Client, filters
import random

puzzle_questions = [
    {"question": "🔢 What comes next in the sequence? 2, 4, 8, 16, ?", "answer": "32"},
    {"question": "🧩 I have keys but open no locks. What am I?", "answer": "Keyboard"},
    {"question": "🎭 The more you take, the more you leave behind. What am I?", "answer": "Footsteps"},
    {"question": "📅 I occur once in a minute, twice in a moment, but never in a thousand years. What am I?", "answer": "The letter M"},
]

@Client.on_message(filters.command("puzzle"))
async def puzzle_game(client, message):
    question = random.choice(puzzle_questions)
    await message.reply_text(f"🧠 Puzzle Challenge!\n\n{question['question']}\n\nReply with your answer!")

    # Store the correct answer in chat memory
    client.puzzle_answers[message.chat.id] = question["answer"].lower()

@Client.on_message(filters.text & filters.reply)
async def check_puzzle_answer(client, message):
    if message.chat.id in client.puzzle_answers:
        correct_answer = client.puzzle_answers[message.chat.id]
        user_answer = message.text.lower()

        if user_answer == correct_answer:
            await message.reply_text("✅ Correct! Well done! 🎉")
            del client.puzzle_answers[message.chat.id]
        else:
            await message.reply_text("❌ Incorrect! Try again!")
