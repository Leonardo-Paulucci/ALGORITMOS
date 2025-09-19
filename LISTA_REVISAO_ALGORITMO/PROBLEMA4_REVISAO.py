filmes = [
    {
        "titulo": "Aventura no Espaço",
        "diretor": "João Silva",
        "bilheteria": 500,
        "avaliacoes": [8, 9, 7, 8, 9]
    },
    {
        "titulo": "Mistério Sombrio",
        "diretor": "Maria Costa",
        "bilheteria": 350,
        "avaliacoes": [9, 8, 8, 9, 10]
    },
    {
        "titulo": "Risos e Lágrimas",
        "diretor": "João Gomes",
        "bilheteria": 420,
        "avaliacoes": [7, 8, 7, 8, 7]
    },
    {
        "titulo": "O Alpinista",
        "diretor": "Carlos Lima",
        "bilheteria": 600,
        "avaliacoes": [9, 9, 8, 10, 9]
    }
]

def top_bilheteria(filmes):
    return sorted(filmes, key=lambda f: f["bilheteria"], reverse=True)[:3]

def top_avaliacao(filmes):
    return sorted(
        filmes,
        key=lambda f: sum(f["avaliacoes"]) / len(f["avaliacoes"]),
        reverse=True
    )[:3]

def bilheteria_por_diretor(filmes):
    resultados = {}
    for f in filmes:
        diretor = f["diretor"]
        resultados[diretor] = resultados.get(diretor, 0) + f["bilheteria"]
    return resultados

def campeao(filmes):

    max_bilheteria = max(f["bilheteria"] for f in filmes)
    
    melhor_pontuacao = -1
    filme_campeao = None
    
    for f in filmes:
        media_avaliacoes = sum(f["avaliacoes"]) / len(f["avaliacoes"])
        bilheteria_normalizada = (f["bilheteria"] / max_bilheteria) * 10
        pontuacao_total = bilheteria_normalizada + media_avaliacoes 
        if pontuacao_total > melhor_pontuacao:
            melhor_pontuacao = pontuacao_total
            filme_campeao = f
    return filme_campeao

print("Top 3 maiores bilheterias:")
for f in top_bilheteria(filmes):
    print(f"{f['titulo']} - ${f['bilheteria']}M")

print("Top 3 melhores avaliados:")
for f in top_avaliacao(filmes):
    media = sum(f["avaliacoes"]) / len(f["avaliacoes"])
    print(f"{f['titulo']} - Média: {media:.2f}")

print("Bilheteria por diretor:")
for diretor, total in bilheteria_por_diretor(filmes).items():
    print(f"{diretor} - ${total}M")

print("Campeão absoluto:")
campeao_filme = campeao(filmes)
media = sum(campeao_filme["avaliacoes"]) / len(campeao_filme["avaliacoes"])
print(f"{campeao_filme['titulo']} - Bilheteria: ${campeao_filme['bilheteria']}M, Média avaliações: {media:.2f}")