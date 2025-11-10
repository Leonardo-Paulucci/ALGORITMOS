def meu_index(lista, valor):
    for i, v in enumerate(lista):
        if v == valor:
            return i
    return -1

print(meu_index([3, 5, 7, 9], 7))