class SongQueue:
    def __init__(self):
        self.queue = []
    
    def add_song(self, song_name, song_url):
        self.queue.append({"name": song_name, "url": song_url})
    
    def next_song(self):
        if self.queue:
            return self.queue.pop(0)
        return None
    
    def get_queue(self):
        return self.queue
    
    def clear(self):
        self.queue = []

queue = SongQueue()
