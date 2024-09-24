import React, { useContext, useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaLock } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
import './loginUser.css';
import AuthContext from "../../context/AuthContext";
import { LoginUser } from "../../services/auth/authService";

const Login = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [errorMessage, setErrorMessage] = useState('');
    const navigate = useNavigate();
    const { setAuth } = useContext(AuthContext);

    const handleLogin = async (e) => {
        e.preventDefault();

        const userData = { email, password };

        try {
             const loginSuccess = await LoginUser(userData, setAuth);

            if (loginSuccess) {
                 navigate("/dashboard");
            } else {
                throw new Error("Login failed. Please check your credentials.");
            }
        } catch (error) {
            setErrorMessage(error.message || 'An error occurred during sign-in');
        }
    };

    return (
        <div className="wrapper">
            <form onSubmit={handleLogin}>
                <h1>Login</h1>
                
                 {errorMessage && <div className="error-message">{errorMessage}</div>}
                
                <div className="input-box">
                    <input 
                        type="email" 
                        placeholder="Email" 
                        value={email} 
                        onChange={(e) => setEmail(e.target.value)} 
                        required 
                    />
                    <MdEmail className="icon" />
                </div>

                <div className="input-box">
                    <input 
                        type="password" 
                        placeholder="Password" 
                        value={password} 
                        onChange={(e) => setPassword(e.target.value)} 
                        required 
                    />
                    <FaLock className="icon" />
                </div>

                <div className="remember-forgot">
                    <label><input type="checkbox" />Remember me</label>
                    <a href="#">Forgot password?</a>
                </div>

                <button type="submit">Login</button>

                <div className="register-link">
                    <p>Don't have an account? <a href="#" onClick={() => navigate("/register")}>Register</a></p>
                </div>
            </form>
        </div>
    );
};

export default Login;
