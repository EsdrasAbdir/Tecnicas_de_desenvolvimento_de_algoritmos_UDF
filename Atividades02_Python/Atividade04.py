""" Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o
número informado é positivo, negativo ou nulo (zero) """

try:
    num_real =  float(input('Digite um número: '))

    if num_real > 0:
        print(f'O número {num_real} é positivo')
    elif num_real == 0:
        print(f'O número {num_real} é nulo')
    else:
        print(f'O número {num_real} é negativo')

except ValueError:
    print(f'Número inválido ❌')