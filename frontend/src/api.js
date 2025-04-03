// frontend/src/api.js

const API_URL = process.env.REACT_APP_BACKEND_URL || "http://localhost:5000";

// Fetch current song queue
export const fetchQueue = async () => {
    const response = await fetch(`${API_URL}/queue`);
    return response.json();
};

// Send play command to backend
export const playSong = async (songName) => {
    const response = await fetch(`${API_URL}/play`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ song_name: songName })
    });
    return response.json();
};

// Skip current song
export const skipSong = async () => {
    const response = await fetch(`${API_URL}/skip`, { method: "POST" });
    return response.json();
};

// Stop the stream
export const stopStream = async () => {
    const response = await fetch(`${API_URL}/stop`, { method: "POST" });
    return response.json();
};
