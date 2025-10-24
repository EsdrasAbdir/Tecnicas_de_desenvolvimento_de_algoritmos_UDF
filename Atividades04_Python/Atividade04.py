""" Faça um programa que solicita uma
quantidade indefinida de notas de uma
prova (deve parar quando um número
negativo for digitado).
Armazena em uma lista.
Após isso, o programa deve mostrar a média
das notas. 
Tarefa 4
"""

soma_das_notas = float()
notas = []
try:
    while True:
        nota = float(input('Digite sua nota ou um número negativo para parar😊: '))
        if nota < 0: 
            break
        else:
            notas.append(nota)
            soma_das_notas += nota
    def media_das_notas():
        media_do_aluno = soma_das_notas / len(notas)
        print(f'A media das notas é : {media_do_aluno}')

    media_das_notas()

except ValueError:
    print(f'A nota {nota} é inválido ❌')