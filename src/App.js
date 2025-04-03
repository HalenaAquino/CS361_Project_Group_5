                    import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
                    import Dashboard from "./Dashboard";
                    import Login from "./Login";
                    import Home from "./Home";

                    function App() {
                      return (
                        <div>
                          <nav>
                            <ul>
                              <li><Link to="/">Home</Link></li>
                              <li><Link to="/dashboard">Dashboard</Link></li>
                              <li><Link to="/Login">Login</Link></li>
                              <li><Link to="/About">About</Link></li>
                            </ul>
                          </nav>
                          <Routes>
                            <Route path="/" element={<Home />} />
                            <Route path="/login" element={<Login />} />
                            <Route path="/dashboard" element={<Dashboard />} />
                            <Route path="/about" element={<About />} />
                          </Routes>
                         </div>
                      );
                    }

                    export default App;

