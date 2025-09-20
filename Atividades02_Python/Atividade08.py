"""  Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade
desse número, caso contrário, imprimir o dobro do número """

from decimal import Decimal
try:
    num = float(input('Digite um número: '))
    num_corrigido =  Decimal(num)
    if num > 20:
        print(f'A metade de {num} é {num/2}')
    else:
        print(f'O dobro de {num} é {num*2}')
except ValueError:
    print('Númro inválido ❌')