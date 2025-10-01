""" Elabore um algoritmo que imprima todos os números ímpares de 1000 até 0  """

numero = 1000
while numero >= 0:
    if numero % 2 != 0:
        print(f'O número {numero} é ímpar 👍')
        numero -= 1
    else:
        numero -= 1
        continue
