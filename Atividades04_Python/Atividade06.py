""" Faça um programa que solicita uma
quantidade indefinida de números positivos
(deve parar quando um número negativo for
digitado).
Armazene todos os números digitados em
uma lista, sem repetição.
TAREFA 6 """



try:
    lista_numeros_positivos = []
    lista_numero_nao_repetidos = []
    
    while True: 
        numero = float(input('Digite um número positivo para colocar na lista ou um número negativo para sair👍: '))
        if numero < 0:
            break
        else:
            lista_numeros_positivos.append(numero)
    
    for numero in lista_numeros_positivos:
        if numero in lista_numero_nao_repetidos:
            continue
        else:
            lista_numero_nao_repetidos.append(numero)

    print(f'A lista de números não repetidos é : {lista_numero_nao_repetidos}')   

except ValueError:
    print(f'O número {numero} é inválido ❌🤷‍♂️')

