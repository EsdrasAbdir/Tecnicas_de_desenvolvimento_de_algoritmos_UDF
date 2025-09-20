"""Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo
de 3, ou, não é múltiplo de 3 """

try:
    num_int = int(input('Digite um número inteiro: '))
    if num_int % 3 == 0:
        print(f'O número {num_int} é múltiplo de 3')
    else:
        print(f'O número {num_int} não é múltiplo de 3 ')

except ValueError:
    print('Número inválido ❌')