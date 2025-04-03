// frontend/src/pages/Home.js

import React from "react"; import { useNavigate } from "react-router-dom";

const Home = () => { const navigate = useNavigate();

return (
    <div>
        <h1>Welcome to the Telegram Music App</h1>
        <button onClick={() => navigate("/stream")}>
            Join Stream
        </button>
    </div>
);

};

export default Home;

