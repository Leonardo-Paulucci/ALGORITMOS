def primeira_ocorrencia(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado = meio
            fim = meio - 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

def ultima_ocorrencia(lista, alvo):
    inicio, fim = 0, len(lista) - 1
    resultado = -1
    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] == alvo:
            resultado = meio
            inicio = meio + 1
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1
    return resultado

def intervalo_indices(lista, alvo):
    inicio = primeira_ocorrencia(lista, alvo)
    if inicio == -1:
        return -1
    fim = ultima_ocorrencia(lista, alvo)
    return (inicio, fim)

lista = [1, 2, 2, 2, 3, 4]
print(intervalo_indices(lista, 2))