import random
import time

lista = [random.randint(0, 1000000) for _ in range(1000000)]
alvo = random.choice(lista)

def busca_linear(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

def busca_binaria(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return -1

inicio = time.time()
busca_linear(lista, alvo)
fim = time.time()
print("Tempo busca linear:", fim - inicio, "s")

lista.sort()

inicio = time.time()
busca_binaria(lista, alvo)
fim = time.time()
print("Tempo busca binária:", fim - inicio, "s")