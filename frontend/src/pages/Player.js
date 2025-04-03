// frontend/src/components/Player.js

import React, { useEffect, useState } from "react";

const Player = ({ currentSong }) => { const [audio, setAudio] = useState(null);

useEffect(() => {
    if (currentSong) {
        const newAudio = new Audio(currentSong.url);
        setAudio(newAudio);
        newAudio.play();
    }

    return () => {
        if (audio) {
            audio.pause();
            audio.src = "";
        }
    };
}, [currentSong]);

return (
    <div>
        <h3>Now Playing: {currentSong ? currentSong.name : "None"}</h3>
        {currentSong && <p>Streaming...</p>}
    </div>
);

};

export default Player;

