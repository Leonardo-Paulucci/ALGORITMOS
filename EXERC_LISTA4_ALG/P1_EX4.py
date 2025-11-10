def menor_numero(lista):
    menor = lista[0]
    for valor in lista:
        if valor < menor:
            menor = valor
    return menor

print(menor_numero([4, 7, 1, 9, 2]))