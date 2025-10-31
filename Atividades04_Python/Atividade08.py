""" TAREFA 8
Faça um programa que solicita que o
usuário digite o nome e a idade de diversas
pessoas (o programa deve parar quando
um nome vazio for informado).
Retorne o nome da pessoa mais velha """

idades = [] 
nomes = []

while True:
    nome_atual = input('Digite seu nome: ')
    if nome_atual == '':
        break

    try:
        idade_atual = int(input('Digite sua idade: '))
    except ValueError:
        print('Idade inválida❌')
        
    nomes.append(nome_atual)
    idades.append(idade_atual)

if not nomes:
    print('Sem nomes!')
else:
    idade_maximo = max(idades)
    indice_pessoa_mais_velha = idades.index(idade_maximo)

    nome_da_pessoa_mais_velha = nomes[indice_pessoa_mais_velha]

    print(f'A pessoa mais velha é {nome_da_pessoa_mais_velha}')