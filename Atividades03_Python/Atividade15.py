""" Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor
nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente. """



numeros_reais = []
numero_real = 0
while True:
    numero_real = float(input('Digite um número real ou 0 para parar: '))
    if numero_real == 0:
        break
    numeros_reais.append(numero_real)

numeros_reais.sort()
print(numeros_reais)