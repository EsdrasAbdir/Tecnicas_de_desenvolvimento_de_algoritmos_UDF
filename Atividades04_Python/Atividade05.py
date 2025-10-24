""" Faça um programa que solicita uma
quantidade indefinida de números positivos
(deve parar quando um número negativo for
digitado).
Armazene-os em duas listas:
uma para os números pares;
outra para os números ímpares.
A seguir, mostre a porcentagem de pares e
ímpares digitados.
TAREFA 5 """



lista_numeros_par = []
lista_numeros_impar = []

try:
    while True:
        numero = int(input('Digite um número positivo ou um número negativo para parar👍: '))
        if numero < 0:
            break

        elif numero % 2 == 0:
            lista_numeros_par.append(numero)
            lista_com_par_e_impar = lista_numeros_par + lista_numeros_impar

        else:
            lista_numeros_impar.append(numero)
            lista_com_par_e_impar = lista_numeros_par + lista_numeros_impar


   
    porcentagem_par = (len(lista_numeros_par)/len(lista_com_par_e_impar)) * 100
    porcentagem_impar = (len(lista_numeros_impar)/len(lista_com_par_e_impar)) * 100

    print(f'A lista com numeros par é : {lista_numeros_par}')
    print(f'A lista com numeros ímpar é : {lista_numeros_impar}')

    print(f'A porcentagem de número par é : {porcentagem_par:.0f} % ' )
    print(f'A porcentagem de número ímpar é : {porcentagem_impar:.0f} %')
    

except ValueError:
    print('Número {numero} é inválido ❌ ! ')
