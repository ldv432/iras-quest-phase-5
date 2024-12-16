import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LoginPage from "./LoginPage";
import SignupPage from "./SignupPage";
// import GamePage from "./Game";
// import PostsPage from "./Posts";
import IrasQuest from "../assets/music/IrasQuest.ogg"
import WelcomePage from "./WelcomePage";
import toast, { Toaster } from "react-hot-toast"

function App() {

 

  return (
    <Router>
      <Routes>
        <Route path="/" element={<WelcomePage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/signup" element={<SignupPage />} />
        {/* <Route path="/game" element={<GamePage />} />
        <Route path="/forum" element={<PostsPage />} /> */}
      </Routes>
    </Router>
  );
}

export default App;