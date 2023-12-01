from models.form.UserForm import UserForm
from models.view.JWTTokenView import JWTTokenView
from models.view.UserView import UserView
from repository.UserRepository import get_user
from services.TokenService import token_generator
from mensageria.sender import sender_post
from mensageria.reciever import receiver

import logging, json
from logging.config import dictConfig
from ..log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

async def userCreate(user: UserForm):
    try:
        logger.info("Serviço de criação de Usuário!")
        form = json.dumps(user.__dict__, indent=2)
        json_form = json.loads(form)
        json_form["type"] = "create_user"
        await sender_post(json_form)
        await receiver()
        return 'Success'
    except Exception as e:
        print(e)

async def getUser(user: UserForm):
    try:
        logger.info("Serviço de autenticação de usuário!")
        internal_user: UserView = await get_user(user)
        tok = await token_generator(internal_user.name, internal_user.id)
        return JWTTokenView(token=tok, userId=internal_user.id)
    except Exception as e:
        logger.error(f"Erro no serviço de autenticação: {str(e)}")
        raise Exception("Falha na autenticação!")