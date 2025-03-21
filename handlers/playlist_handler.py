from pyrogram import Client, filters
from config import MONGO_URI
from pymongo import MongoClient

# Initialize MongoDB
mongo_client = MongoClient(MONGO_URI)
db = mongo_client["music_bot"]
playlists_collection = db["playlists"]

# Function to save a playlist
def save_playlist(user_id, name, songs):
    playlists_collection.update_one(
        {"user_id": user_id, "name": name},
        {"$set": {"songs": songs}},
        upsert=True
    )

# Function to get a playlist
def get_playlist(user_id, name):
    playlist = playlists_collection.find_one({"user_id": user_id, "name": name})
    return playlist["songs"] if playlist else None

# Command: /saveplaylist
@Client.on_message(filters.command("saveplaylist") & filters.private)
async def save_playlist_command(client, message):
    user_id = message.from_user.id
    args = message.text.split(" ", 2)

    if len(args) < 3:
        return await message.reply_text("⚠️ Usage: `/saveplaylist <name> <song1>, <song2>, ...`")

    name = args[1]
    songs = args[2].split(", ")

    save_playlist(user_id, name, songs)
    await message.reply_text(f"✅ Playlist **{name}** saved successfully!")

# Command: /loadplaylist
@Client.on_message(filters.command("loadplaylist") & filters.private)
async def load_playlist_command(client, message):
    user_id = message.from_user.id
    args = message.text.split(" ", 1)

    if len(args) < 2:
        return await message.reply_text("⚠️ Usage: `/loadplaylist <name>`")

    name = args[1]
    songs = get_playlist(user_id, name)

    if songs:
        await message.reply_text(f"🎶 **{name} Playlist:**\n" + "\n".join(songs))
    else:
        await message.reply_text("⚠️ Playlist not found!")

# Command: /deleteplaylist
@Client.on_message(filters.command("deleteplaylist") & filters.private)
async def delete_playlist_command(client, message):
    user_id = message.from_user.id
    args = message.text.split(" ", 1)

    if len(args) < 2:
        return await message.reply_text("⚠️ Usage: `/deleteplaylist <name>`")

    name = args[1]
    playlists_collection.delete_one({"user_id": user_id, "name": name})

    await message.reply_text(f"🗑️ Playlist **{name}** deleted successfully!")