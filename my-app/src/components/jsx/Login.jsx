import '../css/Login.css';
import React from 'react';
import axios from 'axios';
import { useState } from 'react';
import * as Constants from './Constants'

const protocol = Constants.protocol;
const host = Constants.host;
const port = Constants.port;

const logar = (email, password) => {
    if (email === '') {
        email = document.getElementById('emailtxt').value
        if (email === '') {
            alert("Email não pode ser vazio");
            return;
        }
    }
    let form = {
        email: email,
        password: password
    }
    axios.post(`${protocol}://${host}:${port}/user/login`, form)
        .then(function (response) {
            let token = response.data.token;
            console.log(response);
            if (response.status === 200) {
                if (token === '') {
                    alert("Authentication failed!");
                }
                sessionStorage.setItem("token", token);
                window.location.href = "/Home";
            }
        })
        .catch(function (error) {
            console.log(error);
        });
}

const Login = (props) => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <div className='lgn-full'>
            <div className="lgn-card">
                <div className='lgn-header'>
                    <h3>Entrar</h3>
                </div>
                <div className="lgn-email">
                    <label>Email</label>
                    <input id='emailtxt' type="text" placeholder='Email' onChange={e => setEmail(e.target.value)} />
                </div>
                <div className="lgn-password">
                    <label>Senha</label>
                    <input id='passwordtxt' type="password" placeholder='Senha' onChange={e => setPassword(e.target.value)} />
                </div>
                <div className="lgn-login">
                    <button id='btn-login' onClick={e => logar(email, password)}>Entrar</button>
                    <a href='/register' className="lgn-register">Registrar</a>
                </div>
            </div>
        </div>
    )
}

export default Login