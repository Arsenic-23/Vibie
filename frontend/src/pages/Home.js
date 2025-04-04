import { useState, useEffect } from "react";
import MusicPlayer from "@/components/MusicPlayer";
import Queue from "@/components/Queue";
import SearchBar from "@/components/SearchBar";

export default function Home() {
    const [songs, setSongs] = useState([]);
    const [filteredSongs, setFilteredSongs] = useState([]);
    const [currentSong, setCurrentSong] = useState(null);

    useEffect(() => {
        fetch("http://localhost:8000/songs")
            .then(res => res.json())
            .then(data => {
                setSongs(data);
                setFilteredSongs(data);
                setCurrentSong(data[0]); 
            });
    }, []);

    const handleSearch = (query) => {
        const filtered = songs.filter(song =>
            song.title.toLowerCase().includes(query.toLowerCase()) ||
            song.artist.toLowerCase().includes(query.toLowerCase())
        );
        setFilteredSongs(filtered);
    };

    return (
        <div className="p-6 flex flex-col gap-4">
            <SearchBar onSearch={handleSearch} />
            {currentSong && <MusicPlayer track={currentSong} />}
            <Queue queue={filteredSongs} onSelect={setCurrentSong} />
        </div>
    );
}
