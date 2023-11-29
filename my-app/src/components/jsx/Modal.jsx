import React from "react";

const Modal = (props) => {
    return (
        <div id="myModal" className="modal" style={{ display: "none" }}>
            <div className="modal-content">
                <div className="modal-episode-edit">
                    <label>Nome do Episódio</label>
                    <input id="mdNameEp" type="text" autoComplete="off" />
                    <div className="alterButton">
                        <button className="mdButton" onClick={props.function}>Alterar</button>
                    </div>
                </div>
            </div>
        </div>
    )
}

export default Modal;