import React, { useEffect, useState } from 'react';
import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider, Navigate } from 'react-router-dom';
import Login from './components/loginUser/loginUser';
import Dashboard from './components/dashboard/dashboard';
import AuthContext from './context/AuthContext';
import Cookies from 'js-cookie';
import Root from './components/Root';
import Register from './components/registerUser/registerUser';

const App = () => {
  const [auth, setAuth] = useState(false);
  const [accountCreated, setAccountCreated] = useState(false);

  const readCookie = () => {
    const user = Cookies.get("token");
    if (user) {
      setAuth(true);
    }
  };

  useEffect(() => {
    readCookie();
  }, []);

  // Routes setup using createBrowserRouter
  const router = createBrowserRouter(
    createRoutesFromElements(
      <>
        {/* Redirect to Dashboard if authenticated */}
        <Route path='/' element={auth ? <Navigate to="/dashboard" /> : <Navigate to="/login" />} />

        {/* Login Route */}
        <Route path='/login' element={<Login />} />

        {/* Register Route */}
        <Route path='/register' element={<Register />} />

        {/* Dashboard Route - only accessible if authenticated */}
        <Route
          path='/dashboard'
          element={auth ? <Dashboard /> : <Navigate to="/login" />}
        >
          <Route path='welcome' element={<div>Welcome user</div>} />
        </Route>
      </>
    )
  );

  return (
    <AuthContext.Provider value={{ auth, setAuth, setAccountCreated, accountCreated }}>
      <RouterProvider router={router} />
    </AuthContext.Provider>
  );
};

export default App;
