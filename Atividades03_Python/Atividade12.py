"""  Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N
pessoas e ao final apresentar o nome da pessoa mais velha """


idade_mais_velha = 0
nome_mais_velho = ''
qtd_registros = 0 

try:
    
    qtd_registros = int(input('Digite o número de pessoas a serem avaliadas: '))
    
   
    if qtd_registros <= 0:
        print('Nenhum registro será feito. 👍')
        
        
    
    for i in range(qtd_registros):
        
        
        print(f"\n--- Pessoa {i+1} de {qtd_registros} ---")
        nome_atual = input('Digite o nome: ')
        idade_atual = int(input('Idade: '))
        
       
        if idade_atual > idade_mais_velha:
            

            idade_mais_velha = idade_atual
            nome_mais_velho = nome_atual
            

    if qtd_registros > 0:
        print(f'A pessoa mais velha é {nome_mais_velho}, com {idade_mais_velha} anos.')
        
except ValueError:
    print('Valor inválido❌. Certifique-se de digitar números inteiros para a quantidade e idade.')