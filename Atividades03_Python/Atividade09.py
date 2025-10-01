"""Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade
de vezes que o texto "Hello World!" será impresso na tela, um em cada linha.  """

try:
    num_inteiro = int(input('Digite um número inteiro 😊: '))
    for i in range(1,num_inteiro+1):
        print(f'{i}) Hello World!\n')
except ValueError:
    print('Valor inválido ❌')