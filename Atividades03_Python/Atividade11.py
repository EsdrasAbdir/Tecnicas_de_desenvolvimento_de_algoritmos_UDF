""" Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
números a serem lidos. Em seguida, leia n números (conforme o valor informado
anteriormente) e imprima a soma e a média aritmética dos números informados. """
soma = 0
qtd = 0

try:
    qtd = int(input('Digite um número👍: '))
    if qtd  <= 0:
        print("A quantidade de ser um número inteiro positivo.")

    for i in range(qtd):
        numero_atual = int(input(f'Digite o {i+1}. número: '))   
        soma += numero_atual

    media = soma/qtd

    print(f'soma: {soma}')
    print(f'Média aritmética: {media:.2f}')    
except ValueError:
    print(f'Número inválido ❌')

except ZeroDivisionError:
    print(f'Impossível divisão por 0 😒')