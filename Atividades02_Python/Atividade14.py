"""  Escreva um programa em linguagem C que solicite ao usuário a média para aprovação
em um curso e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao
final imprima a frase: "O aluno XXXXX foi aprovado com media YY" considerando o gênero
do(a) aluno(a) e se foi aprovado(a) ou reprovado(a) """

from decimal import Decimal

try:
    media_para_passar = int(input('Digite a média para passar: '))
    nome =  input('Digite seu nome: ').isalpha()
    sexo = input('Digite seu sexo [m]asculino ou [f]eminino ')
    primeira_nota =  float(input('Digite sua primeira nota: '))
    segunda_nota =  float(input('Digite sua segunda nota: '))
    terceira_nota =  float(input('Digite sua terceira nota: '))
    media =  Decimal(primeira_nota + segunda_nota + terceira_nota)/3
    if sexo.upper() == 'M' and media >= media_para_passar:
        print(f'O aluno  foi aprovado com media {media}')
    elif sexo.upper()== 'F' and media >= media_para_passar:
        print(f'A aluna  foi aprovado com media {media}')
    elif sexo.upper()== 'F' and media < media_para_passar:
        print(f'A aluna  não foi aprovado com media {media} ')

    else: 
        print(f'O aluno não foi aprovado com media {media} ') 
      
except ValueError:
    ...