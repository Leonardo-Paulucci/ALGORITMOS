notas = []

qtd = int(input("Quantos alunos existem na turma? "))

for i in range(qtd):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    notas.append(nota)

media = sum(notas) / qtd

maior = max(notas)
menor = min(notas)

acima_media = sum(1 for nota in notas if nota > media)
percentual = (acima_media / qtd) * 100

print(f"A média da turma é de {media:.2f}")
print(f"A maior nota da turma é de {maior}")
print(f"A menor nota da turma é de {menor}")
print(f"O percentual de alunos da turma acima da média é de {percentual:.2f}%")