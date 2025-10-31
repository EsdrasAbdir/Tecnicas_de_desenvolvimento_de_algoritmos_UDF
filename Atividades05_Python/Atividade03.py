""" bandas = {
"Gangrena Gasosa": [
{"álbum": "Gente Ruim Só Manda Lembrança Pra Quem Não Presta", "ano":
2019},
{"álbum": "Se Deus É 10, Satanás É 666", "ano": 1999},
{"álbum": "Welcome to the Macumba", "ano": 1993}
],
"Rogério Skylab": [
{"álbum": "Nas Portas do Cu", "ano": 2023},
{"álbum": "Crítica da Faculdade do Cu", "ano": 2021},
{"álbum": "Cosmos", "ano": 2019}
],
"Garotos Podres": [
{"álbum": "Canções para Ninar", "ano": 2003},
{"álbum": "Com a Corda Toda", "ano": 1997},
{"álbum": "Rock de Subúrbio", "ano": 1995}
],
"Massacration": [
{"álbum": "Live Metal Espancation", "ano": 2017},
{"álbum": "Good Blood Headbanguers", "ano": 2009},
{"álbum": "Gates of Metal Fried Chicken of Death", "ano": 2005}
],
"Raimundos": [
{"álbum": "Cantigas de Roda", "ano": 2014},
{"álbum": "Roda Viva", "ano": 2006},
{"álbum": "Éramos 4", "ano": 2001}
]
}
TAREFA 3
Dado o dicionário ao lado:
Imprima o álbum mais antigo
imprima a banda que tem o maior
intervalo entre os álbuns
Imprima todos os álbuns do mais novo
para o mais antigo, dizendo também o
nome da banda """

bandas = {
    "Gangrena Gasosa": [
        {"álbum": "Gente Ruim Só Manda Lembrança Pra Quem Não Presta", "ano": 2019},
        {"álbum": "Se Deus É 10, Satanás É 666", "ano": 1999},
        {"álbum": "Welcome to the Macumba", "ano": 1993}
    ],
    "Rogério Skylab": [
        {"álbum": "Nas Portas do Cu", "ano": 2023},
        {"álbum": "Crítica da Faculdade do Cu", "ano": 2021},
        {"álbum": "Cosmos", "ano": 2019}
    ],
    "Garotos Podres": [
        {"álbum": "Canções para Ninar", "ano": 2003},
        {"álbum": "Com a Corda Toda", "ano": 1997},
        {"álbum": "Rock de Subúrbio", "ano": 1995}
    ],
    "Massacration": [
        {"álbum": "Live Metal Espancation", "ano": 2017},
        {"álbum": "Good Blood Headbanguers", "ano": 2009},
        {"álbum": "Gates of Metal Fried Chicken of Death", "ano": 2005}
    ],
    "Raimundos": [
        {"álbum": "Cantigas de Roda", "ano": 2014},
        {"álbum": "Roda Viva", "ano": 2006},
        {"álbum": "Éramos 4", "ano": 2001}
    ]
}

# Lista para armazenar todos os álbuns no formato (ano, álbum, banda)
todos_os_albuns = []
maior_intervalo = -1
banda_maior_intervalo = ""

for nome_banda, lista_albuns in bandas.items():
    
    for album_dict in lista_albuns:
        ano = album_dict["ano"]
        album = album_dict["álbum"]
        todos_os_albuns.append((ano, album, nome_banda))

   
    anos_da_banda = [album_dict["ano"] for album_dict in lista_albuns]
    
    ano_max = max(anos_da_banda)
    ano_min = min(anos_da_banda)
    intervalo_atual = ano_max - ano_min
    
    if intervalo_atual > maior_intervalo:
        maior_intervalo = intervalo_atual
        banda_maior_intervalo = nome_banda


album_mais_antigo = min(todos_os_albuns)
ano_antigo, nome_album_antigo, banda_antiga = album_mais_antigo
print("--- Álbum Mais Antigo ---")
print(f"Álbum: {nome_album_antigo} (Banda: {banda_antiga}, Ano: {ano_antigo})")


print("\n--- Banda com o Maior Intervalo ---")
print(f"Banda: {banda_maior_intervalo} (Intervalo: {maior_intervalo} anos)")


albuns_ordenados = sorted(todos_os_albuns, reverse=True)
print("\n--- Todos os Álbuns (Mais Novo para o Mais Antigo) ---")
for ano, album, banda in albuns_ordenados:
    print(f"Ano: {ano} | Álbum: {album} | Banda: {banda}")

