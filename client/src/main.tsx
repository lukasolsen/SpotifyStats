import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.tsx";
import "./index.css";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import Layout from "./layout/index.tsx";
import Register from "./pages/Register.tsx";
import Login from "./pages/Login.tsx";
import { verifyToken } from "./service/api.service.ts";

// check if they are logged in
const getData = () => {
  const token = localStorage.getItem("token");

  if (token) {
    return verifyToken(token);
  }
};

const hasAccount = getData();

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <BrowserRouter>
      <Routes>
        <Route element={<Layout hasAccount={hasAccount} />}>
          <Route path="/" element={<App />} />
          <Route path="/register" element={<Register />} />
          <Route path="/login" element={<Login />} />
        </Route>
      </Routes>
    </BrowserRouter>
  </React.StrictMode>
);
