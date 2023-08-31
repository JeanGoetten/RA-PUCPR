# [13] O valor de π pode ser calculado usando como base a seguinte série:
# S = 1 - 1/3**3 + 1/5**3 - 1/7**3 + 1/9**3 - ... +-?
# Sendo,
# pi = (S x 32)**(1/3)
# Elabore um algoritmo que calcule e mostre o valor de π com base em uma série S de 50 termos.
import math
print("============== while loop ================")
T = 1
t = 50
S = 1
selector = True
index = 1

while T <= t*2:
    if T%2 != 0:
        if selector:
            S -= 1/(T + 2)**3
            selector = False
            index += 1
        else:
            S += 1/(T + 2)**3
            selector = True
            index += 1
    else:
        pass

    T += 1

pi = (S * 32)**(1/3)
print(f"Série {t} de Pi: {pi}")

dif = ((pi/math.pi) - 1)*100
print(f"Força da borboleta: {dif: .20f}%")
# primeiro_porcento = 0
# iteration = 1
# while primeiro_porcento < 1:
#     primeiro_porcento = dif * 10
#     iteration = iteration * 10
#
# print(f"{primeiro_porcento}% de desvio em {iteration} iterações")

print("============== for loop ================")
S = 1
t = 1000
selector = True

for i in range(1, t*2):
    if i % 2 != 0:
        if selector:
            S -= 1 / (i + 2) ** 3
            selector = False
        else:
            S += 1 / (i + 2) ** 3
            selector = True
    else:
        pass


pi = (S * 32) ** (1 / 3)
print(f"Série {t} de Pi: {pi}")

dif = ((pi / math.pi) - 1) * 100
print(f"Força da borboleta: {dif: .30f}%")
# primeiro_porcento = 0
# iteration = 1
#
# while primeiro_porcento < 1:
#     primeiro_porcento = dif * 10
#     iteration = iteration * 10
#
# print(f"{primeiro_porcento}% de desvio em {iteration} iterações")
