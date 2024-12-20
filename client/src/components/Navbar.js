import React from "react";
import { AppBar, Toolbar, Typography, Box } from "@mui/material";
import { NavLink, useNavigate } from "react-router-dom";
import toast, { Toaster } from "react-hot-toast"

const Navbar = ({ currentUser, setCurrentUser }) => {
  const navigate = useNavigate();

  const handleLogout = async () => {
    try {
      const response = await fetch("/logout", {
        method: "DELETE",
        credentials: "include",
      });
      if (!response.ok) throw new Error("Failed to log out");
      setCurrentUser(null);
      toast.success("Successfully logged out!");
    } catch (error) {
      console.error("Logout error:", error);
      toast.error("Failed to log out.");
    }
  };

  const navItemsLoggedOut = [
    { title: "Home", path: "/" },
    { title: "Login", path: "/login" },
    { title: "Signup", path: "/signup" },
  ];

  const navItemsLoggedIn = [
    { title: "Home", path: "/" },
    { title: "Play Ira's Quest", path: "/game" },
    { title: "Chat About The Game", path: "/posts" },
    { title: "Leader Board", path: "/leaderboard" },
  ];

  return (
    <AppBar position="static" color="default" sx={{ boxShadow: "none" }}>
      <Toolbar>
        <Box
          sx={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            gap: 4,
            py: 2,
            borderBottom: "1px solid #ddd",
            backgroundColor: "#fff",
            width: "100%",
            position: "fixed",
            top: 0,
            zIndex: 1000,
          }}
        >
          {!currentUser &&
            navItemsLoggedOut.map((item) => (
              <NavLink
                key={item.title}
                to={item.path}
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "white" : "black",
                  backgroundColor: isActive ? "black" : "transparent",
                  padding: "8px 16px",
                  borderRadius: "4px",
                  fontWeight: isActive ? "bold" : "normal",
                })}
              >
                <Typography variant="button">{item.title}</Typography>
              </NavLink>
            ))}

          {currentUser &&
            navItemsLoggedIn.map((item) => (
              <NavLink
                key={item.title}
                to={item.path}
                style={({ isActive }) => ({
                  textDecoration: "none",
                  color: isActive ? "white" : "black",
                  backgroundColor: isActive ? "black" : "transparent",
                  padding: "8px 16px",
                  borderRadius: "4px",
                  fontWeight: isActive ? "bold" : "normal",
                })}
              >
                <Typography variant="button">{item.title}</Typography>
              </NavLink>
            ))}

          {currentUser && (
            <Typography
              variant="button"
              onClick={async () => {
                await handleLogout();
                navigate("/");
              }}
              sx={{
                textDecoration: "none",
                color: "black",
                padding: "8px 16px",
                borderRadius: "4px",
                fontWeight: "bold",
                cursor: "pointer",
                "&:hover": {
                  backgroundColor: "black",
                  color: "white",
                },
              }}
            >
              Log Out
            </Typography>
          )}
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
