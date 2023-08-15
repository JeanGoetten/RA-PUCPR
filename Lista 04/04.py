# Desenvolva um algoritmo que calcule as raízes de uma equação polinomial de grau dois (equação do segundo grau ou
# equação quadrática) cuja forma geral é ax2 + bx + c (a ≠ 0), levando em consideração a existência de raízes reais
# e empregando a fórmula de Bhaskara (use o valor de Δ para construir a seleção).

print(" ================ Equação do segundo grau ==================")

while True:
    a = float(input("a: "))
    if a == 0:
        print(" O valor de 'a' não pode ser 0")
        continue
    else:
        break

b = float(input("b: "))
c = float(input("c: "))

print(f"Equação: {a}x2 + {b}x + {c}")

delta = (b ** 2) - 4 * a * c

def bhaskara(a, b):
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print(f"x: {x1}, x': {x2}")


if delta < 0:
    print("Sem raizes reais")
else:
    bhaskara(a, b)