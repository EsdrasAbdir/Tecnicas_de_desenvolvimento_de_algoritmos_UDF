"""  Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela 
o número informado da seguinte forma: "Foi informado o valor: X" """


numero =  input('Digite um número inteiro: ')

if numero.isdigit():
    numero_int = int(numero)
    print(f'Foi informado o valor: {numero_int}')

else: 
    print('Número inválido ❌')