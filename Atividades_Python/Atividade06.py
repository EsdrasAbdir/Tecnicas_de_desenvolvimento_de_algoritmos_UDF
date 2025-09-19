"""Escreva um programa que solicite ao usuário a temperatura em graus Celsius e ao final 
apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32   """

temperatura_em_celsius = input('digite a temperatura em celsius: ')

if temperatura_em_celsius.isdigit():
    temperatura_em_celsius_corrigida = int(temperatura_em_celsius)
    temperatura_em_farenheit = temperatura_em_celsius_corrigida * 1.8 + 32
    print(temperatura_em_farenheit)

else:
    print('Temperatura inválida ❌')