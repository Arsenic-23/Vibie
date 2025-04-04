import { useState, useEffect, useContext } from "react";
import { ThemeContext } from "../context/ThemeContext";
import { initTelegramLogin } from "../utils/telegramAuth";
import { Button } from "@/components/ui";

export default function Profile() {
    const { theme, setTheme } = useContext(ThemeContext);
    const [user, setUser] = useState(null);
    const [stats, setStats] = useState({ totalHours: 0, dailyHours: 0, topArtist: "", favoriteSongs: [] });

    useEffect(() => {
        initTelegramLogin((userData) => setUser(userData));

        fetch("http://localhost:8000/user/stats")
            .then(res => res.json())
            .then(data => setStats(data));
    }, []);

    return (
        <div className="p-4">
            <h1 className="text-xl font-bold">Profile</h1>
            {user ? (
                <div className="flex items-center gap-4">
                    <img src={user.photo_url} alt="Profile" className="w-20 h-20 rounded-full" />
                    <div>
                        <h2 className="text-lg">{user.first_name} {user.last_name}</h2>
                        <p>@{user.username}</p>
                    </div>
                </div>
            ) : (
                <div id="telegram-login-container"></div>
            )}

            <h2 className="mt-4 text-lg font-bold">Stats</h2>
            <p>Total Hours: {stats.totalHours}</p>
            <p>Daily Hours: {stats.dailyHours}</p>
            <p>Top Artist: {stats.topArtist}</p>
            <h3 className="mt-2">Favorite Songs:</h3>
            <ul>
                {stats.favoriteSongs.map((song, index) => (
                    <li key={index}>{song}</li>
                ))}
            </ul>

            <Button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>Toggle Theme</Button>
        </div>
    );
}