""" TAREFA 7
Escreva um programa que solicita que o
usuário digite a altura e o peso de 5 pessoas.
Verifique se pelo menos duas das pessoas
tem a mesma altura e mesmo peso. """

altura_primeira_pessoa = input('Digite a altura da primeira pessoa: ')
peso_primeira_pessoa =input('Digite o peso da primeira pessoa: ')
altura_segunda_pessoa = input('Digite a altura da segunda pessoa: ')
peso_segunda_pessoa =input('Digite o peso da segunda pessoa: ')
altura_terceira_pessoa = input('Digite a altura da terceira pessoa: ')
peso_terceira_pessoa =input('Digite o peso da terceira pessoa: ')
altura_quarta_pessoa = input('Digite a altura da quarta pessoa: ')
peso_quarta_pessoa =input('Digite o peso da quarta pessoa: ')
altura_quinta_pessoa = input('Digite a altura da quinta pessoa: ')
peso_quinta_pessoa =input('Digite o peso da quinta pessoa: ')


primeira_pessoa = [altura_primeira_pessoa, peso_primeira_pessoa]
segunda_pessoa = [altura_segunda_pessoa,peso_segunda_pessoa]
terceira_pessoa = [altura_terceira_pessoa,peso_terceira_pessoa]
quarta_pessoa = [altura_quarta_pessoa,peso_quarta_pessoa]
quinta_pessoa = [altura_quinta_pessoa,peso_quinta_pessoa]
lista_das_cinco_pessoas = [primeira_pessoa,segunda_pessoa,terceira_pessoa,quarta_pessoa,quinta_pessoa]

encontrou_duplicata = False
for pessoa in lista_das_cinco_pessoas:
    if lista_das_cinco_pessoas.count(pessoa) >=2 :
        encontrou_duplicata = True
    
if encontrou_duplicata == True:
    print('verificado pessoa com mesma altura e peso!')
else:
    print('Não encontrado pessoa com mesma altura e peso')