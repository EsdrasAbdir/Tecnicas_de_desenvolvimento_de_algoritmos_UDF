"""  Reescrever o programa anterior apresentando o quadrado e o cubo do número informado  """

from decimal import Decimal
try:
    numero_real = input('Digite um número real: ')
    numero_decimal = Decimal(numero_real)
    quadrado_do_numero = print(f'O quadrado do {numero_decimal} é {numero_decimal**2}')
    cubo_do_numero = print(f'O cubo do {numero_decimal} é {numero_decimal**3}')
except ValueError:
    print('Número inválido ❌')