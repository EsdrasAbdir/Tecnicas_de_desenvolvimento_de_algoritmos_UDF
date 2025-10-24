""" Escreva um programa que apaga todos os
elementos negativos de uma lista.
TAREFA 3 """

lista = [2,-3,4,5,8,-10,-30]

lista_com_positivos = []

for numero in lista:
    if numero < 0:
      continue
    else:
       lista_com_positivos.append(numero)

print(f'A lista somente com números positivos é : {lista_com_positivos}')