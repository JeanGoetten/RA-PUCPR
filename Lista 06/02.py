# [2] Imprima os números de 50 até 0 com decremento de 5.
# Exemplo: 50, 45, 40.....5, 0

print("================ While ================")
n = 50
while n >= 0:
    print(n)
    n = n -5



print("")
print("================ For ================")
for i in range(50, -1, -5):
    print(i)