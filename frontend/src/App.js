import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "@/pages/Home";
import ProfilePage from "@/pages/ProfilePage";
import ThemeProvider from "@/context/ThemeContext";

export default function App() {
    return (
        <ThemeProvider>
            <Router>
                <div className="min-h-screen bg-gray-900 text-white">
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/profile" element={<ProfilePage />} />
                    </Routes>
                </div>
            </Router>
        </ThemeProvider>
    );
}
