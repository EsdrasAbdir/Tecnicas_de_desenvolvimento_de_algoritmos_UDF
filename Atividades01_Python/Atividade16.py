""" . Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendido
no mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.
 """

# fórmula : Valor das Vendas x (Percentagem da Comissão / 100) = Comissão
try:
    salario_fixo_vendedor = float(input('Digite o seu salário fixo: '))
    total_vendido = float(input('Digite o total vendido: '))
    percentual_comissao =  float(input('Digite o percentual da comissão :  %'))
    salario_bruto = print(f'O salário bruto é {total_vendido * (percentual_comissao/100) + salario_fixo_vendedor}')
except ValueError:
    print('Número inválido ❌')
