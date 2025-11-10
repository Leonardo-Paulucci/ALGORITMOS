a, b, c, d = map(int, input("Digite quatro valores inteiros, separados por espaço: ").split())

def forma_triangulo(x, y, z):
    return (x + y > z) and (x + z > y) and (y + z > x)

comb1 = forma_triangulo(a, b, c)
comb2 = forma_triangulo(a, b, d)
comb3 = forma_triangulo(a, c, d)
comb4 = forma_triangulo(b, c, d)

if comb1 or comb2 or comb3 or comb4:
    print("S")
else:
    print("N")
