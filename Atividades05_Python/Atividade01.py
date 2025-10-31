""" Quantos alunos existem?
Alguém tirou nota zero?
Qual foi a menor nota?
Qual foi a maior nota?
alunos = {
"Alice": 8.5,
"Bruno": 7.8,
"Carla": 9.2,
"Diego": 6.9,
"Eva": 8.0,
"Fernando": 7.5,
"Gabriela": 9.0,
"Henrique": 6.7,
"Isabela": 8.3,
"João": 7.2
}
TAREFA 1
Dado o dicionário ao lado, imprima os
seguintes dados: """

alunos = {
"Alice": 8.5,
"Bruno": 7.8,
"Carla": 9.2,
"Diego": 6.9,
"Eva": 8.0,
"Fernando": 7.5,
"Gabriela": 9.0,
"Henrique": 6.7,
"Isabela": 8.3,
"João": 7.2
}

numero_de_alunos = len(alunos)
todas_as_notas = list(alunos.values())

print(f'O número de alunos é {numero_de_alunos}')

menor_nota = min(todas_as_notas)
print(f'A menor nota foi {menor_nota}')

maior_nota = max(todas_as_notas)
print(f'A maior nota é {maior_nota}')