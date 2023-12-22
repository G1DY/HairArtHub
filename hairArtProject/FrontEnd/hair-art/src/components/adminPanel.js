import axios from "axios";
import React, { useEffect, useState } from "react";

const AdminPanel = () => {
  // State for storing services data
  const [services, setServices] = useState([]);

  // useEffect to fetch data when the component mounts
  useEffect(() => {
    const fetchServices = async () => {
      try {
        const response = await axios.get(
          "http://http://127.0.0.1:5000/admin/services"
        );
        setServices(response.data);
      } catch (error) {
        console.error("Error fetching services:", error);
      }
    };

    fetchServices();
  }, []);

  // Function to create a new service
  const createService = async (newService) => {
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/admin/services",
        newService
      );
      console.log("Service created:", response.data);

      // Update the state to include the new service
      setServices((prevServices) => [...prevServices, response.data]);
    } catch (error) {
      console.error("Error creating service:", error);
    }
  };

  return (
    <div>
      <h1>Services</h1>
      {/* Render services list */}
      <ul>
        {services.map((service) => (
          <li key={service.id}>{service.service_name}</li>
        ))}
      </ul>

      {/* Example: Create a new service */}
      <button onClick={() => createService({ service_name: "New Service" })}>
        Create New Service
      </button>
    </div>
  );
};

export default AdminPanel;
