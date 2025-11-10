nomes = []
n = int(input("Quantos nomes você quer adicionar na lista? "))
for i in range(n):
    nome = input(f"Digite o nome {i+1}: ")
    nomes.append(nome)

alvo = input("Digite o nome que deseja buscar: ")

def busca_linear(lista, alvo):
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

indice = busca_linear(nomes, alvo)
if indice != -1:
    print(f"{alvo} encontrado no índice {indice}")
else:
    print(f"{alvo} não encontrado")