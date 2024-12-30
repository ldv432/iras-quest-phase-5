import React, { useEffect, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import { UserContext } from "./UserContext";
import LoginPage from "./LoginPage";
import SignupPage from "./SignupPage";
import GamePage from "./GamePage";
import PostsPage from "./PostsPage";
import WelcomePage from "./WelcomePage";
import Navbar from "./Navbar";

function App() {
  const [currentUser, setCurrentUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // Fetch current user on mount
  useEffect(() => {
    const storedUser = JSON.parse(localStorage.getItem("currentUser"));
    if (storedUser) {
      setCurrentUser(storedUser);
    }
  
    fetch("/current-user", { credentials: "include" })
      .then((res) => {
        if (res.ok) {
          res.json().then((data) => {
            setCurrentUser(data);
            localStorage.setItem("currentUser", JSON.stringify(data));
          });
        }
      })
      .catch((err) => console.error("Error checking user:", err))
      .finally(() => setLoading(false));
  }, []);
  
  if (loading) return <div>Loading...</div>;

  return (
    <UserContext.Provider value={{ currentUser, setCurrentUser }}>
      <Router>
        <Navbar />
        <Routes>
          {/* Routes accessible to all users */}
          <Route path="/" element={<WelcomePage />} />
          <Route path="/game" element={<GamePage />} />

          {/* Routes for logged-out users */}
          {!currentUser && (
            <>
              <Route path="/login" element={<LoginPage />} />
              <Route path="/signup" element={<SignupPage />} />
            </>
          )}

          {/* Routes for logged-in users */}
          {currentUser && (
            <>
              <Route path="/posts" element={<PostsPage />} />
              <Route path="/leaderboard" element={<div>Leaderboard</div>} />
            </>
          )}

          {/* Redirect unknown routes */}
          <Route path="*" element={<Navigate to="/" />} />
        </Routes>
      </Router>
    </UserContext.Provider>
  );
}

export default App;
