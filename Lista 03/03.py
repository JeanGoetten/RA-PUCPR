# Elabore um algoritmo que leia um número inteiro e mostre sua raiz quadrada (informe “Valor
# inválido” para números negativos).

print(" ================ Raiz quadrada ==================")

import math

number = int(input("Insira um número inteiro: "))
if number < 0:
    print("Valor inválido: número negativo")
else:
    square_root = math.sqrt(number)
    if square_root - math.floor(square_root) == 0:
        print(f"{square_root: .0f}")
    else:
        print(square_root)
