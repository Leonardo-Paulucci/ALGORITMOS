def busca_sequencial(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i 
    return -1

lista = [3, 7, 1, 9, 5]
alvo = 9
print(busca_sequencial(lista, alvo))