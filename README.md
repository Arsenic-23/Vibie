# Vibie - A Powerful Telegram Music Bot

Vibie is an advanced, feature-packed Telegram music bot designed for seamless music playback, lyrics synchronization, playlist management, and more. This bot supports MPV and FFmpeg for high-quality audio streaming, automatic lyrics syncing, and a premium user experience.

## Features
- **Music Playback**: Play, pause, skip, and control the volume of music in group voice chats.
- **Lyrics Sync**: Displays lyrics in sync with the currently playing song.
- **Playlist Management**: Users and admins can create, view, and manage playlists and queues.
- **Admin Controls**: Admins can skip songs, manage playlists, and control who can play music.
- **Voice Filters**: Includes multiple voice filters to enhance the music experience.
- **AI Jukebox**: A feature to automatically recommend and play music.
- **Queue System**: Multiple songs can be added to the queue for continuous playback.
- **Premium UI**: Clean and modern user interface with song thumbnails, lyrics, and more.

## Requirements

1. **Python 3.x** (preferably Python 3.8 or higher)
2. **FFmpeg**: Make sure FFmpeg is installed and accessible in the system path.
3. **Telegram Bot API Token**: Create a bot using [BotFather](https://core.telegram.org/bots#botfather) and get the API token.

## Installation

1. **Clone the Repository**:

2. Install Dependencies:

Use the following command to install all required Python libraries:

pip install -r requirements.txt


3. Configure the Bot:

Edit the config.py file to add your Telegram bot token and other configuration settings.

# config.py
BOT_TOKEN = "your-telegram-bot-api-token"


4. Install FFmpeg:

Download FFmpeg and ensure it's available in your system's PATH.



5. Run the Bot:

Once everything is set up, you can start the bot with the following command:

python main.py


6. Enjoy the Bot:

Your bot should now be up and running! You can interact with it by typing /help to get a list of available commands.



Commands

Music Commands:

/play [song_name or URL]: Play a song in the voice chat.

/pause: Pause the currently playing song.

/resume: Resume the paused song.

/skip: Skip to the next song in the queue.

/queue: Show the current song queue.

/volume [level]: Adjust the volume of the music playback.

/lyrics: Display the lyrics of the currently playing song.


Admin Commands:

/add_playlist [playlist_name]: Create a new playlist.

/remove_playlist [playlist_name]: Delete an existing playlist.

/add_to_playlist [playlist_name] [song_name]: Add a song to a playlist.

/remove_from_playlist [playlist_name] [song_name]: Remove a song from a playlist.

/clear_queue: Clear the current song queue.

/force_skip: Skip the current song without a vote (Admin only).

/set_admin [user_id]: Grant admin privileges to a user.


Other Commands:

/start: Start the bot and receive an introduction.

/help: Display the list of available commands.

/about: Get information about the bot and its features.


Configuration Files

config.py: Stores the bot token and other essential configurations.

playlist_data.json: Stores data about created playlists and the song queue.

user_data.json: Stores user-specific preferences and data.


Contributing

Feel free to fork the repository, create a pull request, or report any issues. Contributions are always welcome!

License

This bot is open-source and free to use. However, ensure that you follow the respective licenses for any libraries and platforms integrated with the bot (e.g., YouTube, FFmpeg).

Support

For any issues, please check the GitHub Issues or reach out to the bot's maintainers.

### **Explanation of the README Structure**:
1. **Introduction**: Briefly introduces the bot and its purpose.
2. **Features**: Lists all the functionalities of the bot (e.g., music playback, lyrics sync, etc.).
3. **Requirements**: Lists necessary software and dependencies for the bot to work.
4. **Installation**: Provides detailed steps on how to set up the bot on a local machine or server.
5. **Commands**: Lists all the commands available for users and admins, such as play, pause, skip, and manage playlists.
6. **Configuration**: Instructions for setting up configuration files like `config.py` for API tokens and preferences.
7. **Contributing**: Encourages contributions to the project.
8. **License**: Information about the open-source nature of the bot.
9. **Support**: Provides information on how users can seek help or

