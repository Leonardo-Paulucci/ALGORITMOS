A = int(input("Digite o primeiro valor: "))
B = int(input("Digite o segundo valor: "))
C = int(input("Digite o terceiro valor: "))

if A >= B and A >= C:
    print(A)
elif B >= A and B >= C:
    print(B)
else:
    print(C)