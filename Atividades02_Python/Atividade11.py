"""Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da
pessoa mais pesada  """


pessoa_1 = {
    'nome': 'João',
    'peso_kg': 80,
}

pessoa_2 = {
    'nome': 'Vitor',
    'peso': 60,
}


if pessoa_1['peso_kg'] > pessoa_2['peso']:
    print(f'O {pessoa_1['nome']} é mais pesada que a {pessoa_2['nome']}')

else:
    print(f'O {pessoa_2["nome"]} é mais pesada que a {pessoa_1["nome"]}')

