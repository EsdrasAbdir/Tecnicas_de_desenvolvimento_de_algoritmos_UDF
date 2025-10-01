""" Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o
maior e o menor deles. """

numeros = []
numero_maior = 0

for i in range(10):
    numeros.append(float(input('Digite um número: ')))
    

for numero in numeros:
    if numero > numero_maior:
        numero_maior = numero

print(f'O número maior da lista é {numero_maior}')