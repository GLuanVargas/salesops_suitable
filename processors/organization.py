import requests
import datetime
import logging

logger = logging.getLogger(__name__)

class Organization:

    def __init__(self, id, current, previous):
        logger.info('Objeto organization instanciado')
        self.id = id
        self.current = current
        self.previous = previous

    def check_cnpj(self):
        logger.info('function de check cnpj chamada')
        
        current_cnpj = self.replace_cnpj(self.current['672b8609651a4abb49163251348abb68ea3d4c32'])
        previous_cnpj = self.replace_cnpj(self.previous['672b8609651a4abb49163251348abb68ea3d4c32'])

        if current_cnpj != previous_cnpj:
            logger.info('cnpj anterior diferente do atual')
            logger.info('CNPJ ATUAL')
            logger.info(current_cnpj)
            
            logger.info('CNPJ ANTERIOR')
            logger.info(previous_cnpj)
            
            self.update_cnpj()

            return True

        logger.info('nao mudou cnpj')
        return False

    def update_cnpj(self):
        logger.info('fazendo UPDATE do cnpj')
        current_cnpj = self.replace_cnpj(self.current['672b8609651a4abb49163251348abb68ea3d4c32'])

        logger.info('cnpj: ' + str(current_cnpj))
        url = 'https://www.receitaws.com.br/v1/cnpj/' + current_cnpj
        logger.info('chamando URL')
        logger.info(url)

        response = requests.get(url)
        company_data = response.json()

        logger.info('company data')
        logger.info(company_data)

        data_formatada = datetime.datetime.strptime(company_data['abertura'], "%d/%m/%Y").strftime("%Y-%m-%d")

        pipedrive_data = dict()
        pipedrive_data["2b7009936b355a66aa43ff9c315aac486c28bc2c"] = company_data['nome']
        pipedrive_data["4b25cee90f86703c7db4aea12bc6f5596d71b082"] = company_data['fantasia']
        pipedrive_data["fb92beab971dc23d02eec68f3d5a5916cb8ecea3"] = data_formatada
        pipedrive_data["672b8609651a4abb49163251348abb68ea3d4c32"] = company_data['cnpj']
        pipedrive_data["9d3909646b10da284bd804bea07f4ad78ca6ea70"] = company_data['porte']
        pipedrive_data["3abe545c7a7304abd868148d8717fba752cfda75"] = company_data['natureza_juridica']
        pipedrive_data["fc37c855c0f47dd110f52094665ac3a682db3c21"] = float(company_data['capital_social'])
        pipedrive_data["2aaf0208a2bb64479f0a2ac55af10b3cdac7d997"] = company_data['situacao']
        cnae_principal = company_data['atividade_principal'][0]

        cnae_prim_sec = ''
        cnae_prim_sec += 'Atividade principal: ' + '\n'
        cnae_prim_sec += 'Codigo: ' + cnae_principal.get('code') + ' | Atividade: ' + cnae_principal.get('text')
        cnae_prim_sec += '\n' + 'Atividades secundárias: ' + '\n'

        cnaes_secundarios = company_data['atividades_secundarias']

        for cnae in cnaes_secundarios:
            cnae_prim_sec += 'Codigo: ' + cnae.get('code') + ' | Atividade: ' + cnae.get('text')
            cnae_prim_sec += '\n'

        pipedrive_data["29313b6413c81943941ef1ca08ddac36a122fe14"] = cnae_prim_sec

        api_token = 'af6014e1b668c2451d9ccadd13b14e12a2645828'
        company_domain = 'suitable2'
        url_update_org = 'https://' + company_domain + '.pipedrive.com/api/v1/organizations/' + str(self.id) +  '?api_token=' + api_token

        requests.put(url_update_org, pipedrive_data)
        logger.info('Procedimento finalizado')

        return True


    def replace_cnpj(self, cnpj):
        cnpj = cnpj.replace('.', '').replace('-','').replace('/','').strip()

        return cnpj