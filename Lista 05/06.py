# Escreva um algoritmo que leia três números inteiros A, B e C e mostre-os em ordem crescente. Emprega apenas
# comparações e seleção encadeada (não usar o sort do Python e não usar listas).

A = int(input("Inteiro para A: "))
B = int(input("Inteiro para B: "))
C = int(input("Inteiro para C: "))

maior = 0
medio = 0
menor = 0

if A > B:
    maior = A
    if C > maior:
        maior = C
        medio = A
        menor = C
    else:
        medio = B
        menor = C
else:
    maior = B
    if C > maior:
        maior = C
        medio = B
        menor = A
    elif C > A:
        medio = C
        menor = A
    else:
        medio = A
        menor = C

print(f"Maior: {maior} - Medio: {medio} - Menor: {menor}")