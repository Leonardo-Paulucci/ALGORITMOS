#4. Busca LinearDada uma lista de nomes, implemente uma função que busque um nome digitado pelo usuário. Informe a posição em que ele aparece ou diga que não foi encontrado.

def buscar_nome(lista, nome_procurado):
    for i in range(len(lista)):
        if lista[i] == nome_procurado:
            return i + 1
    return -1 

nomes = ["Leonardo", "Larissa", "Maria", "Pedro", "Carlos", "Vanessa"]

nome = input("Digite um nome para buscar: ")

posicao = buscar_nome(nomes, nome)

if posicao != -1:
    print(f"O nome '{nome}' foi encontrado na posição {posicao}.")
else:
    print(f"O nome '{nome}' não foi encontrado na lista.")