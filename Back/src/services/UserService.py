from src.models.form.UserForm import UserForm
from src.models.view.JWTTokenView import JWTTokenView
from src.models.view.UserView import UserView
from src.repository.UserRepository import create_user, get_user
from src.services.TokenService import token_generator
from src.mensageria.sender import sender_post

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
        return await sender_post(json_form)
    except Exception as e:
        print(e)

async def getUser(user: UserForm):
    try:
        internal_user: UserView = await get_user(user)
        tok = await token_generator(internal_user.name, internal_user.id)
        return JWTTokenView(token=tok, userId=internal_user.id)
    except Exception as e:
        print(e)
        raise Exception("Authentication Failed!")