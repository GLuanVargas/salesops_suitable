from django.http import HttpResponse
from django.views.decorators.http import require_POST
from processors.organization import Organization
import logging
import json

logger = logging.getLogger(__name__)

@require_POST
def example(request):

    logger.info('Entrou na request EXAMPLE')
    
    if request.body:
        logger.info('Corpo da request tem informações')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        logger.info(body)

        logger.info(body.get("meta").get("id"))
        deal_id = body.get("meta").get("id")
        
    else: 
        logger.info('Request sem nada')

    return HttpResponse('Hello, world. This is the webhook response.')

@require_POST
def organization(request):

    logger.info('Entrou na request ORGANIZATION')
    
    if request.body:
        logger.info('Corpo da request tem informações')
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        logger.info(body)

        logger.info(body.get("meta").get("id"))
        deal_id = body.get("meta").get("id")
        
        current_org = body.get("current")
        previous_org = body.get("previous")

        org = Organization(deal_id, current_org, previous_org)
        org.check_cnpj()




    else: 
        logger.info('Request sem nada')

        

    return HttpResponse('Hello, world. This is the webhook response.')