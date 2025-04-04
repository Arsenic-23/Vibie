import { useState, useRef, useEffect } from "react";
import { Button } from "@/components/ui";
import { Play, Pause, SkipForward } from "lucide-react";

export default function MusicPlayer({ track }) {
    const [isPlaying, setIsPlaying] = useState(false);
    const [progress, setProgress] = useState(0);
    const audioRef = useRef(new Audio(track?.url));

    useEffect(() => {
        const audio = audioRef.current;
        
        const updateProgress = () => {
            setProgress((audio.currentTime / audio.duration) * 100);
        };

        audio.addEventListener("timeupdate", updateProgress);
        return () => audio.removeEventListener("timeupdate", updateProgress);
    }, []);

    const togglePlay = () => {
        const audio = audioRef.current;
        if (isPlaying) {
            audio.pause();
        } else {
            audio.play();
        }
        setIsPlaying(!isPlaying);
    };

    const skipTrack = () => {
        audioRef.current.currentTime = audioRef.current.duration;
    };

    return (
        <div className="p-4 bg-gray-900 text-white rounded-xl flex items-center gap-4">
            <img src={track?.cover} alt={track?.title} className="w-16 h-16 rounded-lg" />
            <div className="flex-grow">
                <h3 className="text-lg font-bold">{track?.title}</h3>
                <p className="text-sm">{track?.artist}</p>
                <div className="w-full bg-gray-700 rounded-full h-2 mt-2">
                    <div className="bg-blue-500 h-2 rounded-full" style={{ width: `${progress}%` }}></div>
                </div>
            </div>
            <Button onClick={togglePlay}>
                {isPlaying ? <Pause /> : <Play />}
            </Button>
            <Button onClick={skipTrack}>
                <SkipForward />
            </Button>
        </div>
    );
}