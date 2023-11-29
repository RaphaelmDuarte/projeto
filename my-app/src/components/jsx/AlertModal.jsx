import "../css/AlertModal.css"
import React from "react";

const AlertModal = (props) => {
    const modalName = props.name

    const closeModal = () => {
        var modal = document.getElementById(modalName)
        modal.style.display = "none"
    }


    return (
        <div id={modalName} className="alert-modal" style={{ display: "none" }}>
            <div className="alert-modal-content">
                <div className="alert-modal-titulo">
                    <label className="alert-modal-titulo-label">{props.titulo}</label>
                </div>
                <div className="alert-modal-mensagem">
                    <label>{props.mensagem}</label>
                </div>
                <div>
                    <button onClick={e => closeModal()} className="alert-modal-button">Ok</button>
                </div>
            </div>
        </div>
    )
}

export default AlertModal;