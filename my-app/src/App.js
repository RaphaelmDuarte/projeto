import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Home from "./components/jsx/Home";
import Login from "./components/jsx/Login";
import Register from "./components/jsx/Register";
import RegSeries from "./components/jsx/RegisterSeries";
import Serie from "./components/jsx/Serie";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/home" element={<Home />} />
        <Route path="/register" element={<Register />} />
        <Route path="/registerSeries" element={<RegSeries />} />
        <Route path="/serie" element={<Serie />} />
      </Routes>
    </Router>
  )
}

export default App;
