# Escreva um algoritmo para calcular o volume de uma esfera de raio r, sendo que r é um valor fornecido
# pelo usuário, dado que v = ( 4 /3 ) π r3


import math
print("============== Calculadora de volume esférico ==============")

r = float(input("Insira o raio de sua esfera: "))

def volume_esfera(r):
    v = (4/3) * math.pi * r**3
    return v


print(f"O volume da esfera com raio {r} é{volume_esfera(r): .2f}")