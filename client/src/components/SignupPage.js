import React, { useContext } from "react";
import { useNavigate } from "react-router-dom";
import { Box, Typography, TextField, Button, Alert } from "@mui/material";
import { Formik, Form, Field, ErrorMessage } from "formik";
import * as Yup from "yup";
import castleImage from "../assets/pictures/Splash.png";
import { UserContext } from "./UserContext";



const SignUpPage = () => {
  const { setCurrentUser } = useContext(UserContext);
  const nav = useNavigate();

  // Validation schema using Yup
  const validationSchema = Yup.object({
    email: Yup.string()
      .email("Invalid email format")
      .required("Email is required"),
    username: Yup.string()
      .min(3, "Username must be at least 2 characters")
      .required("Username is required"),
    password: Yup.string()
      .min(6, "Password must be at least 6 characters")
      .required("Password is required"),
  });

  // Formik initial values
  const initialValues = {
    email: "",
    username: "",
    password: "",
  };


const handleSubmit = async (values, { setSubmitting, setFieldError, setStatus }) => {
  setStatus(null); // Clear previous status messages
  try {
    const response = await fetch("/signup", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(values),
    });

    const data = await response.json();
    if (!response.ok) throw new Error(data.error || "Failed to sign up");

    // Update the currentUser in the context
    setCurrentUser(data);

    setStatus({ success: "Account created successfully!" });

    // Navigate to the posts page immediately after updating the user context
    nav("/posts");
  } catch (err) {
    setFieldError("general", err.message); // Set general error
  } finally {
    setSubmitting(false);
  }
};

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
              width: "500px",
              height: "500px",
              objectFit: "cover",
            }}
          />
        </Box>

        <Box
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

          <Formik
            initialValues={initialValues}
            validationSchema={validationSchema}
            onSubmit={handleSubmit}
          >
            {({ isSubmitting, status, errors }) => (
              <Form>
                {errors.general && (
                  <Alert severity="error" sx={{ mb: 2 }}>
                    {errors.general}
                  </Alert>
                )}
                {status?.success && (
                  <Alert severity="success" sx={{ mb: 2 }}>
                    {status.success}
                  </Alert>
                )}

                <Field
                  as={TextField}
                  name="email"
                  label="Enter your e-mail"
                  type="email"
                  variant="outlined"
                  size="small"
                  fullWidth
                  error={!!errors.email}
                  helperText={<ErrorMessage name="email" />}
                />

                <Field
                  as={TextField}
                  name="username"
                  label="Enter a username"
                  variant="outlined"
                  size="small"
                  fullWidth
                  error={!!errors.username}
                  helperText={<ErrorMessage name="username" />}
                />

                <Field
                  as={TextField}
                  name="password"
                  label="Choose a password"
                  type="password"
                  variant="outlined"
                  size="small"
                  fullWidth
                  error={!!errors.password}
                  helperText={<ErrorMessage name="password" />}
                />

                <Button
                  type="submit"
                  variant="contained"
                  color="primary"
                  disabled={isSubmitting}
                  sx={{
                    mt: 2,
                    borderRadius: "8px",
                    fontWeight: "bold",
                  }}
                >
                  {isSubmitting ? "Signing Up..." : "Sign Up"}
                </Button>
              </Form>
            )}
          </Formik>

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
  );
};

export default SignUpPage;
