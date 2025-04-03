class SongQueue:
    def __init__(self):
        self.queue = []
    
    def add_song(self, name, url):
        """Adds a song to the queue."""
        self.queue.append({"name": name, "url": url})
    
    def next_song(self):
        """Returns the next song and removes it from the queue."""
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def clear(self):
        """Clears the song queue."""
        self.queue = []
    
    def get_queue(self):
        """Returns the current song queue."""
        return self.queue

