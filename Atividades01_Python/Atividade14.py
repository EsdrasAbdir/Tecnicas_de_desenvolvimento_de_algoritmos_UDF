""" Escreva um programa que solicite ao usuário dois números reais e ao final apresente na 
tela o produto dos dois números informados da seguinte forma: "O produto dos numeros N 
e X corresponde a Y" """

try:
    num_1 =  float(input('Digite um número real: '))
    num_2 =  float(input('Digite o segundo número real: '))
    print(f'O produto dos numeros {num_1} e {num_2} corresponde a {num_1*num_2}')
except ValueError:
    print('Número inválido ❌')