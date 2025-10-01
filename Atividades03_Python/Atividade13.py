""" Elabore um algoritmo que leia um número de entrada que indicará a quantidade de
registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N
pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados. """


qtd_registros = 0
num_homens = 0
num_mulheres = 0
idade_masculina = 0
soma_de_idades_masculinas = 0
idade_feminina = 0
soma_de_idades_femininas = 0
try:
    qtd_registros = int(input('Digite a quantidade de registros: '))

    for i in range(qtd_registros):
        sexo = input('Digite o sexo da pessoa -> [M]asculino ou [F]eminino: ').upper()

        if sexo == 'M':
            idade_masculina = int(input('Digite a idade dele: '))
            num_homens += 1
            soma_de_idades_masculinas += idade_masculina
            
        elif sexo == 'F':
            idade_feminina = int(input('Digite a idade dele: '))
            num_mulheres += 1
            soma_de_idades_femininas += idade_feminina

        else:
            print('Digite [M] para masculino 🤷‍♂️ ou [F] para feminino 🤷‍♀️')

        
    if num_homens > 0:
        media_masculina = soma_de_idades_masculinas/num_homens
        print(f'A média idade/número de homens é {media_masculina}')
    else:
        print('Nenhum registro de homem foi colocado')

    if num_mulheres> 0:  
        media_feminina = soma_de_idades_femininas/num_mulheres 
        print(f'A média idade/número de mulheres é {media_feminina}')
    else:
        print('Nenhum registro de mulheres foi colocado')

except ZeroDivisionError:
    if num_mulheres == 0:
        print('Sem mulheres')
    elif num_homens == 0:
        print('Sem homens')