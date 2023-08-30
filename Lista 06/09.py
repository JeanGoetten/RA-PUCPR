# [9] Elabore um algoritmo que leia um conjunto de 10 números inteiros. Mostre então qual o valor da soma e da
# média aritmética do conjunto.

print("============== while loop ================")
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
i = 0
soma = 0
while i <= len(n) - 1:
    soma = soma + n[i]
    i = i + 1


print(f"Soma: {soma}")
print(f"MA: {soma / len(n)}")

print("")
print("================ for loop ================")
sum = 0
for i in range(n[0] - 1, n[len(n) - 1], 1):
    sum = sum + n[i]

print(f"Soma: {sum}")
print(f"MA: {sum / len(n)}")