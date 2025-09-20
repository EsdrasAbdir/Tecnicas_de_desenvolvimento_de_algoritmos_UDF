"""  Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final 
apresente na tela os dois números informados formatando com duas casas decimais 
somente o número real da seguinte forma: "Voce informou os numeros N e X.YY" """



try:
    num_inteiro = int(input('Digite um numero inteiro: '))
    num_real = float(input('Digite um número real: '))
    print(f'Você informou o número {num_inteiro} e {num_real:.2f}')

except ValueError:
    print('Número inválido')