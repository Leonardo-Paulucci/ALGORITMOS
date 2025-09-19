musicas = [
    {
        "titulo": "Luz do Sol",
        "artista": "Ana Souza",
        "downloads": 1500,
        "avaliacoes": [5, 4, 5, 3, 4]
    },
    {
        "titulo": "Noite Serena",
        "artista": "Carlos Lima",
        "downloads": 2500,
        "avaliacoes": [4, 4, 5, 5, 5]
    },
    {
        "titulo": "Vento Livre",
        "artista": "Marina Alves",
        "downloads": 1800,
        "avaliacoes": [5, 5, 5, 4, 5]
    }
]

def calcular_media_avaliacoes(musicas):
    medias = {}
    for m in musicas:
        if m["avaliacoes"]:
            media = sum(m["avaliacoes"]) / len(m["avaliacoes"])
        else:
            media = 0
        medias[m["titulo"]] = round(media, 2)
    return medias

def artista_com_mais_downloads(musicas):
    downloads_por_artista = {}
    for m in musicas:
        artista = m["artista"]
        downloads_por_artista[artista] = downloads_por_artista.get(artista, 0) + m["downloads"]
    
    return max(downloads_por_artista, key=downloads_por_artista.get)

def ranking_musicas(musicas):
    return sorted(
        musicas,
        key=lambda m: sum(m["avaliacoes"]) / len(m["avaliacoes"]) if m["avaliacoes"] else 0,
        reverse=True
    )

print("Médias das músicas:", calcular_media_avaliacoes(musicas))
print("Artista com mais downloads:", artista_com_mais_downloads(musicas))

print("Ranking das músicas mais bem avaliadas:")
for m in ranking_musicas(musicas):
    media = sum(m["avaliacoes"]) / len(m["avaliacoes"])
    print(f"{m['titulo']} - {m['artista']} (Média: {media:.2f})")