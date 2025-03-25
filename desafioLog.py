import logging

logging.basicConfig(level=logging.DEBUG, filename='desafio.log',
                    format='%(asctime)s - %(levelname)s - %(message)s')
email = input('Digite seu email')
senha = int(input('Digite sua senha'))

try:
    if senha == 1234:
        print('Login feito com sucesso')
        logging.info(f'{email} entrou em sua conta bancária')
except ValueError as erro:
    print('Digite apeenas números')
    logging.info(erro)
