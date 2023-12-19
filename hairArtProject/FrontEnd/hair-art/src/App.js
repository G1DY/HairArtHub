import React, { useState, useEffect } from "react";

// import React from 'react';

import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/navbar';
import Home from './components/home';
import Services from './components/services';
import Team from './components/team';
import Gallery from './components/gallery';
import Contact from './components/contact';
import BookAppointment from './components/bookAppointment';

import './App.css';

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
