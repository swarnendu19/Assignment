import Cookies from "js-cookie";

// Register User
export const RegisterUser = async (email, password, username, setAccountCreated) => {
    try {
        const response = await fetch('http://localhost:8000/api/auth/register', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email, password, username }),  
        });

        const data = await response.json();  
        if (!response.ok) {
            throw new Error(data.detail || "REGISTRATION FAILED");  
        }

        console.log('Registration successful', data);
        setAccountCreated(true);  

    } catch (error) {
        console.error('Error registering user:', error);
    }
};

// Login User
export const LoginUser = async (credentials, setAuth) => {
    try {
        const response = await fetch('http://localhost:8000/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(credentials),
        });

        const data = await response.json();

        if (!response.ok) {
            return console.log(data.detail || "Login failed");  
        }

        console.log('Login successful', data);

        const { access_token } = data;  
        setAuth(true);

        // Store access token and other static values in Cookies
        Cookies.set('access_token', access_token, { expires: 5 });
        Cookies.set("logged_in", true, { expires: 5 });

    } catch (error) {
        console.error('Error logging in:', error);
    }
};
