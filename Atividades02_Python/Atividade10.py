""" O sistema de avaliação de determinada disciplina é composto por três provas. A primeira
prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Considerando que a
média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno
desta disciplina e dizer se o aluno foi aprovado ou não """
from decimal import Decimal

try:
    nota_1 = float(input('Digite a nota da primeira prova: '))
    nota_2 = float(input('Digite a nota da segunda prova: '))
    nota_3 = float(input('Digite a nota da terceira prova: '))
    nota_peso_dois = Decimal(nota_1 * 2)
    nota_peso_tres = Decimal(nota_2 * 3)
    nota_peso_cinco = Decimal(nota_2 * 5)
    media = Decimal(nota_peso_dois * nota_peso_tres * nota_peso_cinco)/3
    if media >= 6:
        print('Você foi aprovado 👍')
    else:
        print(f'Você foi reprovado ❌')
except ValueError:
    print(f'Número inválido ❌')

