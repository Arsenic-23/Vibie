import yt_dlp
import os
import logging
from config import DOWNLOAD_DIR

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Ensure the download directory exists
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

def download_song(url: str, song_title: str) -> str:
    """Download song from the given URL and return the file path."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(DOWNLOAD_DIR, f'{song_title}.%(ext)s'),
        'restrictfilenames': True,  
        'postprocessors': [{
            'key': 'FFmpegAudioConvertor',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            # Fetch final file path after processing
            file_path = info_dict['requested_downloads'][0]['filepath']
            logger.info(f"Downloaded song: {file_path}")
            return file_path
    except Exception as e:
        logger.error(f"Error downloading song: {e}")
        return None

def get_video_url(search_query: str) -> str:
    """Search YouTube for the song and return the best video URL."""
    ydl_opts = {
        'quiet': True,
        'default_search': 'ytsearch',
        'noplaylist': True,
        'extract_flat': True,  
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(search_query, download=False)
            video_url = info_dict['entries'][0]['url']
            logger.info(f"Found video URL: {video_url}")
            return video_url
    except Exception as e:
        logger.error(f"Error searching for video: {e}")
        return None

def download_from_search(query: str) -> str:
    """Search for the song on YouTube and download it."""
    video_url = get_video_url(query)
    if video_url:
        return download_song(video_url, query)
    return None