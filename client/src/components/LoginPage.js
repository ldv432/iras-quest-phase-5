import React, { useState } from "react"
import { Box, Typography, TextField, Button, Alert } from "@mui/material"
import castleImage from "../assets/pictures/Splash.png"

function LoginPage() {
  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [error, setError] = useState(null)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)

    try {
      const r = await fetch("http://localhost:5000/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ email, password }),
      })

      const data = await r.json()
      if (!r.ok) throw new Error(data.error || "Failed to log in")

      console.log("Login successful:", data)
      // Redirect or update state based on successful login
    } catch (err) {
      setError(err.message)
    }
  }

  return (
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
      <Box>
        <img
          src={castleImage}
          alt="Ira's Quest Castle"
          style={{
            width: "700px",
            height: "700px",
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
          width: "300px",
          p: 3,
          borderRadius: "8px",
          boxShadow: "0 4px 10px rgba(0, 0, 0, 0.2)",
          bgcolor: "white",
        }}
      >
        <Typography variant="h4" sx={{ mb: 2, textAlign: "center" }}>
          Log In
        </Typography>

        {error && <Alert severity="error">{error}</Alert>}

        <TextField
          type="email"
          placeholder="Enter your email"
          variant="outlined"
          size="small"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          fullWidth
          required
        />

        <TextField
          type="password"
          placeholder="Enter your password"
          variant="outlined"
          size="small"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          fullWidth
          required
        />

        <Button
          type="submit"
          variant="contained"
          color="primary"
          sx={{ mt: 2, borderRadius: "8px", fontWeight: "bold" }}
        >
          Log In
        </Button>
        <Typography sx={{ textAlign: "center", mt: 2 }}>
          Don't have an account?{" "}
          <a href="/signup" style={{ textDecoration: "none", color: "#1976d2" }}>
            Sign up here!
          </a>
        </Typography>
      </Box>
    </Box>
  )
}

export default LoginPage
