import React from "react"
import { useNavigate } from "react-router-dom"
import castleImage from "../assets/pictures/Splash.png"
import { CssVarsProvider } from "@mui/joy/styles"
import Sheet from "@mui/joy/Sheet"
import Typography from "@mui/joy/Typography"
import Button from "@mui/joy/Button"

function WelcomePage() {
  const nav = useNavigate()

  const handleLogin = () => {
    nav("/login")
  }

  const handleSignup = () => {
    nav("/signup")
  }

  return (
    <CssVarsProvider>
      <div
        style={{
          display: "flex",
          flexDirection: "row",
          alignItems: "center",
          justifyContent: "center",
          minHeight: "100vh",
          gap: "2rem",
          backgroundColor: "#f5f5f5",
          padding: "2rem",
        }}
      >
        <img
          src={castleImage}
          alt="Ira's Quest Castle"
          style={{
            width: "700px",
            height: "700px",
            objectFit: "cover",
          }}
        />
        <Sheet
          sx={{
            width: 500,
            py: 2,
            px: 2,
            display: "flex",
            flexDirection: "column",
            gap: 2,
            borderRadius: "sm",
            boxShadow: "md",
            alignItems: "center",
          }}
        >
          <Typography level="h1" component="h1">
            Welcome to Ira's Quest!
          </Typography>
          <Typography level="body1" sx={{ textAlign: "center" }}>
            In order to play the game, you'll need to log in or sign up.
          </Typography>
          <div style={{ display: "flex", gap: "1rem" }}>
            <Button
              variant="solid"
              color="primary"
              size="lg"
              onClick={handleLogin}
            >
              Log In
            </Button>
            <Button
              variant="soft"
              color="neutral"
              size="lg"
              onClick={handleSignup}
            >
              Sign Up
            </Button>
          </div>
        </Sheet>
      </div>
    </CssVarsProvider>
  )
}

export default WelcomePage
