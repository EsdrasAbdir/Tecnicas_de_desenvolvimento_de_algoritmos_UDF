""" Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o 
número informado formatado com duas casas decimais da seguinte forma: "Voce informou 
o numero X.YY"  """


try:
    numero_real = float(input('Digite um número real: '))
    print(f'Você informou o numero {numero_real:.2f}')
except ValueError:
    print('Número inválido ❌')