import React, { useContext } from "react";
import { UserContext } from "./UserContext";
import { AppBar, Toolbar, Typography, Box } from "@mui/material";
import { NavLink, useNavigate } from "react-router-dom";

const Navbar = () => {
  const { currentUser, setCurrentUser } = useContext(UserContext);
  console.log("Navbar current user:", currentUser)
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch("/logout", {
        method: "DELETE",
        credentials: "include",
      });
      if (!response.ok) throw new Error("Failed to log out");
      setCurrentUser(null);
      navigate("/");
    } catch (error) {
      console.error("Logout error:", error);
    }
  };

  const linkStyle = ({ isActive }) => ({
    textDecoration: "none",
    color: isActive ? "white" : "black",
    backgroundColor: isActive ? "black" : "transparent",
    padding: "8px 16px",
    borderRadius: "4px",
    fontWeight: "600", // Adjusted for Inter font
    fontSize: "16px",
    fontFamily: "'Inter', sans-serif",
    transition: "background-color 0.3s, color 0.3s",
  });

  return (
    <AppBar
      position="static"
      color="default"
      sx={{
        boxShadow: "none",
        backgroundColor: "#fff",
        borderBottom: "1px solid #ddd",
        fontFamily: "'Inter', sans-serif",
      }}
    >
      <Toolbar sx={{ justifyContent: "space-between", padding: "0 16px" }}>
        <Typography
          variant="h6"
          sx={{
            fontWeight: "700", // Bold font for the title
            fontFamily: "'Inter', sans-serif",
          }}
        >
          Ira's Quest
        </Typography>
        <Box sx={{ display: "flex", gap: 2 }}>
          {!currentUser ? (
            <>
              <NavLink to="/login" style={linkStyle}>
                Login
              </NavLink>
              <NavLink to="/signup" style={linkStyle}>
                Signup
              </NavLink>
            </>
          ) : (
            <>
              <NavLink to="/" style={linkStyle}>
                Home
              </NavLink>
              <NavLink to="/game" style={linkStyle}>
                Play Ira's Quest
              </NavLink>
              <NavLink to="/posts" style={linkStyle}>
                Chat About The Game
              </NavLink>
              <NavLink to="/leaderboard" style={linkStyle}>
                Leader Board
              </NavLink>
              <Typography
                onClick={handleLogout}
                sx={{
                  cursor: "pointer",
                  padding: "8px 16px",
                  borderRadius: "4px",
                  fontWeight: "600",
                  fontSize: "16px",
                  fontFamily: "'Inter', sans-serif",
                  color: "black",
                  "&:hover": {
                    backgroundColor: "black",
                    color: "white",
                  },
                  transition: "background-color 0.3s, color 0.3s",
                }}
              >
                Logout
              </Typography>
            </>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
