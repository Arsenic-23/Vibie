import os
import subprocess
import logging
import asyncio
from config import DOWNLOAD_DIR
from utils.downloader import download_song
from utils.lyrics_handler import get_lyrics
from asyncio import TimeoutError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the music cache folder and file name for the currently playing song
CACHE_DIR = './cache'
CURRENT_SONG_FILE = os.path.join(CACHE_DIR, 'current_song.mp3')

# Ensure the cache directory exists
if not os.path.exists(CACHE_DIR):
    os.makedirs(CACHE_DIR)

# Global variables for playback control
is_playing = False
current_process = None

def play_audio(song_file: str) -> None:
    """Plays the audio file using MPV and FFmpeg."""
    global current_process, is_playing

    if is_playing:
        logger.info("A song is already playing.")
        return
    
    try:
        # Start the FFmpeg/MPV process to play the audio in the voice chat
        logger.info(f"Playing song: {song_file}")
        current_process = subprocess.Popen(
            ['ffmpeg', '-re', '-i', song_file, '-vn', '-acodec', 'libmp3lame', '-f', 'mp3', '-'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        is_playing = True
        logger.info(f"Playback started: {song_file}")
    except Exception as e:
        logger.error(f"Error while playing audio: {e}")
        is_playing = False

def stop_audio() -> None:
    """Stops the currently playing song."""
    global current_process, is_playing

    if not is_playing:
        logger.info("No song is currently playing.")
        return
    
    try:
        current_process.terminate()
        is_playing = False
        logger.info("Playback stopped.")
    except Exception as e:
        logger.error(f"Error stopping playback: {e}")

def pause_audio() -> None:
    """Pauses the currently playing song."""
    global current_process, is_playing

    if not is_playing:
        logger.info("No song is currently playing.")
        return
    
    try:
        current_process.send_signal(subprocess.signal.SIGSTOP)
        is_playing = False
        logger.info("Playback paused.")
    except Exception as e:
        logger.error(f"Error pausing playback: {e}")

def resume_audio() -> None:
    """Resumes the currently paused song."""
    global current_process, is_playing

    if is_playing:
        logger.info("Song is already playing.")
        return
    
    try:
        current_process.send_signal(subprocess.signal.SIGCONT)
        is_playing = True
        logger.info("Playback resumed.")
    except Exception as e:
        logger.error(f"Error resuming playback: {e}")

def skip_audio() -> None:
    """Skips the currently playing song."""
    stop_audio()
    logger.info("Skipping to next song.")
    # Here, you could integrate a feature for adding the next song to the queue.
    # For now, simply stopping playback is sufficient.

async def fetch_and_play_song(query: str) -> str:
    """Fetch and play a song based on a search query."""
    song_file = download_song(query)
    if song_file:
        play_audio(song_file)
        return song_file
    else:
        logger.error("Error downloading the song.")
        return None

async def get_current_lyrics(song_title: str) -> str:
    """Fetches and synchronizes the lyrics with the current song."""
    try:
        lyrics = await get_lyrics(song_title)
        return lyrics
    except TimeoutError:
        logger.error("Error fetching lyrics: Request timed out.")
        return "Unable to fetch lyrics."