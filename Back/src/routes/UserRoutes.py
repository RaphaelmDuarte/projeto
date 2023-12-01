from fastapi import APIRouter, Response, status
from models.form.UserForm import UserForm
from services.UserService import userCreate, getUser
import bcrypt

import logging 
from logging.config import dictConfig
from log_config import log_config

user = APIRouter(
    prefix='/user',
    tags=['user']
)

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

@user.post('/', status_code=201)
async def create(user: UserForm, response: Response):
    try:
        logger.info("Requisição de criação de usuário!")        
        salt = bcrypt.gensalt(rounds=12)
        cryptpassword = bcrypt.hashpw(user.password.encode('utf-8'), salt)
        internal_user = UserForm(name=user.name,
                                email=user.email,
                                password=cryptpassword)
        return await userCreate(internal_user)
    except Exception as e:
        logger.error(f"Não foi possível criar o usuário: {str(e)}")
        response.status_code = status.HTTP_400_BAD_REQUEST

@user.post('/login', status_code=200)
async def authenticate(user: UserForm, response: Response):
    try:
        logger.info("Authenticação de usuário!")
        return await getUser(user)
    except Exception as e:
        logger.error(f"Não foi possível autenticar: {str(e)}")
        response.status_code = status.HTTP_401_UNAUTHORIZED