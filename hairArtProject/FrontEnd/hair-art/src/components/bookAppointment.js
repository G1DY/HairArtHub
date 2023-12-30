import axios from "axios";
import React, { useState } from "react";
import "./bookAppointment.css";

const BookAppointment = () => {
  // const [name, setName] = useState("");
  // const [email, setEmail] = useState("");
  const [service, setService] = useState("");
  const [errorMessage, setErrorMessage] = useState("");
  const [successMessage, setSuccessMessage] = useState("");
  const [selected_time, setDateTime] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Make a POST request to backend endpoint
      const response = await axios.post(
        "http://127.0.0.1:5000/create_bookings",
        {
          service,
          selected_time,
        }
      );

      // If successful, update success message
      setSuccessMessage(response.data.message);
      setErrorMessage(""); // Clear any previous error message
    } catch (error) {
      // If there's an error, update error message
      setErrorMessage(error.response.data.error);
      setSuccessMessage(""); // Clear any previous success message
    }
    console.log("Form submitted:", { service, selected_time });
  };

  return (
    <div className="container">
      <h1 className="heading">Book an Appointment</h1>
      {errorMessage && <p style={{ color: "red" }}>{errorMessage}</p>}
      {successMessage && <p style={{ color: "green" }}>{successMessage}</p>}
      <form onSubmit={handleSubmit}>
        <label>
          Select Service:
          <select
            value={service}
            onChange={(e) => setService(e.target.value)}
            required
          >
            <option value="">Choose a service</option>
            <option value="Male Section">Line Up Haircut</option>
            <option value="Male Section">Waves + Low Fade</option>
            <option value="Male Section">
              Twisted Curls With Blow Out Fade
            </option>
            <option value="Male Section">Frohawk</option>
            <option value="Male Section">
              Faux Hawk With blonde Sponge Twists
            </option>
            <option value="Male Section">Box Braids With Fade</option>
            <option value="Male Section">Shaving</option>
            <option value="Male Section">Hair Dye</option>
            <option value="Male Section">Hair Tinting</option>
            <option value="Male Section">Dread</option>
            <option value=">Male Section">Hair Locking</option>
            <option value="Male Section">Maintenance</option>
            <option value="Female section">Goddess Braids</option>
            <option value="Female section">Knotless Braids</option>
            <option value="Female section">Box Braids</option>
            <option value="Female section">Cornrows</option>
            <option value="Female section">Frontals Installation</option>
            <option value="Female section">Closure Installation</option>
            <option value="Female section">Hair Revamping</option>
            <option value="Female section">Hair Wigging</option>
            <option value="Female section">Hair Customization</option>
            <option value="Female section">Classic Lash Extension</option>
            <option value="Female section">Hybrid Lash Extension:</option>
            <option value="Female section">Volume Lash Extension</option>
            <option value="Female section">Mega Volume Lash</option>
            <option value="Female section">Doll Eye Lash Extension</option>
            <option value="General">Full body massage</option>
            <option value="General">Full body wax</option>
            <option value="General">Pedicure</option>
            <option value="General">Manicure</option>
            <option value="General">Fixing of Nails</option>
            <option value="General">Microbolading</option>
            <option value="General">Microshading</option>
            <option value="General">Brow Threading</option>
          </select>
        </label>
        <br />
        <label htmlFor="preferredDateTime">Preferred Date and Time:</label>
        <input
          type="datetime-local"
          id="preferredDateTime"
          value={selected_time}
          onChange={(e) => setDateTime(e.target.value)}
          required
        />
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default BookAppointment;
