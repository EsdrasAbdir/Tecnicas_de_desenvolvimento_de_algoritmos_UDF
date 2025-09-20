"""Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se
o número informado é maior ou igual a dez ou menor que 10 """

try:
    numero_real =  float(input('Digite um número real: '))

    if numero_real >= 10:
        print(f'O número {numero_real} é maior ou igual a 10')

    else: 
        print(f'O número  {numero_real} é menor que 10 ')

except ValueError:
    print(f'Número inválido ❌')