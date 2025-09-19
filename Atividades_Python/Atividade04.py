"""  Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na 
tela os dois números informados da seguinte forma: "Voce informou os numeros X e Y"  """
numero_1 = input('Digite um número inteiro: ')
numero_2 = input('Digite o segundo número inteiro: ')

if numero_1.isdigit() and numero_2.isdigit():
    numero_int_1 = int(numero_1)
    numero_int_2 = int(numero_2)
    print(f'Voce informou os numeros {numero_int_1} e {numero_int_2}')

else:
    print('Número inválido ❌')