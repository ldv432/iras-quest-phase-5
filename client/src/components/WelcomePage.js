import React from "react";
import { useNavigate } from "react-router-dom";
import castleImage from "../assets/pictures/Splash.png";
import { Box, Typography, Button } from "@mui/material";
import Navbar from "./Navbar";

function WelcomePage({ currentUser }) {
  const nav = useNavigate();

  const handlePlay = () => {
    nav("/game");
  };

  const handlePost = () => {
    nav("/posts");
  };

  const handleLogin = () => {
    nav("/login");
  };

  const handleSignup = () => {
    nav("/signup");
  };

  return (
    <>
      <Navbar currentUser={currentUser} />
      <Box
        sx={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
          minHeight: "100vh",
          bgcolor: "#f5f5f5",
          gap: 4,
          px: 4,
          fontFamily: "Arial, sans-serif",
        }}
      >
        {/* Image Section */}
        <Box>
          <img
            src={castleImage}
            alt="Ira's Quest Castle"
            style={{
              width: "500px",
              height: "500px",
              objectFit: "cover",
            }}
          />
        </Box>

        {/* Content Section */}
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            gap: 2,
            width: "400px",
            p: 3,
            borderRadius: "8px",
            boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)",
            bgcolor: "white",
            textAlign: "center",
          }}
        >
          <Typography variant="h4" sx={{ mb: 2 }}>
            Welcome to Ira's Quest!
          </Typography>

          {currentUser ? (
            <>
              <Typography>
                Ready to play or share your thoughts about the game?
              </Typography>
              <Box sx={{ display: "flex", justifyContent: "center", gap: 2 }}>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handlePlay}
                  sx={{ borderRadius: "8px", fontWeight: "bold" }}
                >
                  Play Ira's Quest!
                </Button>
                <Button
                  variant="outlined"
                  color="primary"
                  onClick={handlePost}
                  sx={{ borderRadius: "8px", fontWeight: "bold" }}
                >
                  Post About The Game
                </Button>
              </Box>
            </>
          ) : (
            <>
              <Typography>
                In order to play the game, you'll need to log in or sign up.
              </Typography>
              <Box sx={{ display: "flex", justifyContent: "center", gap: 2 }}>
                <Button
                  variant="contained"
                  color="primary"
                  onClick={handleLogin}
                  sx={{ borderRadius: "8px", fontWeight: "bold" }}
                >
                  Log In
                </Button>
                <Button
                  variant="outlined"
                  color="primary"
                  onClick={handleSignup}
                  sx={{ borderRadius: "8px", fontWeight: "bold" }}
                >
                  Sign Up
                </Button>
              </Box>
            </>
          )}
        </Box>
      </Box>
    </>
  );
}

export default WelcomePage;
