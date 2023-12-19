import React from 'react';
import './contact.css';

const Contact = () => {
  return (
    <div className="contact-container">
      <h1>Contact Us</h1>
      <p>Have questions or want to schedule an appointment? Reach out to us!</p>
      <address>
        <p>Email: <a href="mailto:info@hairsalon.com">info@hairsalon.com</a></p>
        <p>Phone: (+234) 8152- 3483</p>
        <p>Address: 123 Salon Street, Cityville, Lagos State, Zip</p>
      </address>
    </div>
  );
};

export default Contact;
