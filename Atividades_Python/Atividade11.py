""" Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o 
numero informado e na linha de baixo o dobro deste número da seguinte forma:  
Numero -> X  
Dobro deste numero -> Y  """

try:
    numero_real = float(input('Digite seu número real: '))
    print(f'Numero -> {numero_real}')
    print(f'Dobro deste número -> {numero_real * 2}')
except ValueError:
    print('Número inválido ❌')