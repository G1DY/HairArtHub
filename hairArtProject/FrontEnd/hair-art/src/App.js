// import React, { useState, useEffect } from "react";
import React from "react";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import BookAppointment from "./components/bookAppointment";
import Contact from "./components/contact";
import Gallery from "./components/gallery";
import Home from "./components/home";
import Navbar from "./components/navbar";
import Services from "./components/services";
import Team from "./components/team";

import "./App.css";

const App = () => {
  return (
    <Router>
      <div>
        <Navbar />
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/services" element={<Services />} />
          <Route path="/team" element={<Team />} />
          <Route path="/gallery" element={<Gallery />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/bookAppointment" element={<BookAppointment />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
