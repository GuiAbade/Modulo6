# Primeiro casso
'''try:
    meses = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    print(meses[15])
except IndexError as erro:
    print('Favor, acessar indice válido')
'''

# Segundo caso

'''internet = None
try:
    print('Fazendo conezão com a ' + internet)
except TypeError as erro:
    print('Não há conexão com a internet')
finally:
    print('Desfazendo a compra!')'''

# Terceiro caso
try:
    valor = int(input('Digite um valor: '))
    print(valor / 0)
except ZeroDivisionError as erro:
    print('Não é possível dividir por zero!')
except ValueError as erro:
    print('Favor, digitar apenas números!')
finally:
    print('A operação foi cancelada')
