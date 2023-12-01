from fastapi import HTTPException
from models.form.UserForm import UserForm
from models.view.UserView import UserView
from settings import CONECTION
import bcrypt, json

import logging 
from logging.config import dictConfig
from log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

connect = CONECTION

async def create_user(userForm: UserForm):
    logger.info("Repositório de criação de usuário!")
    query = "INSERT INTO appuser(name, email, password) VALUES('{}', '{}', '{}') RETURNING id;"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(userForm.name, userForm.email.lower(), userForm.password)
        print(sql)
        cur.execute(sql)
        first = cur.fetchone()
        print(userForm)
        use = UserView(id=first[0],
                        name=userForm.name,
                        email=userForm.email)
        conn.commit()
        return use
    except Exception as e:
        logger.error(f"Erro no repositório de criação: {str(e)}")
        raise HTTPException(status_code=409, detail="Email já cadastrado!")

async def get_user(user: UserForm):
    logger.info("Repositório de busca de usuário")
    query = "SELECT * FROM appuser WHERE email = '{}'"
    conn = connect
    cur = conn.cursor()
    try:
        sql = query.format(user.email.lower())
        cur.execute(sql)
        first = cur.fetchone()
        if not bcrypt.checkpw(user.password.encode('utf-8'), first[3].encode('utf-8')):
            logger.error(f"Erro na autenticação!")
            raise Exception("Falha na autenticação!")
        internal_user = UserView(id=first[0],
                                name=first[1],
                                email=user.email)
        return internal_user
    except Exception as e:
        logger.error(f"Erro no repositório de busca: {str(e)}")
        raise HTTPException(status_code=400, detail="Usuário não encontrado!")