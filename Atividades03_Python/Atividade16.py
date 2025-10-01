"""  Escreva um programa que vá solicitando as idades dos alunos da sala até que todos
sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao
final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de
18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana. """


idade_dos_alunos = []
soma_de_idade = 0
while True:
    idade= int(input('Deseja informar a idade do próximo aluno, digite [0] para parar : '))

    if idade == 0:
        break
    
    idade_dos_alunos.append(idade)

idade_dos_alunos.sort()
print(f'A idade do aluno mais novo é {idade_dos_alunos[0]} e a idade do aluno mais velhor é {idade_dos_alunos[-1]}')

for numero in idade_dos_alunos:
    soma_de_idade += numero

media_aritmetica = soma_de_idade/len(idade_dos_alunos)

print(f'A media aritmética da idade dos alunos é: {media_aritmetica}')

N = len(idade_dos_alunos)

if N % 2 != 0:
    indice_mediana = N // 2
    mediana = idade_dos_alunos[indice_mediana]
    print(f'A mediana da lista de idade dos alunos é: {mediana} ')

else:
    indice_1 = N//2 -1
    indice_2 = N//2
    valor_primeiro = idade_dos_alunos[indice_1]
    valor_segundo = idade_dos_alunos[indice_2]
    print(f'A mediana da lista de idade dos alunos é : {valor_primeiro+valor_segundo/2}')

