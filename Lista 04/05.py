# Dados três valores A, B e C, verificar se eles podem ser os comprimentos dos lados de um triângulo empregando a regra
# que cada um deve ser menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas
# medidas (ou seja, | B − C | < A < B + C). Caso as medidas fornecidas possam formar um triângulo, verificar se elas compõem
# um triângulo equilátero, isósceles ou escaleno. Informar se elas não compuserem um triângulo.

print(" ================ △? ==================")

A = float(input("A: "))
B = float(input("B: "))
C = float(input("C: "))

def verificar_lados(a, b, c):
    abs_BC = abs(b - c)
    BC = b + c
    if a > abs_BC and a < BC:
        checked = True
    else:
        checked = False
    return checked


if verificar_lados(A, B, C):
    #equilatero
    if A == B and A == C and B == C:
        print("△ equilátero")
    #escaleno
    elif A != B and A != C and B != C:
        print("△ escaleno")
    #isosceles
    else:
        print("△ isosceles")

else:
    print("!△")