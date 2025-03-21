import pymongo
import os

# Load MongoDB URI from environment variables
MONGO_URI = os.getenv("MONGO_URI", "your_mongodb_uri_here")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_URI)
db = client["music_bot"]  # Database name

# Collections
users_collection = db["users"]
groups_collection = db["groups"]
queue_collection = db["queue"]

# Function to add a user to the database
def add_user(user_id, username):
    if not users_collection.find_one({"user_id": user_id}):
        users_collection.insert_one({"user_id": user_id, "username": username})
        
# Function to check if a user exists
def is_user_registered(user_id):
    return users_collection.find_one({"user_id": user_id}) is not None

# Function to add a group to the database
def add_group(chat_id, chat_name):
    if not groups_collection.find_one({"chat_id": chat_id}):
        groups_collection.insert_one({"chat_id": chat_id, "chat_name": chat_name})
        
# Function to check if a group exists
def is_group_registered(chat_id):
    return groups_collection.find_one({"chat_id": chat_id}) is not None

# Function to add a song to queue
def add_to_queue(chat_id, song_name, song_url):
    queue_collection.insert_one({"chat_id": chat_id, "song_name": song_name, "song_url": song_url})

# Function to get the current queue
def get_queue(chat_id):
    return list(queue_collection.find({"chat_id": chat_id}))

# Function to clear the queue
def clear_queue(chat_id):
    queue_collection.delete_many({"chat_id": chat_id})