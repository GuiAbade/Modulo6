# Logging
import logging
'''
DEBUG: Mensagem de DEBUG - usada para diagnósticos detalhados
INFO: Mensagem de INFO - usada para informações gerais
WARNING: Mensagem de WARNING - alerta sobre algo inesperado
ERROR: Mensagem de ERROR - indica um erro que pode afetar o programa
CRITICAL: Mensagem de CRITICAL - indica um erro grave ou falha crítica
'''
logging.basicConfig(level=logging.DEBUG, filename='app.log',
                    filemode='a', format='%(levelname)s - %(message)s')
# Niveis de gravidade de loggin
logging.debug("Isso é um log de depuração")  # Informação para desenvolvedores
# Informa oque esta acontecendo no programa
logging.info("Isso é um log de informação")
# Informa algo acontecendo fora do esperados e que pode gera erro
logging.warning("Isso é um log de aviso")
# Informa um erro ocorreu na aplicação
logging.error("Isso é um log de erro")
# Informa um erro grave que pode comprometer fatalmente a aplicação
logging.critical("Isso é um log crítico")
