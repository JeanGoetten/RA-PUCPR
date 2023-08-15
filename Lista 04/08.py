# Escreva um algoritmo que leia três números inteiros A, B e C e mostre o valor do maior deles.
# Construa o algoritmo usando uma seleção encadeada.

print(" ================ A B C ^? ==================")

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A > B:
    maior = A
elif C > A:
    maior = C
else:
    maior = B

print(maior)