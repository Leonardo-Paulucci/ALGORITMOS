livros_emprestados = {
    "O Pequeno Príncipe": ["Ana", 5],
    "Senhor dos Anéis": ["João", 10],
    "Harry Potter": ["Maria", 8]
}

livros_mais_7_dias = [titulo for titulo, info in livros_emprestados.items() if info[1] > 7]
print("Livros emprestados há mais de 7 dias:", livros_mais_7_dias)

livro_mais_tempo = max(livros_emprestados, key=lambda titulo: livros_emprestados[titulo][1])
print("Livro emprestado há mais tempo:", livro_mais_tempo, "(", livros_emprestados[livro_mais_tempo][1], "dias )")

usuarios_com_livros = [info[0] for info in livros_emprestados.values()]
print("Usuários com livros emprestados:", usuarios_com_livros)

media_dias = sum(info[1] for info in livros_emprestados.values()) / len(livros_emprestados)
print("Média de dias de empréstimo:", round(media_dias, 2))