import os
import telebot

# Load environment variables
API_ID = os.getenv("API_ID")
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Initialize the bot
bot = telebot.TeleBot(BOT_TOKEN)

# Start Command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🎵 Welcome to the Music Bot! Type /play to start.")

# Play Command (Placeholder)
@bot.message_handler(commands=['play'])
def play_music(message):
    bot.reply_to(message, "🎶 Playing music... (Feature coming soon!)")

# Run the bot
bot.polling()
