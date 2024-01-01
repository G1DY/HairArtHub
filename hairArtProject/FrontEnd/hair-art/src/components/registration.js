import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import LoginPage from './loginPage';
import SignupPage from './Signup.js';
import './Registration.css'; 


const Registration = () => {
  const [isLoginMode, setIsLoginMode] = useState(true);

  const toggleMode = () => {
    setIsLoginMode((prevMode) => !prevMode);
  };

  const handleLogout = () => {
    setIsLoginMode(true);
    console.log('User logged out');
  };

  return (
    <div className="container">
      <div className="formContainer">
        <h2 className="formTitle">{isLoginMode ? 'Login' : 'Signup'}</h2>
        {isLoginMode ? <LoginPage /> : <SignupPage />}
      </div>
      <p className="message">
        {isLoginMode
          ? "Don't have an account?"
          : 'Already have an account?'}{' '}
        <button onClick={toggleMode} className="toggleButton">
          {isLoginMode ? 'Signup here' : 'Login here'}
        </button>
        {isLoginMode && (
          <button onClick={handleLogout} className="logoutButton">
            Logout
          </button>
        )}
      </p>
      <Link to="/" className="link">Back to Home</Link>
    </div>
  );
};

export default Registration;
