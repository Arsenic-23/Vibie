import json
import os

# Define the path for storing playlists
PLAYLISTS_FILE = "playlists.json"

# Ensure the file exists
if not os.path.exists(PLAYLISTS_FILE):
    with open(PLAYLISTS_FILE, "w") as f:
        json.dump({}, f)


# Function to load playlists
def load_playlists():
    with open(PLAYLISTS_FILE, "r") as f:
        return json.load(f)


# Function to save playlists
def save_playlists(playlists):
    with open(PLAYLISTS_FILE, "w") as f:
        json.dump(playlists, f, indent=4)


# Function to add a song to a user's playlist
def add_to_playlist(user_id, song_name, song_url):
    playlists = load_playlists()
    
    if str(user_id) not in playlists:
        playlists[str(user_id)] = []
    
    playlists[str(user_id)].append({"name": song_name, "url": song_url})
    
    save_playlists(playlists)
    return f"✅ **{song_name}** has been added to your playlist!"


# Function to remove a song from a playlist
def remove_from_playlist(user_id, song_name):
    playlists = load_playlists()
    
    if str(user_id) in playlists:
        playlists[str(user_id)] = [song for song in playlists[str(user_id)] if song["name"] != song_name]
        save_playlists(playlists)
        return f"🗑️ **{song_name}** has been removed from your playlist."
    else:
        return "❌ You don't have any songs in your playlist."


# Function to get a user's playlist
def get_playlist(user_id):
    playlists = load_playlists()
    
    if str(user_id) in playlists and playlists[str(user_id)]:
        playlist_text = "🎵 **Your Playlist:**\n\n"
        for idx, song in enumerate(playlists[str(user_id)], start=1):
            playlist_text += f"{idx}. [{song['name']}]({song['url']})\n"
        return playlist_text
    else:
        return "❌ Your playlist is empty!"


# Function to clear a user's playlist
def clear_playlist(user_id):
    playlists = load_playlists()
    
    if str(user_id) in playlists:
        del playlists[str(user_id)]
        save_playlists(playlists)
        return "🗑️ Your playlist has been cleared."
    else:
        return "❌ You don't have a playlist to clear."