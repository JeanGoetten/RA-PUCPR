# [14] Elabore um algoritmo que calcule o valor da série S abaixo, sendo que o valor inteiro de n é fornecido pelo
# usuário.
#
# S = (1/sqrt(3)) + (2/sqrt(4)) + (3/sqrt(5)) ... (n/sqrt(n + 2))
import math

n = int(input("Tamanho da série: "))
index = 1
R = 0

while index <= n:
    R = R + (index / math.sqrt(index + 2))
    index = index + 1

print(f"Valor da série: {R}")

print("")
print("================ for loop ================")
R = 0
for i in range(1, n + 1):
    R = R + (i / math.sqrt(i + 2))

print(f"Valor da série: {R}")