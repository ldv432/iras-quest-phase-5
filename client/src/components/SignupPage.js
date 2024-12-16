import React from "react";
import { Box, Typography, TextField, Button } from "@mui/material";
import castleImage from "../assets/pictures/Splash.png";

function SignUpPage() {
 

  return (
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
            width: "700px",
            height: "700px",
            objectFit: "cover",
          }}
        />
      </Box>

      <Box
        component="form"
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

        <TextField
          label="Enter your e-mail"
          type="email"
          placeholder="Enter your e-mail"
          variant="outlined"
          size="small"
          fullWidth
        />

        <TextField
          label="Enter a username"
          placeholder="Enter a username"
          variant="outlined"
          size="small"
          fullWidth
        />

        <TextField
          label="Choose a password"
          type="password"
          placeholder="Choose a password"
          variant="outlined"
          size="small"
          fullWidth
        />

        <Button
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
          <a href="/login" style={{ textDecoration: "none", color: "#1976d2" }}>
            Log in here!
          </a>
        </Typography>
      </Box>
    </Box>
  );
}

export default SignUpPage;
