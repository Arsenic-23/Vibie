from pyrogram import Client, filters
import random

# Puzzle questions and answers
PUZZLES = [
    {"question": "I speak without a mouth and hear without ears. What am I?", "answer": "echo"},
    {"question": "The more you take, the more you leave behind. What am I?", "answer": "footsteps"},
    {"question": "What has to be broken before you can use it?", "answer": "egg"},
]

# Music challenge (guess the song)
SONG_QUIZ = {
    "Despacito": "🎵 Guess this song: 'Des... pa... ???' 🎶",
    "Shape of You": "🎵 Guess this song: 'I'm in love with the ?? of you' 🎶",
    "Believer": "🎵 Guess this song: 'First things first, I'ma say all the ?? inside my head' 🎶",
}

@Client.on_message(filters.command("puzzle"))
async def send_puzzle(client, message):
    puzzle = random.choice(PUZZLES)
    await message.reply_text(f"🧩 Puzzle: {puzzle['question']}\n\nReply with your answer!")

@Client.on_message(filters.text & filters.reply)
async def check_puzzle_answer(client, message):
    replied = message.reply_to_message.text
    for puzzle in PUZZLES:
        if puzzle["question"] in replied and message.text.lower() == puzzle["answer"]:
            return await message.reply_text("✅ Correct answer! 🎉")
    
    await message.reply_text("❌ Incorrect! Try again.")

@Client.on_message(filters.command("songquiz"))
async def send_song_quiz(client, message):
    song, hint = random.choice(list(SONG_QUIZ.items()))
    await message.reply_text(f"{hint}\n\nReply with the song name!")

@Client.on_message(filters.text & filters.reply)
async def check_song_quiz_answer(client, message):
    replied = message.reply_to_message.text
    for song, hint in SONG_QUIZ.items():
        if hint in replied and message.text.lower() == song.lower():
            return await message.reply_text("✅ Correct! You guessed the song! 🎵")
    
    await message.reply_text("❌ Wrong! Try again.")