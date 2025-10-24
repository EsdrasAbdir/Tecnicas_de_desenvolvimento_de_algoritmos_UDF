""" Escreva um programa que solicita que o
usuário digite 5 números inteiros e os coloca
em uma lista.
Quando terminar, imprima a lista.
TAREFA 1 """


try:
    lista = []
    numero_inteiro = ''
    while len(lista) <= 5:
        numero_inteiro = int(input('Digite um número inteiro: '))
        lista.append(numero_inteiro)
        if len(lista) == 5:
            print(f'Sua lista é : {lista}')
            break
except ValueError:
    print('Número inválido ❌')

