import React from "react";
import App from "./components/App";
import "./index.css";
import { createRoot } from "react-dom/client";
import { UserProvider } from "./components/UserContext";

const container = document.getElementById("root");
const root = createRoot(container);
root.render(
<UserProvider>
    <App />
</UserProvider>,
);
