import pika, json
from repository.UserRepository import create_user
from models.form.UserForm import UserForm

import logging 
from logging.config import dictConfig
from log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

async def receiver():
    try:
        logger.info("Serviço de consumo de mensagem!")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq-service', port=5672))
        channel = connection.channel()

        while True:
            method_frame, header_frame, body = channel.basic_get(queue='post',auto_ack=True)
            if method_frame:
                logger.info("Mensagem recebida, decodificando!")
                json_string = body.decode()
                json_form = json.loads(json_string)
                type = json_form.get('type')
                json_form.pop('type', None)
                if type == "create_user":
                    logger.info("Criação de Usuário!")
                    await create_user(UserForm(**json_form))
                    return 'Sucess'
                

    except Exception as e:
        logger.error(f"Erro ao receber mensagem: {str(e)}")
        return 'Failed'