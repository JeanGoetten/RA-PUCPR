# ler diâmetro e calcular área

import math

diameter = float(input("Insira o diâmetro: "))

def circle_area(a):
    area = math.pi * (a/2)**2
    return area


print(f"A área do seu círculo é {circle_area(diameter): .2f}")