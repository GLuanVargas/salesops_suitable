import requests
import logging
from random import randint
import time

logger = logging.getLogger(__name__)

class Message:

    def __init__(self):
        logger.info('Objeto message instanciado')

    def send_msg(self, phone, msg):
        url = 'https://www.waboxapp.com/api/send/chat'
        token = 'e0701f135b971ae33650947a64af59465c29e0cc04ea9'
        origin = '555139021791'

        obj = {
            'token': token,
            'uid': origin,
            'to': phone,
            'text': msg 
        }

        x = requests.post(url, data = obj)
        logger.info(x.text)
        logging.debug("Enviando msg")

    def dayone_messages(self):

        logger.debug("Enviando dayone messages")

        msgs = [
        # msg 1
        "Ooi, boa tarde, tudo jóia?! \n"
        "Aqui é o Gabriel da Suitable, somos uma empresa aqui de Santa Cruz do Sul - RS.",
        # msg 2
        'Encontrei vocês nas redes sociais, gostei da forma como trabalham e me chamou a atenção, vi que tem um produto muito bom, de qualidade, bem apresentado..',
        # msg 4
        "Isto me chamou a atenção, hoje trabalhamos com automatização de WhatsApp, aplicativo de pedidos e sistema de gestão, com essas soluções, possibilitamos a padronização do atendimento, aumento de vendas e redução de custos 😊",
        # msg 5
        "Você tem um tempinho para falarmos a respeito disso? \n"
        "Desde já, agradeço a atenção!",
        ]

        for m in msgs:
            self.send_msg('555199959269', m)
        
        logger.debug("Finalizando ciclo envio messages dayone")
