def maior_numero(lista):
    maior = lista[0]
    for valor in lista:
        if valor > maior:
            maior = valor
    return maior

print(maior_numero([4, 7, 1, 9, 2]))