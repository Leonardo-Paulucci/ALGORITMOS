def busca_por_nome(pessoas, nome_procurado):
    for i, pessoa in enumerate(pessoas):
        if pessoa.get("nome") == nome_procurado:
            return pessoa
    return None 

lista_pessoas = [
    {"nome": "Ana", "idade": 25},
    {"nome": "Carlos", "idade": 30},
    {"nome": "João", "idade": 22},
    {"nome": "Maria", "idade": 28}
]

resultado = busca_por_nome(lista_pessoas, "João")
if resultado:
    print("Pessoa encontrada:", resultado)
else:
    print("Pessoa não encontrada.")