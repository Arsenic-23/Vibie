from fastapi import FastAPI, HTTPException
from database import queue
from streaming import start_stream, stop_stream
from pydantic import BaseModel

app = FastAPI()

class SongRequest(BaseModel):
    song_name: str
    song_url: str

@app.post("/add_to_queue")
def add_to_queue(song: SongRequest):
    queue.add_song(song.song_name, song.song_url)
    if len(queue.get_queue()) == 1:
        start_stream(song.song_url)
    return {"message": f"{song.song_name} added to queue"}

@app.post("/skip")
def skip_song():
    next_song = queue.next_song()
    if next_song:
        start_stream(next_song["url"])
        return {"message": f"Skipping... Now playing {next_song['name']}"}
    else:
        stop_stream()
        return {"message": "Queue is empty, stopping stream"}

@app.post("/stop")
def stop():
    queue.clear()
    stop_stream()
    return {"message": "Stream stopped"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
