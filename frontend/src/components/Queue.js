import { useState } from "react";
import { Button } from "@/components/ui";

export default function Queue({ queue, onSelect }) {
    const [currentSong, setCurrentSong] = useState(null);

    const handleSelect = (song) => {
        setCurrentSong(song);
        onSelect(song);
    };

    return (
        <div className="p-4 bg-gray-800 text-white rounded-xl">
            <h2 className="text-lg font-bold mb-2">Queue</h2>
            <ul>
                {queue.map((song, index) => (
                    <li key={index} className={`p-2 rounded-lg ${currentSong?.id === song.id ? "bg-blue-500" : "hover:bg-gray-700"}`}>
                        <Button onClick={() => handleSelect(song)} className="flex items-center w-full">
                            <img src={song.cover} alt={song.title} className="w-10 h-10 rounded-lg mr-3" />
                            <div className="text-left">
                                <h3 className="text-sm font-bold">{song.title}</h3>
                                <p className="text-xs text-gray-300">{song.artist}</p>
                            </div>
                        </Button>
                    </li>
                ))}
            </ul>
        </div>
    );
}