def contar_ocorrencias(lista, alvo):
    contador = 0
    for valor in lista:
        if valor == alvo:
            contador += 1
    return contador

lista = [1, 2, 2, 3, 2]
print(contar_ocorrencias(lista, 2))