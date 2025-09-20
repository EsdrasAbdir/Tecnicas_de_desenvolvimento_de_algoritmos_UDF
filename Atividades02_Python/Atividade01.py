""" Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se o
número informado é maior que 10 (dez) """

try:
    num_real = float(input('Digite um número real: '))
    if num_real > 10:
        print(f'O número {num_real} é maior que 10 👍')
    else:
        print(f'O número {num_real} não é maior que 10 👍')
except ValueError:
    print(f'Número inválido ❌')