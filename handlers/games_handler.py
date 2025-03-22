from pyrogram import Client, filters
import random

puzzle_questions = [
    {"question": "🔢 What comes next in the sequence? 2, 4, 8, 16, ?", "answer": "32"},
    {"question": "🧩 I have keys but open no locks. What am I?", "answer": "Keyboard"},
    {"question": "🎭 The more you take, the more you leave behind. What am I?", "answer": "Footsteps"},
    {"question": "📅 I occur once in a minute, twice in a moment, but never in a thousand years. What am I?", "answer": "The letter M"},
]

# Initialize puzzle_answers as an attribute of the bot
def ensure_puzzle_storage(client):
    if not hasattr(client, "puzzle_answers"):
        setattr(client, "puzzle_answers", {})

@Client.on_message(filters.command("puzzle"))
async def puzzle_game(client, message):
    """Sends a random puzzle to the group."""
    ensure_puzzle_storage(client)
    
    question = random.choice(puzzle_questions)
    await message.reply_text(f"🧠 Puzzle Challenge!\n\n{question['question']}\n\nReply with your answer!")

    # Store the correct answer
    client.puzzle_answers[message.chat.id] = question["answer"].lower()

@Client.on_message(filters.text & filters.reply)
async def check_puzzle_answer(client, message):
    """Checks if the user's reply is the correct answer to the puzzle."""
    ensure_puzzle_storage(client)

    if message.from_user.is_bot:  # Ignore bot messages
        return

    if message.chat.id in client.puzzle_answers:
        correct_answer = client.puzzle_answers[message.chat.id]
        user_answer = message.text.strip().lower()

        if user_answer == correct_answer:
            await message.reply_text("✅ Correct! Well done! 🎉")
            del client.puzzle_answers[message.chat.id]  # Remove the answered puzzle
        else:
            await message.reply_text("❌ Incorrect! Try again!")
    else:
        await message.reply_text("⚠ No active puzzle! Use `/puzzle` to start a new one.")