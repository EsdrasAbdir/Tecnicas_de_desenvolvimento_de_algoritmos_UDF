"""  Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela 
o número informado pelo usuário do programa  """

numero = input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    print(numero_int)

else:
    print('Número inválido ❌')