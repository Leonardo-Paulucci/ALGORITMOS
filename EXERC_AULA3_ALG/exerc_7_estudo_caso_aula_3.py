produto1 = {"nome": "Arroz", "preco": 25.90, "estoque": 100}
produto2 = {"nome": "Feijão", "preco": 12.50, "estoque": 50}
produto3 = {"nome": "Macarrão", "preco": 8.30, "estoque": 80}

produtos = [produto1, produto2, produto3]

for produto in produtos:
    print(f"O produto {produto['nome']} custa R${produto['preco']} e tem {produto['estoque']} unidades em estoque.")