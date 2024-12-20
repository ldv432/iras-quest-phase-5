import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Typography, TextField, Button, Alert } from "@mui/material";
import castleImage from "../assets/pictures/Splash.png";
import Navbar from "./Navbar";

function SignUpPage() {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState(null);
  const [success, setSuccess] = useState(null);

  const nav = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setSuccess(null);

    try {
      const response = await fetch("/signup", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, username, password }),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.error || "Failed to sign up");

      setSuccess("Account created successfully!");
      setTimeout(() => nav("/posts"), 1000);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <>
      <Navbar />
      <Box
        sx={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          minHeight: "100vh",
          bgcolor: "#f5f5f5",
          gap: 4,
          px: 4,
        }}
      >
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

        <Box
          component="form"
          onSubmit={handleSubmit}
          sx={{
            display: "flex",
            flexDirection: "column",
            gap: 2,
            width: "350px",
            p: 3,
            borderRadius: "8px",
            boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)",
            bgcolor: "white",
          }}
        >
          <Typography variant="h4" sx={{ textAlign: "center", mb: 1 }}>
            Sign Up
          </Typography>

          {error && <Alert severity="error">{error}</Alert>}
          {success && <Alert severity="success">{success}</Alert>}

          <TextField
            label="Enter your e-mail"
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your e-mail"
            variant="outlined"
            size="small"
            fullWidth
            required
          />

          <TextField
            label="Enter a username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter a username"
            variant="outlined"
            size="small"
            fullWidth
            required
          />

          <TextField
            label="Choose a password"
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Choose a password"
            variant="outlined"
            size="small"
            fullWidth
            required
          />

          <Button
            type="submit"
            variant="contained"
            color="primary"
            sx={{
              mt: 2,
              borderRadius: "8px",
              fontWeight: "bold",
            }}
          >
            Sign Up
          </Button>
          <Typography sx={{ textAlign: "center", mt: 2 }}>
            Already have an account?{" "}
            <a
              href="/login"
              style={{ textDecoration: "none", color: "#1976d2" }}
            >
              Log in here!
            </a>
          </Typography>
        </Box>
      </Box>
    </>
  );
}

export default SignUpPage;
