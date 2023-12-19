import React from 'react';
import './services.css';

const Services = () => {
  return (
    <div className="services-container">
      <h1 className="heading">Our Services & Pricing</h1>

      <div className="section">
        <h2 className="section-heading">MALE SECTION</h2>
        <ul className="list">
          <li>Line Up Haircut: $35</li>
          <li>Waves + Low Fade: $35</li>
          <li>Twisted Curls With Blow Out Fade: $35</li>
          <li>Frohawk: $35</li>
          <li>Faux Hawk With blonde Sponge Twists: $35</li>
          <li>Box Braids With Fade: $35</li>
          <li>The Afro Style: $35</li>
          <li>Shaving: $25</li>
          <li>Hair Dye: $35</li>
          <li>Hair Tinting: $35</li>
          <li>Maintenance: $35</li>
        </ul>
      </div>

      <div className="section">
        <h2 className="section-heading">FEMALE SECTION</h2>
        <ul className="list">
          <li>Goddess Braids: $50</li>
          <li>Knotless Braids: $80</li>
          <li>Box Braids: $80</li>
          <li>Knotless Braids: $80</li>
          <li>Cornrows: $20</li>
          <li>Frontals Installation: $80</li>
          <li>Closure Installation: $80</li>
          <li>Hair Revamping: $80</li>
          <li>Hair Wigging: $80</li>
          <li>Classic Lash Extension: $80</li>
          <li>Hybrid Lash Extension: $80</li>
          <li>Volume Lash Extension: $80</li>
          <li>Mega Volume Lash: $80</li>
          <li>Doll Eye Lash Extension: $80</li>
</ul>
      </div>

      <div className="section">
        <h2 className="section-heading">GENERAL</h2>
        <ul className="list">
          <li>Full body massage: $50</li>
          <li>Full body wax: $80</li>
          <li>Pedicure: $80</li>
          <li>Manicure: $20</li>
          <li>Fixing of Nails: $80</li>
          <li>Facials: $80</li>
          <li>Microblading: $80</li>
          <li>Microshading: $80</li>
          <li>Brow Threading: $80</li>

          </ul>
      </div>
    </div>
  );
};

export default Services;
