// frontend/src/pages/Stream.js

import React, { useEffect, useState } from "react"; import Player from "../components/Player"; import { fetchQueue } from "../api";

const Stream = () => { const [queue, setQueue] = useState([]);

useEffect(() => {
    const loadQueue = async () => {
        const data = await fetchQueue();
        setQueue(data);
    };
    loadQueue();
}, []);

return (
    <div>
        <h2>Live Stream</h2>
        {queue.length > 0 ? (
            <Player currentSong={queue[0]} />
        ) : (
            <p>No songs in queue</p>
        )}
    </div>
);

};

export default Stream;

