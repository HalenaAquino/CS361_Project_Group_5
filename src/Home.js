import React from 'react';
import './Home.css';
import './Styles.css';
import { useNavigate } from 'react-router-dom';

function Home() {
    const navigate = useNavigate(); // Hook for navigation

  // Inline styles for the violet theme
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    color: 'black',
    fontFamily: 'Arial, sans-serif',
  };

  const headingStyle = {
    fontSize: '3rem',
    marginBottom: '20px',
    color: 'violet',
  };

  const paragraphStyle = {
    fontSize: '1.2rem',
    marginBottom: '30px',
  };

  const buttonStyle = {
    padding: '10px 20px',
    fontSize: '1rem',
    backgroundColor: 'violet',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    transition: 'background-color 0.3s',
  };

  const buttonHoverStyle = {
    backgroundColor: 'darkviolet',
  };

  return (
    <div style={containerStyle}>
      <h1 style={headingStyle}>Welcome to ShopSmart Solutions</h1>
      <p style={paragraphStyle}>Use the Login credentials to see the DashBoard.</p>
      {/* Button with hover effect using inline style */}
      <button
        style={buttonStyle}
        onMouseOver={(e) => (e.target.style.backgroundColor = buttonHoverStyle.backgroundColor)}
        onMouseOut={(e) => (e.target.style.backgroundColor = buttonStyle.backgroundColor)}
        onClick={() => navigate('/dashboard')}
      >
        Go to Dashboard
      </button>
    </div>
  );
}

export default Home;
