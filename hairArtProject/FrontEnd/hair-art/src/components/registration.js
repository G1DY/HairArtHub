import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import LoginPage from './loginPage'; 
import SignupPage from './Signup.js'; 

const Registration = () => {
  const [isLoginMode, setIsLoginMode] = useState(true);

  const toggleMode = () => {
    setIsLoginMode((prevMode) => !prevMode);
  };

  const handleLogout = () => {
    // Simple logout logic: just switch to login mode
    setIsLoginMode(true);
    console.log('User logged out');
  };

  return (
    <div>
      <h1>Registration</h1>
      <div>
        <h2>{isLoginMode ? 'Login' : 'Signup'}</h2>
        {isLoginMode ? <LoginPage /> : <SignupPage />}
      </div>
      <p>
        {isLoginMode
          ? "Don't have an account?"
          : 'Already have an account?'}{' '}
        <button onClick={toggleMode}>
          {isLoginMode ? 'Signup here' : 'Login here'}
        </button>
        {isLoginMode && (
          <button onClick={handleLogout} style={{ marginLeft: '10px' }}>
            Logout
          </button>
        )}
      </p>
      <Link to="/">Back to Home</Link>
    </div>
  );
};

export default Registration;

   
