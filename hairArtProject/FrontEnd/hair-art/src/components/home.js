import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../components/home.css";
import LoginPage from "./loginPage";
import SignupPage from "./signUp";

const Home = () => {
  const [showLogin, setShowLogin] = useState(false);
  const [showSignup, setShowSignup] = useState(false);

  const handleLoginClick = () => {
    setShowLogin(true);
  };

  const handleSignupClick = () => {
    setShowSignup(true);
  };

  return (
    <div className="home-container">
      <div className="home-background"></div>
      <div className="home-content">
        <h1>Welcome to Our Hair Salon</h1>
        <p>Experience the best in hair care and styling at our salon.</p>
        <p>Book an appointment with our talented team today!</p>

        {!showLogin ? (
          <button className="login-button" onClick={handleLoginClick}>
            Login
          </button>
        ) : (
          <LoginPage />
        )}

        {!showSignup ? (
          <button className="signup-button" onClick={handleSignupClick}>
            Sign Up
          </button>
        ) : (
          <SignupPage />
        )}

        <p>
          Don't have an account?{" "}
          <Link to="http://localhost:3000/signup">Sign up</Link>
        </p>
      </div>
    </div>
  );
};

export default Home;
