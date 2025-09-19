pedidos = [
    {
        "cliente": "Ana",
        "itens": [
            {"prato": "Pizza", "preco": 35.0},
            {"prato": "Suco", "preco": 8.0}
        ]
    },
    {
        "cliente": "Bruno",
        "itens": [
            {"prato": "Hamburguer", "preco": 25.0},
            {"prato": "Suco", "preco": 8.0},
            {"prato": "Pizza", "preco": 35.0}
        ]
    },
    {
        "cliente": "Carla",
        "itens": [
            {"prato": "Pizza", "preco": 35.0},
            {"prato": "Sorvete", "preco": 6.0}
        ]
    }
]

def total_gasto(pedidos, cliente_nome):
    total = 0
    for pedido in pedidos:
        if pedido["cliente"] == cliente_nome:
            for item in pedido["itens"]:
                total += item["preco"]
    return total

def prato_mais_vendido(pedidos):
    contagem = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            contagem[prato] = contagem.get(prato, 0) + 1

    mais_vendido = max(contagem, key=contagem.get)
    return mais_vendido, contagem[mais_vendido]

def ranking_clientes(pedidos):
    gastos = {}
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = sum(item["preco"] for item in pedido["itens"])
        gastos[cliente] = gastos.get(cliente, 0) + total
    
    ranking = sorted(gastos.items(), key=lambda x: x[1], reverse=True)
    return ranking[:3]

print("Total gasto por Ana:", total_gasto(pedidos, "Ana"))
print("Total gasto por Bruno:", total_gasto(pedidos, "Bruno"))
print("Total gasto por Carla:", total_gasto(pedidos, "Carla"))

prato, qtd = prato_mais_vendido(pedidos)
print("Prato mais vendido:", prato, f"({qtd} vezes)")

print("Ranking dos 3 clientes que mais gastaram:")
for pos, (cliente, valor) in enumerate(ranking_clientes(pedidos), start=1):
    print(f"{pos}º {cliente} - R$ {valor:.2f}")