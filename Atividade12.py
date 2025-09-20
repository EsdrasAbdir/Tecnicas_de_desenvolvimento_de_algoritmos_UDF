"""  Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e
90, ou não """

try:
    num =  int(input('Digite um número: '))
    if num in range(20,90):
        print(f'O número {num} está entre 20 e 90')
    else:
        print(f'O número {num} não está entre 20 e 90')
except ValueError:
    print(f'Número inválido ❌')