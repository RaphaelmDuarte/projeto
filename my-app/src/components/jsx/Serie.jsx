import '../css/Serie.css'
import React, { useEffect, useState } from "react";
import axios from 'axios';
import * as Constants from './Constants'
import Modal from './Modal';
import AlertModal from './AlertModal';

const Serie = (props) => {
    const protocol = Constants.protocol;
    const host = Constants.host;
    const port = Constants.port;
    const [errorMessage, setErrorMessage] = useState('');

    const Popula = () => {
        let ver = document.getElementById("serieMaster")
        if (ver !== null) {
            return
        }
        let values = sessionStorage.getItem("serieParams")
        let item = JSON.parse(values)
        let div = document.getElementById("headerSerie")
        let header = document.createElement("div")
        header.append(item.name)
        header.setAttribute("id", "serieMaster")
        header.addEventListener("click", function () {
            Seasons(item.id)
        })
        div.appendChild(header)
    }

    const Seasons = (params) => {
        let serieId = params

        axios.get(`${protocol}://${host}:${port}/season/${serieId}`)
            .then(function (response) {
                let seasonDiv = document.getElementById("bodySeasons")
                seasonDiv.innerHTML = ""
                document.getElementById("bodyEpisodes").innerHTML = ""
                if (Object.keys(response.data).length === 0) {
                    let error = document.getElementById("series-error")
                    setErrorMessage("Série não possui temporada!")
                    error.style.display = "block"
                } else {
                    for (let rslt of response.data) {
                        let element = document.createElement("div")
                        element.append(rslt.season)
                        element.setAttribute("id", "seasonDiv")
                        if (rslt.current === true) {
                            element.style.backgroundColor = 'orange';
                        }
                        element.addEventListener("click", function () {
                            episodes(rslt.id)
                        })
                        seasonDiv.appendChild(element)
                    }
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    function episodes(params) {
        let seasonId = params

        axios.get(`${protocol}://${host}:${port}/episodes/${seasonId}`)
            .then(function (response) {
                let episodesDiv = document.getElementById("bodyEpisodes")
                episodesDiv.innerHTML = ""

                if (Object.keys(response.data).length === 0) {
                    let error = document.getElementById("series-error")
                    setErrorMessage("Temporada não possui episódios!")
                    error.style.display = "block"
                } else {
                    for (let rslt of response.data) {
                        let element = document.createElement("div")
                        let item = "Eps: " + rslt.episode + " - " + rslt.name
                        element.append(item)
                        element.setAttribute("id", "episodesDiv")
                        if (rslt.current === true) {
                            element.style.backgroundColor = 'orange';
                        }
                        let form = {
                            id: rslt.id,
                            episode: rslt.episode,
                            name: rslt.name,
                            seasonId: rslt.seasonId,
                            current: rslt.current
                        }
                        element.addEventListener('contextmenu', (event) => {
                            event.preventDefault();
                            form.current = !form.current
                            updateCurrentEpisode(form)
                        })
                        element.addEventListener('dblclick', function (event) {
                            openModal(event, form)
                        })
                        episodesDiv.appendChild(element)
                    }
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    const updateCurrentEpisode = (params) => {
        axios.put(`${protocol}://${host}:${port}/episodes/current`, params)
            .then(function (response) {
                let result = response.data
                if (Object.keys(result).length === 0) {
                    alert("Update error!")
                } else {
                    episodes(result.seasonId)
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    window.onclick = function (event) {
        var modal = document.getElementById("myModal");
        if (event.target === modal) {
            modal.style.display = "none";
        }
    }

    const openModal = (event, params) => {
        let text = document.getElementById("mdNameEp");
        text.value = params.name
        localStorage.setItem("episodeForm", JSON.stringify(params))
        const modal = document.getElementById("myModal");
        modal.style.display = "block";
        const modalContent = document.querySelector(".modal-content");
        const cursorX = event.clientX;
        const cursorY = event.clientY;
        const offSetWidth = modalContent.offsetWidth / 2;
        const offSetHeight = modalContent.offsetHeight / 2;
        const contentPosX = cursorX + offSetWidth;
        const contentPosY = cursorY + offSetHeight;
        modalContent.style.left = contentPosX + "px";
        modalContent.style.top = contentPosY + "px";
    }

    const updateEpisode = (params) => {
        let name = document.getElementById("mdNameEp")

        let object = localStorage.getItem("episodeForm")
        let form = JSON.parse(object)
        if (form.name === name.value) {
            return
        }
        form.name = name.value
        axios.put(`${protocol}://${host}:${port}/episodes/name`, form)
            .then(function (response) {
                let result = response.data
                if (Object.keys(result).length === 0) {
                    alert("Update error!")
                } else {
                    var modal = document.getElementById("myModal");
                    modal.style.display = "none";
                    episodes(result.seasonId)
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }



    useEffect(() => {
        Popula()
    }, []);

    return (
        <div>
            <div className="header">
                <div id="headerSerie"></div>
                <div id="backButton">
                    <button id="back" onClick={e => window.location.href = '/home'}>Voltar</button>
                </div>
            </div>
            <div id="bodySeasons">
            </div>
            <div id="bodyEpisodes">
            </div>
            <Modal function={e => updateEpisode()} />
            <AlertModal name="series-error" titulo="Erro" mensagem={errorMessage} />
        </div>
    )
};

export default Serie;