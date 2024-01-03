import axios from "axios";
import React, { useState } from "react";

const SignupPage = () => {
  const [email, setEmail] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [_password, setConfirmPassword] = useState("");
  const [errorMessage, setErrorMessage] = useState(""); // Added state for error message
  const [successMessage, setSuccessMessage] = useState(""); // Added state for success message

  const handleSignup = async (e) => {
    e.preventDefault();

    try {
      // Make a POST request to backend endpoint
      const response = await axios.post("http://127.0.0.1:5000/sign_up", {
        email,
        username,
        password,
        _password,
      });

      // If successful, update success message
      setSuccessMessage(response.data.message);
      setErrorMessage(""); // Clear any previous error message
    } catch (error) {
      // If there's an error, update error message
      setErrorMessage(error.response.data.error);
      setSuccessMessage(""); // Clear any previous success message
    }
  };

  return (
    <div>
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}
      <form onSubmit={handleSignup}>
        <label>
          Email:
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Username:
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Password:
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <label>
          Confirm Password:
          <input
            type="password"
            value={_password}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
        </label>
        <br />
        <button type="submit">Sign Up</button>
      </form>
    </div>
  );
};

export default SignupPage;
