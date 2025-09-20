""" Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final 
apresente na tela a letra informada pelo usuário da seguinte forma: "Voce digitou w"  """


primeira_letra_nome = input('Digite a primeira letra do seu nome: ')
if len(primeira_letra_nome) == 1:
    print(f'Você digitou {primeira_letra_nome}') 

else:
    print('letra inválida ❌')