""" Imprima o total de episódios
Substitua a quantidade de episódios pelo
percentual (ep_anime/ep_total)
Imprima nome e percentual de cada
anime, em ordem decrescente de
percentual
animes = { "Naruto": 220,
"Jujutsu Kaisen": 47, "Dragon Ball Z": 291, "Death Note": 37,
"Fullmetal Alchemist": 64,
"Evangelion": 26,
"Berserk": 25,
"Code Geass": 50, "Akame ga Kill!": 24, "Elfen Lied": 13
}
TAREFA 2
Dado o dicionário ao lado """


animes = { "Naruto": 220,
"Jujutsu Kaisen": 47, "Dragon Ball Z": 291, "Death Note": 37,
"Fullmetal Alchemist": 64,
"Evangelion": 26,
"Berserk": 25,
"Code Geass": 50, "Akame ga Kill!": 24, "Elfen Lied": 13
}

lista_percentuais = []

ep_total = animes.values()

soma_do_ep_total = sum(ep_total)

print(soma_do_ep_total)

for nome_anime, ep_anime in animes.items():
    percentual = ep_anime/soma_do_ep_total * 100
    lista_percentuais.append((percentual,nome_anime))
    print(f'{nome_anime} tem porcentagem de {percentual:.2f} %')

lista_ordenada = sorted(lista_percentuais,reverse=True)

print('--------------------------Lista decrescente-----------------------')
for percentual_ordenado, nome_anime_ordenado in lista_ordenada:
    print(f'Anime: {nome_anime_ordenado} -> {percentual_ordenado:.2f}%')



