import { useState } from "react";
import {
  Moon,
  Sun,
  Heart,
  Home,
  Search,
  User,
  Flame,
  Play,
  Pause,
  SkipForward,
  Users,
  ListMusic,
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

export default function App() {
  const [darkMode, setDarkMode] = useState(true);
  const [joined, setJoined] = useState(false);
  const [liked, setLiked] = useState(false);
  const [playing, setPlaying] = useState(false);
  const [page, setPage] = useState("home");
  const [profileTab, setProfileTab] = useState("stats");

  const themeClass = darkMode ? "bg-black text-white" : "bg-white text-black";
  const orbitronFont = "font-[Orbitron,sans-serif]";

  const navItem = (icon, label, pageName) => (
    <button
      onClick={() => setPage(pageName)}
      className={`flex flex-col items-center text-xs transition ${
        page === pageName ? "text-pink-400" : "text-white"
      }`}
    >
      {icon}
      {label}
    </button>
  );

  const renderFrontPage = () => (
    <div
      className={`${themeClass} h-screen flex flex-col justify-center items-center px-6 relative`}
    >
      <div className="absolute inset-0 bg-gradient-to-br from-purple-600 via-pink-600 to-indigo-600 animate-pulse blur-3xl opacity-30"></div>
      <div className="z-10 text-center space-y-8">
        <h1 className={`text-6xl font-extrabold ${orbitronFont}`}>Astral ✨</h1>
        <p className="text-lg text-gray-300">Music from the cosmos</p>
        <button
          onClick={() => setJoined(true)}
          className="mt-4 px-8 py-3 text-lg font-medium rounded-full bg-blue-600 hover:bg-blue-500 transition"
        >
          Join Stream 🚀
        </button>
      </div>
    </div>
  );

  const renderSearchPage = () => (
    <div className="p-6">
      <h2 className="text-2xl font-semibold mb-4">Search</h2>
      <input
        type="text"
        placeholder="Search for songs, artists..."
        className="w-full p-4 rounded-xl bg-gray-800 text-white placeholder-gray-400 shadow-inner focus:outline-none focus:ring-2 focus:ring-pink-500"
      />
    </div>
  );

  const renderHitsPage = () => (
    <div className="p-6 text-center">
      <h2 className="text-3xl font-bold mb-2">Trending Hits 🔥</h2>
      <p className="text-gray-400">Coming soon...</p>
    </div>
  );

  const renderQueuePage = () => (
    <div className="p-6">
      <h2 className="text-3xl font-bold mb-4">Up Next ⏭️</h2>
      <ul className="space-y-4">
        <li className="bg-gray-800 p-4 rounded-xl shadow-md">
          01. Galaxy Flow – Starbeat
        </li>
        <li className="bg-gray-800 p-4 rounded-xl shadow-md">
          02. Nightdrive – Orion Echo
        </li>
        <li className="bg-gray-800 p-4 rounded-xl shadow-md">
          03. Starlight Dreams – Vega Vibes
        </li>
      </ul>
    </div>
  );

  const renderProfileTabs = () => {
    const tabs = ["stats", "history", "favourites"];
    return (
      <div className="flex justify-center gap-4 my-4">
        {tabs.map((tab) => (
          <button
            key={tab}
            onClick={() => setProfileTab(tab)}
            className={`px-4 py-2 rounded-full transition ${
              profileTab === tab
                ? "bg-pink-500 text-white"
                : "bg-gray-800 text-gray-300 hover:bg-gray-700"
            }`}
          >
            {tab.charAt(0).toUpperCase() + tab.slice(1)}
          </button>
        ))}
      </div>
    );
  };

  const renderProfileTabContent = () => {
    switch (profileTab) {
      case "stats":
        return (
          <p className="text-gray-300 mt-4">
            You’ve listened to 1,234 minutes this week.
          </p>
        );
      case "history":
        return (
          <ul className="mt-4 space-y-2 text-left text-gray-400">
            <li>• Galaxy Flow – Starbeat</li>
            <li>• Orion Echo – Nightdrive</li>
            <li>• Cosmic Drift – Lost in the Stars</li>
          </ul>
        );
      case "favourites":
        return (
          <ul className="mt-4 space-y-2 text-left text-gray-400">
            <li>❤️ Starlight Dreams – Vega Vibes</li>
            <li>❤️ Aurora Bloom – Nova Pulse</li>
          </ul>
        );
      default:
        return null;
    }
  };

  const renderProfilePage = () => (
    <div className="p-6 text-center">
      <h2 className="text-3xl font-bold mb-2">Your Profile 👤</h2>
      {renderProfileTabs()}
      {renderProfileTabContent()}
    </div>
  );

  const renderPlayerPage = () => (
    <div className="flex flex-col items-center px-6 mt-6 pb-32 relative z-10">
      <img
        src="https://via.placeholder.com/500"
        alt="Song Thumbnail"
        className="rounded-3xl w-96 h-96 object-cover shadow-2xl"
      />
      <h2 className="text-3xl font-semibold mt-6">Lost in the Stars</h2>
      <p className="text-md text-gray-400">by Cosmic Drift</p>

      <div className="flex items-center gap-10 mt-8">
        <motion.button
          onClick={() => setLiked(!liked)}
          className={`p-4 rounded-full ${
            liked ? "bg-pink-600" : "bg-gray-700"
          } hover:scale-110 shadow-xl relative`}
        >
          <Heart
            fill={liked ? "white" : "none"}
            className="text-white w-6 h-6 z-10 relative"
          />
          <AnimatePresence>
            {liked && (
              <motion.div
                initial={{ opacity: 0, y: 0, scale: 0.5 }}
                animate={{ opacity: 1, y: -40, scale: 1 }}
                exit={{ opacity: 0, y: -60, scale: 0 }}
                transition={{ duration: 0.6 }}
                className="absolute top-0 left-1/2 transform -translate-x-1/2 text-pink-500 text-2xl"
              >
                ❤️
              </motion.div>
            )}
          </AnimatePresence>
        </motion.button>

        <button
          onClick={() => setPlaying(!playing)}
          className="p-6 rounded-full bg-blue-600 hover:bg-blue-500 shadow-xl transition transform hover:scale-110"
        >
          {playing ? <Pause className="w-8 h-8" /> : <Play className="w-8 h-8" />}
        </button>

        <button className="p-4 rounded-full bg-gray-800 hover:bg-gray-700 shadow-xl">
          <SkipForward className="w-6 h-6" />
        </button>
      </div>
    </div>
  );

  const renderContent = () => {
    switch (page) {
      case "search":
        return renderSearchPage();
      case "hits":
        return renderHitsPage();
      case "queue":
        return renderQueuePage();
      case "profile":
        return renderProfilePage();
      default:
        return renderPlayerPage();
    }
  };

  if (!joined) return renderFrontPage();

  return (
    <div
      className={`${themeClass} min-h-screen transition-all duration-500 relative`}
    >
      <div className="absolute inset-0 bg-gradient-to-br from-indigo-700 via-purple-700 to-pink-700 animate-pulse blur-3xl opacity-20"></div>

      <div className="flex justify-between items-center px-5 pt-4 z-10">
        <h2 className={`text-3xl font-bold ${orbitronFont}`}>Astral ✨</h2>
        <div className="flex items-center gap-4">
          <button
            className="flex items-center gap-2 px-3 py-1 rounded-full bg-gray-800 hover:bg-gray-700 text-sm"
            onClick={() => alert("Participants view coming soon")}
          >
            <Users className="w-4 h-4" />
            Participants
          </button>
          <button
            onClick={() => setDarkMode(!darkMode)}
            className="p-2 rounded-full hover:bg-gray-800 transition"
          >
            {darkMode ? (
              <Sun className="text-yellow-300" />
            ) : (
              <Moon className="text-gray-800" />
            )}
          </button>
        </div>
      </div>

      <main className="z-10">{renderContent()}</main>

      <nav className="fixed bottom-0 left-0 right-0 flex justify-around bg-black/80 border-t border-gray-700 py-3 z-20 backdrop-blur-md">
        {navItem(<Home className="h-5 w-5" />, "Home", "home")}
        {navItem(<Search className="h-5 w-5" />, "Search", "search")}
        {navItem(<Flame className="h-5 w-5" />, "Hits", "hits")}
        {navItem(<ListMusic className="h-5 w-5" />, "Queue", "queue")}
        {navItem(<User className="h-5 w-5" />, "Profile", "profile")}
      </nav>
    </div>
  );
}