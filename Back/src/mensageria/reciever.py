import pika, json
from ..models.enum.type import Type

import logging 
from logging.config import dictConfig
from ..log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

def receiver():
    try:
        logger.info("Serviço de consumo de mensagem!")
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port="5672"))
        channel = connection.channel()

        while True:
            method_frame, header_frame, body = channel.basic_get(queue='post',auto_ack=True)
            if method_frame:
                type: Type = body.decode().type
                body.pop("type", None)
                type(body)
    except Exception as e:
        logger.error(f"Erroao receber mensagem: {str(e)}")