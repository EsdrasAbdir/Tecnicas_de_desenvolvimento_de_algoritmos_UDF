""" Escreva um programa que aplica a função
módulo a todos os elementos e uma lista. """

lista = [2,3,-5,-10,8,-30]

lista_corrrigida = []
numero_absoluto = ''
for numero in lista: 
    numero_absoluto = numero.__abs__()
    lista_corrrigida.append(numero_absoluto)

print(f'A lista com números absolutos é: {lista_corrrigida} ')
print(f'A lista original é : {lista} ')