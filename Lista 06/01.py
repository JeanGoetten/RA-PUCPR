# [1] Imprima os números de 1 até 99, com incremento de 2.
# Exemplo: 1, 3, 5.....97, 99

print("============== while loop ================")
n = 1
while n < 100:
    print(n)
    n = n +2

print("")
print("================ for loop ================")
for i in range(0, 100):
    if i%2 > 0:
        print(i)