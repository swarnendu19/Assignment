/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useContext, useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import { FaLock } from "react-icons/fa";
import { MdEmail } from "react-icons/md";
import AuthContext from "../../context/AuthContext";
import { RegisterUser } from "../../services/auth/authService";

const Register = () => {
    const [username, setUsername] = useState(''); 
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const navigate = useNavigate();

    const { setAccountCreated, accountCreated } = useContext(AuthContext);

    const handleRegistration = async (event) => {
        event.preventDefault();
        try {
            // Validate that passwords match
            if (password !== confirmPassword) {
                throw new Error('Passwords do not match, Please try again');
            }
            
            // Call the register service, passing username
            await RegisterUser(username, email, password, setAccountCreated);

        } catch (error) {
            console.error("Registration error:", error.message);
            alert(error.message);
        }
    };

    // Redirect to login page after successful registration
    useEffect(() => {
        if (accountCreated) {
            navigate("/login"); // Redirect to login when accountCreated is true
        }
    }, [accountCreated, navigate]);

    return (
        <div className="wrapper">
            <form onSubmit={handleRegistration}>
                <h1>Register</h1>
                
                {/* Username Input */}
                <div className="input-box">
                    <input 
                        type="text" 
                        placeholder="Username" 
                        value={username} 
                        onChange={(e) => setUsername(e.target.value)} 
                        required 
                    />
                </div>

                {/* Email Input */}
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

                {/* Password Input */}
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

                {/* Confirm Password Input */}
                <div className="input-box">
                    <input 
                        type="password" 
                        placeholder="Confirm Password" 
                        value={confirmPassword} 
                        onChange={(e) => setConfirmPassword(e.target.value)} 
                        required 
                    />
                    <FaLock className="icon" />
                </div>

                <div className="remember-forgot">
                    <label><input type="checkbox" />Remember me</label>
                    <a href="#">Forgot password?</a>
                </div>

                <button type="submit">Register</button>

                <div className="register-link">
                    <p>Already have an account? <a href="#" onClick={() => navigate("/login")}>Login</a></p>
                </div>
            </form>
        </div>
    );
};

export default Register;
