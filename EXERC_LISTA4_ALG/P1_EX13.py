def buscar_por_preco(produtos, preco_procurado):
    resultados = []
    for produto in produtos:
        if produto["preco"] == preco_procurado:
            resultados.append(produto)
    return resultados

def main():

    produtos = [
        {"nome": "Arroz", "preco": 5.50},
        {"nome": "Feijão", "preco": 7.20},
        {"nome": "Macarrão", "preco": 4.00},
        {"nome": "Açúcar", "preco": 5.50},
        {"nome": "Óleo", "preco": 6.80},
        {"nome": "Sal", "preco": 3.20},
        {"nome": "Café", "preco": 7.20},
    ]

    print("Busca de produtos por preço.")
    while True:
        entrada = input("Digite o preço para buscar (ou ENTER para sair): ")
        if entrada == "":
            print("Saindo do programa.")
            break

        try:
            preco_busca = float(entrada)
        except ValueError:
            print("Entrada inválida! Digite um número válido.")
            continue

        encontrados = buscar_por_preco(produtos, preco_busca)
        if encontrados:
            print(f"Produtos com preço R$ {preco_busca:.2f}:")
            for p in encontrados:
                print(f" - {p['nome']}")
        else:
            print("Nenhum produto encontrado com esse preço.")

if __name__ == "__main__":
    main()