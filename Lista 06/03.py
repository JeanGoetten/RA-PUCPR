# [3] Imprima os números de -100 até 100, com incremento de 10.
# Exemplo: -100, -90, -80.....90, 100

print("================ While ================")
n = -100
while n <= 100:
    print(n)
    n = n + 10



print("")
print("================ For ================")
for i in range(-100, 101, 10):
    print(i)