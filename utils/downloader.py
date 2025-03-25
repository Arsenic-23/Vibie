import yt_dlp
import os
import logging
from config import DOWNLOAD_DIR

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure the download directory exists
if not os.path.exists(DOWNLOAD_DIR):
    os.makedirs(DOWNLOAD_DIR)

def download_song(url: str, song_title: str) -> str:
    """Download song from the given URL and return the file path."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'extractaudio': True,  # Only extract audio
        'audioquality': 1,     # Best audio quality
        'outtmpl': os.path.join(DOWNLOAD_DIR, f'{song_title}.%(ext)s'),
        'restrictfilenames': True,  # Remove any special characters from filenames
        'quiet': False,            # Show progress
        'postprocessors': [{       # Post-process to convert to mp3
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        # Use yt-dlp to download the song
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)
            song_file = file_path.replace(info_dict['ext'], 'mp3')  # Replace file extension
            logger.info(f"Downloaded song: {song_file}")
            return song_file
    except Exception as e:
        logger.error(f"Error downloading song: {e}")
        return None

def get_video_url(search_query: str) -> str:
    """Search YouTube for the song and return the URL."""
    search_url = f"https://www.youtube.com/results?search_query={search_query.replace(' ', '+')}"
    
    ydl_opts = {
        'quiet': True,
        'extract_flat': True,  # Get the URL of the first result without downloading
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(search_url, download=False)
            video_url = f"https://www.youtube.com/watch?v={info_dict['entries'][0]['id']}"
            logger.info(f"Found video URL: {video_url}")
            return video_url
    except Exception as e:
        logger.error(f"Error searching for video: {e}")
        return None

def download_from_search(query: str) -> str:
    """Search for the song on YouTube and download it."""
    video_url = get_video_url(query)
    if video_url:
        song_title = query.split(" ")[0]  # Using the first word of the query as the title (can be changed)
        return download_song(video_url, song_title)
    else:
        return None