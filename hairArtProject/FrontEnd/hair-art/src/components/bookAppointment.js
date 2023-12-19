import React, { useState } from 'react';
import './bookAppointment.css';

const BookAppointment = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [service, setService] = useState('');
  const [date, setDate] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', { name, email, service, date });
  };

  return (
    <div className="container">
      <h1 className="heading">Book an Appointment</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
        </label>
        <br />
        <label>
          Email:
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
        </label>
        <br />
        <label>
          Select Service:
          <select value={service} onChange={(e) => setService(e.target.value)} required>
          <option value="">Choose a service</option>
            <option value="Male Section">Line Up Haircut</option>
            <option value="Male Section">Waves + Low Fade</option>
            <option value="Male Section">Twisted Curls With Blow Out Fade</option>
            <option value="Male Section">Frohawk</option>
            <option value="Male Section">Faux Hawk With blonde Sponge Twists</option>
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
        <label>
          Preferred Date:
          <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
        </label>
        <br />
        <button type="submit">Submit</button>
      </form>
    </div>
  );
};

export default BookAppointment;
