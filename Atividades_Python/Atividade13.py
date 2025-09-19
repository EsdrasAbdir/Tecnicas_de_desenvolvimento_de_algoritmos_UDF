"""  Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente 
na tela a soma dos dois números informados da seguinte forma: "O numeros N e X 
somados correspondem a Y"  """

try:
    num_1 = int(input('Digite um número inteiro: '))
    num_2 =  int(input('Digite o segundo número inteiro: '))
    print(f'Os numeros {num_1} e {num_2} somados correspondem a {num_1 + num_2}')

except ValueError:
    print('Número inválido 😒')