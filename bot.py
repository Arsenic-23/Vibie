import os
import logging
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN
from music_handler import MusicPlayer
from jukebox_ai import AIChat
from voice_commands import VoiceCommands

# Enable logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the bot client
bot = Client(
    "MusicBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# Initialize music player and AI chat
music_player = MusicPlayer(bot)
ai_chat = AIChat(bot)
voice_commands = VoiceCommands(bot)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        "**Welcome to the Highly Advanced Music Bot!**\n"
        "- Use /play <song name> to play music\n"
        "- Use /skip to skip the current song\n"
        "- Use /pause to pause the music\n"
        "- Use /continue to resume\n"
        "- Use /help to see all commands"
    )

@bot.on_message(filters.command("play"))
async def play_song(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a song name!")
        return
    await music_player.play(query, message)

@bot.on_message(filters.command("skip"))
async def skip_song(client, message):
    await music_player.skip(message)

@bot.on_message(filters.command("pause"))
async def pause_song(client, message):
    await music_player.pause(message)

@bot.on_message(filters.command("continue"))
async def resume_song(client, message):
    await music_player.resume(message)

@bot.on_message(filters.command("help"))
async def help_command(client, message):
    await message.reply_text(
        "**🎵 Music Bot Commands 🎵**\n"
        "/play <song> - Play a song\n"
        "/skip - Skip current song\n"
        "/pause - Pause music\n"
        "/continue - Resume music\n"
        "/vplay <video> - Play video in voice chat\n"
        "/pf - Force play a new song immediately\n"
        "/seek <time> - Seek to a specific time in the song\n"
        "/lyrics <song> - Get song lyrics\n"
        "/mban <user> - Ban a user from using the bot\n"
        "/unmban <user> - Unban a user\n"
        "/auth <user> - Authorize user for admin commands\n"
    )

@bot.on_message(filters.command("lyrics"))
async def get_lyrics(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("Please provide a song name!")
        return
    lyrics = await music_player.get_lyrics(query)
    await message.reply_text(lyrics)

@bot.on_message(filters.command("chat"))
async def chat_with_ai(client, message):
    query = " ".join(message.command[1:])
    if not query:
        await message.reply_text("What would you like to ask?")
        return
    response = await ai_chat.get_response(query)
    await message.reply_text(response)

@bot.on_message(filters.command("voice"))
async def voice_command(client, message):
    command = " ".join(message.command[1:])
    if not command:
        await message.reply_text("Please provide a voice effect (chipmunk, echo, deep, etc.)")
        return
    await voice_commands.apply_effect(command, message)

if __name__ == "__main__":
    bot.run()