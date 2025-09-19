vendas_por_dia = {
    1: 5,
    2: 8,
    3: 3,
    4: 10,
    5: 7,
    6: 12,
    7: 6,
    8: 4,
    9: 9,
    10: 11,
    11: 3,
    12: 8,
    13: 7,
    14: 5,
    15: 6,
    16: 9,
    17: 4,
    18: 10,
    19: 6,
    20: 8,
    21: 7,
    22: 5,
    23: 9,
    24: 10,
    25: 11,
    26: 4,
    27: 6,
    28: 8,
    29: 7,
    30: 5
}

total_vendas = sum(vendas_por_dia.values())
print("Total de vendas no mês:", total_vendas)

dia_mais_vendas = max(vendas_por_dia, key=vendas_por_dia.get)
dia_menos_vendas = min(vendas_por_dia, key=vendas_por_dia.get)
print("Dia com mais vendas:", dia_mais_vendas, "(", vendas_por_dia[dia_mais_vendas], "vendas )")
print("Dia com menos vendas:", dia_menos_vendas, "(", vendas_por_dia[dia_menos_vendas], "vendas )")

media_vendas = total_vendas / len(vendas_por_dia)
print("Média de vendas por dia:", round(media_vendas, 2))

dias_acima_media = [dia for dia, vendas in vendas_por_dia.items() if vendas > media_vendas]
print("Dias com vendas acima da média:", dias_acima_media)