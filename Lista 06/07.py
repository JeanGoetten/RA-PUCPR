# [7] Faça um algoritmo que mostre o resultado da função de Babbage f(x) = x2 + x + 41 (polinômio que gera apenas
# números primos), variando x de 0 até 20.

print("================ While ================")
x = 0
while x <= 20:
    fbb = x**2 + x + 41
    print(fbb)
    x = x + 1


print("")
print("================ For ================")
for i in range(0, 21, 1):
    fbb = i ** 2 + i + 41
    print(fbb)