""" Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado
seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele """

try:
    num_1 =  int(input('Digite um número inteiro: '))
    num_2 =  int(input('Digite o segundo número inteiro: '))
    soma =   num_1 + num_2
    print(f'A soma de {num_1} e {num_2} é {num_1 + num_2}')
    if soma > 10:
        print(f'O quadrado da {soma} é {soma**2}')
    else:
        print(f'A metade da {soma} é {soma/2}')
except ValueError:
    print(f'Número inválido ❌')