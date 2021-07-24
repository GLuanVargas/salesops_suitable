import logging
from processors.message import Message

logger = logging.getLogger(__name__)

class Deal:

    def __init__(self, id, current, previous):
        logger.info('Objeto deal instanciado')
        self.id = id
        self.current = current
        self.previous = previous

    def check_actions(self):

        self.check_stage()

        return True

    def check_stage(self):

        curr_stage = self.current["stage_id"]
        prev_stage = self.previous["stage_id"]

        
        logging.debug("Estagio atual:")
        logging.debug(curr_stage)

        logging.debug("Estagio anterior:")
        logging.debug(prev_stage)

        if curr_stage != prev_stage and curr_stage == 22:
            logging.debug("Enviando msg estagio 22")
            msg = Message()
            msg.dayone_messages()

