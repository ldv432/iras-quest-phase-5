import React, { useEffect, useState } from "react"
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom"
import LoginPage from "./LoginPage"
import SignupPage from "./SignupPage"
import GamePage from "./GamePage"
import PostsPage from "./PostsPage"
import WelcomePage from "./WelcomePage"
import toast, { Toaster } from "react-hot-toast"
import Navbar from "./Navbar"

function App() {
  const [currentUser, setCurrentUser] = useState(null)
  const [loading, setLoading] = useState(true)

  const updateCurrentUser = (value) => setCurrentUser(value)

  

  useEffect(() => {
    fetch("/current-user", { credentials: "include" })
      .then((res) => {
        if (res.ok) {
          res.json().then((data) => setCurrentUser(data))
        }
      })
      .catch((err) => console.error("Error checking user:", err))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <div>Loading...</div>

  return (
    <Router>
      {currentUser && <Navbar currentUser={currentUser} setCurrentUser={setCurrentUser} />}
      <Toaster />
      <Routes>
        <Route path="/" element={<WelcomePage currentUser={currentUser} />} />
        {!currentUser && (
          <>
            <Route path="/login" element={<LoginPage updateCurrentUser={updateCurrentUser} />} />
            <Route path="/signup" element={<SignupPage updateCurrentUser={updateCurrentUser} />} />
          </>
        )}
        {currentUser && (
          <>
            <Route path="/login" element={<Navigate to="/login" />} />
            <Route path="/signup" element={<Navigate to="/signup" />} />
          </>
        )}
        <Route path="/game" element={<GamePage />} />
        <Route path="/posts" element={<PostsPage />} />
        <Route path="*" element={<Navigate to="/" />} />
      </Routes>
    </Router>
  )
}

export default App
