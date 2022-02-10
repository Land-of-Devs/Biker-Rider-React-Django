import React, { useState } from "react";
import { useNavigate } from "react-router-dom"
import useAuth from '/src/hooks/useAuth'
import { useEffect } from "react";

const LoginForm = ({ close, onLogin }) => {
  const [dni, setDni] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate()
  const { isLoginLoading, hasLoginError, login, isLogged } = useAuth()

  useEffect(() => {
    if (isLogged) {
      navigate('/')
      onLogin && onLogin()
    }
  }, [isLogged, navigate, onLogin])

  const handleSubmit = (e) => {
    e.preventDefault();
    login({ dni, password }).then(() => close())
  };

  return (
    <>
      {isLoginLoading && <strong>Checking credentials...</strong>}
      {!isLoginLoading &&
        <form className='form' onSubmit={handleSubmit}>
          <label>
            DNI
            <input
              placeholder="username"
              onChange={(e) => setDni(e.target.value)}
              value={dni}
            />
          </label>

          <label>
            Password
            <input
              type="password"
              placeholder="password"
              onChange={(e) => setPassword(e.target.value)}
              value={password}
            />
          </label>

          <button className='btn'>Login</button>
        </form>
      }
      {
        hasLoginError && <strong>Credentials are invalid</strong>
      }
    </>
  );
}

export default LoginForm;