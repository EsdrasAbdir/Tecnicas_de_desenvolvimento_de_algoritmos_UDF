""" 0. Elabore um algoritmo que solicite ao usuário uma palavra e um número inteiro que
indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada
linha """

try:
    palavra = input('Digite uma palavra😊: ')
    numero_inteiro = int(input('Digite um número inteiro👍: '))
    for i in range(1,numero_inteiro+1):
        print(f'{i}) {palavra}\n')

except ValueError:
    print('Valor inválido ❌')