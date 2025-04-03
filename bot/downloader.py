import yt_dlp
import os

def download_audio(song_name):
    """Downloads the best audio version of a song using yt-dlp."""
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s',
        'noplaylist': True,
        'quiet': True,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f'ytsearch:{song_name}', download=True)
            if 'entries' in info and len(info['entries']) > 0:
                return os.path.abspath(ydl.prepare_filename(info['entries'][0]))
        except Exception as e:
            print(f"Download failed: {e}")
    return None

