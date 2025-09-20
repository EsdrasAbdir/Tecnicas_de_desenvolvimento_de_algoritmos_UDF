""" Refazer o exercício anterior, solicitando antes o múltiplo a ser testado """

try:
    num_int = int(input('Digite um número inteiro: '))
    if num_int % 3 == 0:
        print(f'O número {num_int} é múltiplo de 3')
    else:
        print(f'O número {num_int} não é múltiplo de 3 ')

except ValueError:
    print('Número inválido ❌')