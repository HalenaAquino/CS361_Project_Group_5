                              import { useState } from "react";
                              import { useNavigate } from "react-router-dom";

                              function Login() {
                                const [username, setUsername] = useState("");
                                const [password, setPassword] = useState("");
                                const navigate = useNavigate();

                                const handleLogin = (e) => {
                                  e.preventDefault();

                                  // Dummy login validation
                                  if (username === "admin" && password === "password") {
                                    alert("Login successful!");
                                    navigate("/dashboard"); // Redirect to Dashboard
                                  } else {
                                    alert("Invalid credentials. Try again.");
                                  }
                                };

                                return (
                                  <div className="flex flex-col items-center justify-center h-screen">
                                    <h2 className="text-2xl font-bold mb-4">Login</h2>
                                    <form className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4" onSubmit={handleLogin}>
                                      <div className="mb-4">
                                        <label className="block text-gray-700 text-sm font-bold mb-2">Username</label>
                                        <input
                                          type="text"
                                          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
                                          value={username}
                                          onChange={(e) => setUsername(e.target.value)}
                                          required
                                        />
                                      </div>
                                      <div className="mb-6">
                                        <label className="block text-gray-700 text-sm font-bold mb-2">Password</label>
                                        <input
                                          type="password"
                                          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700"
                                          value={password}
                                          onChange={(e) => setPassword(e.target.value)}
                                          required
                                        />
                                      </div>
                                      <button
                                        type="submit"
                                        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
                                      >
                                        Login
                                      </button>
                                    </form>
                                  </div>
                                );
                              }

                              export default Login;

