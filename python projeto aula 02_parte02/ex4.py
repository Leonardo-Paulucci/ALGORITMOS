vendas = []
dias = int(input("Quantos dias de vendas o mês teve? "))

for i in range(dias):
    qtd = int(input(f"Digite as vendas do dia {i+1}: "))
    vendas.append(qtd)

total = sum(vendas)

mais_vendas = max(vendas)
menos_vendas = min(vendas)
dia_mais = vendas.index(mais_vendas) + 1
dia_menos = vendas.index(menos_vendas) + 1

media = total / len(vendas)

dias_acima = [i+1 for i, v in enumerate(vendas) if v > media]

print("Resultados:")
print("Total de vendas no mês:", total)
print(f"Dia com mais vendas: {dia_mais} ({mais_vendas} vendas)")
print(f"Dia com menos vendas: {dia_menos} ({menos_vendas} vendas)")
print("Média de vendas por dia:", round(media, 2))
print("Dias acima da média:", dias_acima)