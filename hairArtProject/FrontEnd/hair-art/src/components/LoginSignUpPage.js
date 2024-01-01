import React from 'react';
import { Link } from 'react-router-dom';
import LoginPage from './loginPage';
import SignupPage from './signUp';

const LoginSignupPage = () => {
  return (
    <div>
      <h1>Login</h1>
      <LoginPage />
      <p>
        Don't have an account? <Link to="/signup">Signup here</Link>.
      </p>
      <Link to="/">Back to Home</Link>
    </div>
  );
};

export default LoginSignupPage;


