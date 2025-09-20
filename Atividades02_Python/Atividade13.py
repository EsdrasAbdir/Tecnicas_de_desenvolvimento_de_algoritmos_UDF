"""Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se
são iguais """

try: 
    num_1 = float(input('Digite um número: '))
    num_2 = float(input('Digite o segundo número: '))
    if num_1 > num_2:
        print(f'O número {num_1} é maior que {num_2} 👍')
    elif num_1 == num_2:
        print(f'Os números {num_1} é igual a {num_2} 👍')
    else:
        print(f'O número {num_2} é maior que {num_1} 👍')
except ValueError:
    print(f'Número inválido ❌')