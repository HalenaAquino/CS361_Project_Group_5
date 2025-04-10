import { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Login.css';
import './Styles.css';

function Login() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    if (username === "admin" && password === "ad123") {
      alert("Login successful!");
      navigate("/dashboard");
    } else {
      setError("Invalid credentials. Try again.");
    }
  };

  return (
    <div className="login-container">
      {/* Top Section - Login Title */}
      <h2 className="login-title">Login</h2>

      {/* Middle Section - Login Form */}
      <div className="login-box">
        <form onSubmit={handleLogin}>
          <div className="input-container">
            <label>Username</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
              placeholder="Enter your username"
            />
          </div>

          <div className="input-container">
            <label>Password</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
              placeholder="Enter your password"
            />
          </div>

          {error && <div className="error-message">{error}</div>}

          <button type="submit">Login</button>
        </form>
      </div>

      {/* Bottom Section - Customer Support */}
      <div className="support-text">
        Need help? <a href="#" className="support-link">Contact Support</a>
      </div>
    </div>
  );
}

export default Login;

