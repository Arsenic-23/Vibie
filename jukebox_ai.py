from pyrogram import Client, filters
import openai
from config import OPENAI_API_KEY, BOT_TOKEN, API_ID, API_HASH
from music_handler import play_music

# Initialize bot client
app = Client("jukebox_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Set up OpenAI API
openai.api_key = OPENAI_API_KEY

# Command: /jukebox <mood>
@app.on_message(filters.command("jukebox") & filters.group)
async def jukebox_command(client, message):
    if len(message.command) > 1:
        mood = message.text.split(None, 1)[1]
    else:
        await message.reply_text("🎵 Please provide a mood or theme! Example: `/jukebox chill`")
        return

    await message.reply_text(f"🤖 Finding the perfect song for **{mood}**...")

    # Generate song recommendation using AI
    prompt = f"Suggest a song for the mood: {mood}. Provide the song name and artist."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    song_suggestion = response["choices"][0]["message"]["content"]

    await message.reply_text(f"🎶 **AI Jukebox Suggests:** {song_suggestion}")

    # Auto-play the recommended song
    await play_music(client, message, song_suggestion)

# Command: /vibecheck
@app.on_message(filters.command("vibecheck") & filters.group)
async def vibe_check(client, message):
    await message.reply_text("🔮 Checking the group's vibe...")

    # AI determines the mood of the chat
    chat_history = []
    async for msg in client.get_chat_history(message.chat.id, limit=10):
        chat_history.append(msg.text)

    prompt = f"Analyze the following chat messages and determine the overall vibe in one word:\n\n{chat_history}"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    mood = response["choices"][0]["message"]["content"]
    
    await message.reply_text(f"🌈 The group's vibe is: **{mood}**\nTry `/jukebox {mood}` for a perfect song!")

# Start the bot
if __name__ == "__main__":
    app.run()