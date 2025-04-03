import subprocess

def start_stream(song_url):
    """Start streaming the given song URL using FFmpeg."""
    subprocess.Popen([
        "ffmpeg", "-re", "-i", song_url, "-acodec", "libmp3lame", "-f", "mp3", "icecast://source:password@localhost:8000/stream"
    ])

def stop_stream():
    """Stops the stream by killing FFmpeg."""
    subprocess.run(["pkill", "-f", "ffmpeg"])
