import React from 'react';
import { Link } from 'react-router-dom';
import './navbar.css';
import logo2 from '../images/logo2.jpg';


const Navbar = () => {
  return (
    <nav>
      <div className="logo">
        <Link to="/">
        <img src={logo2} alt="Logo" className="logo" />
      </Link>
      </div>
      <div className="nav-links">
        <Link to="/">Home</Link>
        <Link to="/services">Services & Pricing</Link>
        <Link to="/team">Meet the Team</Link>
        <Link to="/gallery">Gallery</Link>
        <Link to="/contact">Contact Us</Link>
        <Link to="/bookAppointment">Book an Appointment</Link>
        <Link to="/registration">Registration</Link>
      </div>
    </nav>
  );
};

export default Navbar;
