import '../css/Register.css'
import React from "react";
import axios from 'axios'
import { useState } from 'react';
import * as Constants from './Constants'

const protocol = Constants.protocol;
const host = Constants.host;
const port = Constants.port;

const registrar = (nome, email, password) => {
    let form = {
        name: nome,
        email: email,
        password: password
    }
    axios.post(`${protocol}://${host}:${port}/user`, form)
        .then(function (response) {
            console.log(response);
            if (response.status === 201) {
                alert("User registered successfully!")
                window.location.href="/"
            }
        })
        .catch(function (error) {
            if (error.response.status === 409) {
                alert("Email already registered!")
            } else {
                console.log(error);
            }
        });
}

const Register = (props) => {
    const [nome, setNome] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    return (
        <div className='rgs-full'>
            <div className="rgs-card">
                <div className='rgs-header'>
                    <h3>Registrar</h3>
                </div>
                <div className="rgs-nome">
                    <label>Nome</label>
                    <input type="text" placeholder='Nome' onChange={e => setNome(e.target.value)} />
                </div>
                <div className="rgs-email">
                    <label>Email</label>
                    <input type="text" placeholder='Email' onChange={e => setEmail(e.target.value)} />
                </div>
                <div className="rgs-password">
                    <label>Senha</label>
                    <input type="password" placeholder='Senha' onChange={e => setPassword(e.target.value)} />
                </div>
                <div className="rgs-registrar">
                    <button id='btn-registro' onClick={e => registrar(nome, email, password)}>Registrar</button>
                    <a href='/' className="rgs-login">Entrar</a>
                </div>
            </div>
        </div>
    )
};

export default Register;