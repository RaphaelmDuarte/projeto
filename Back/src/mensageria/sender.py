import pika
import json

import logging 
from logging.config import dictConfig
from ..log_config import log_config

dictConfig(log_config)
logger = logging.getLogger('foo-logger')

async def sender_post(form: json):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', port="5672"))
        channel = connection.channel()
        channel.queue_declare(queue='post')

        channel.basic_publish(exchange='',
                              routing_key='post',
                              body=json.dumps(form))
        connection.close()
        return 'sucess'
    except Exception as e:
        logger.error(f"Erro ao enviar ao rabbit, create_user: {str(e)}")
        return 'failed'