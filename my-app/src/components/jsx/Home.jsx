import '../css/Home.css'
import React from "react";
import axios from 'axios';
import * as Constants from './Constants'
import AlertModal from './AlertModal';
import { useState } from 'react';

const protocol = Constants.protocol;
const host = Constants.host;
const port = Constants.port;
const Home = (props) => {
    const [alertMensagem, setMensagem] = useState('')

    const series = () => {
        let token = sessionStorage.getItem("token")

        axios.get(`${protocol}://${host}:${port}/series`, {
            headers: {
                'Authorization': `${token}`
            }
        })
            .then(function (response) {
                console.log(response);
                let divSeries = document.getElementById("divSeries")
                divSeries.innerHTML = ""
                if (Object.keys(response.data).length === 0) {
                    var modal = document.getElementById("alerta");
                    setMensagem("Nenhuma série encontrada!")
                    modal.style.display = "block";
                    // alert("No series found!")
                } else {
                    for (let item of response.data) {
                        let divItem = document.createElement("div")
                        let labDiv = item.name
                        divItem.append(labDiv)
                        divSeries.appendChild(divItem)
                        divItem.addEventListener("click", function () {
                            sessionStorage.setItem("serieParams", JSON.stringify(item));
                            window.location.href = '/serie';
                        })
                    }
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }


    const logout = () => {
        sessionStorage.clear()
        window.location.href = "/"
    }



    return (
        <div>
            <div id="button" className="header">
                <div className="selects">
                    <button id="getAllSeries" onClick={e => series()}>Series</button>
                    <button id="registerSeries" onClick={e => window.location.href = "/registerSeries"}>Cadastrar Série</button>
                </div>
                <div className="logout">
                    <button id="logoutRedirect" onClick={e => logout()}>Logout</button>
                </div>
            </div>
            <div id="divSeries" className="divSeries"></div>
            <AlertModal name="alerta" titulo="Erro" mensagem={alertMensagem} />
        </div>
    );
}

export default Home;