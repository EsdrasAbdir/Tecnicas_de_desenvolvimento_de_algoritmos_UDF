""" Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como
par ou ímpar """

try:
    num_int = int(input('Digite um número inteiro: '))
    if num_int % 2 == 0:
        print(f'O número {num_int} é par 👍')
    else:
        print(f'O número {num_int} é ímpar 👍')
except ValueError:
    print(f'Número inválido ❌')