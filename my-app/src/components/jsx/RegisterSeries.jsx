import '../css/RegisterSeries.css'
import React, { useState } from "react";
import axios from 'axios';
import * as Constants from './Constants'
import AlertModal from './AlertModal';

const RegSeries = (props) => {
    const protocol = Constants.protocol;
    const host = Constants.host;
    const port = Constants.port;
    const [temporadas, setTemporadas] = useState('');
    const [errorMessage, setErrorMessage] = useState('');

    const RegisterSeries = () => {
        let token = sessionStorage.getItem("token")

        let seasonName = document.getElementById("hdinRegName")
        if (seasonName.value === '') {
            let error = document.getElementById("registro-erro")
            setErrorMessage("Nome da série não pode ser vazia.")
            error.style.display = "block"
            return null
        }
        let temporadas = document.getElementsByClassName("temporadas")
        let seasons = []
        if (temporadas.length === 0) {
            let error = document.getElementById("registro-erro")
            setErrorMessage('Nenhuma temporada na série.')
            error.style.display = "block"
            return null
        }
        for (let i = 0; i < temporadas.length; i++) {
            let ssForm = {
                season: parseInt(temporadas[i].firstChild.textContent),
                episodes: temporadas[i].lastChild.value
            }
            if (ssForm.episodes === '') {
                let error = document.getElementById("registro-erro")
                setErrorMessage(`A temporada ${ssForm.season} não contém episódios.`)
                error.style.display = "block"
                return null
            }
            seasons.push(ssForm)
        }

        let form = {
            name: seasonName.value,
            seasons: seasons
        }

        axios.post(`${protocol}://${host}:${port}/series`, form, {
            headers: {
                'Authorization': `${token}`
            }
        })
            .then(function (response) {
                console.log(response);
                if (response.status === 200) {
                    var modal = document.getElementById("registro-sucesso")
                    modal.style.display = "block"
                    setTemporadas(0)
                }
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    const renderTemporadas = () => {
        const count = parseInt(temporadas, 10);
        if (isNaN(count)) {
            return null;
        }

        return Array.from({ length: count }, (_, index) => (
            <div className='temporadas'>
                <div className='episodio-label' key={index}>{index + 1}</div>
                <input className='episodio-input' type="number" />
            </div>
        ));
    };


    return (
        <div>
            <div className="headerRegSeries">
                <div className="inRegSeries">
                    <label id="hdlbRegSeries">Série</label>
                    <input type="text" id="hdinRegName" autoComplete="off" placeholder="Nome" required="" />
                </div>
                <div className="final">
                    <button id="fnbtReturn" onClick={e => window.location.href = "/home"}>Voltar</button>
                </div>
            </div>
            <div className="bodyRegSeries">
                <label id="bdlbRegSeries">Temporadas</label>
                <input type='number' autoComplete='off' placeholder='Nº' onChange={e => setTemporadas(e.target.value)}></input>
                <div className='register-series-temporadas'>
                    {renderTemporadas()}
                </div>
                <div className="addNewLine">
                    <button id="registerSeries" onClick={e => RegisterSeries()}>Cadastrar</button>
                </div>
            </div>
            <AlertModal name="registro-sucesso" titulo="Sucesso" mensagem="Série cadastrada com sucesso." />
            <AlertModal name="registro-erro" titulo="Erro" mensagem={errorMessage} />
        </div>
    )
};

export default RegSeries;