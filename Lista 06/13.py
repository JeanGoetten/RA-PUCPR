# [13] O n-ésimo número harmônico é dado pelo seguinte somatório:
# Escreva um algoritmo para calcular o valor do número harmônico H dado que o número n será fornecido pelo
# usuário. Exemplo, se o usuário digitar 5, calcular H = 1 + 1/2 + 1/3 + 1/4 + 1/5
# (Para maiores informações sobre o número harmônico http://en.wikipedia.org/wiki/Harmonic_number)

print("============== while loop ================")
n = int(input("Tamanho da harmonia: "))
VH = 0
F = 0
index = 1
while True:
    if index == 1:
        VH = 1
    elif 1 < index <= n:
        F = F + (1 / index)
        VH = 1 + F
    else:
        break
    index = index + 1

print(f"Valor harmônico: {VH}")

print("")
print("================ for loop ================")
H = 0
VH = 0
F = 0
for i in range(1, n + 1):
    if i == 1:
        VH = 1
    else:
        F = F + (1 / i)
        VH = 1 + F


print(f"Valor harmônico: {VH}")