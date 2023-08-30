# [4] Imprima os números múltiplos de 4 existentes no intervalo aberto ]1, 100[

print("================ While ================")
n = 1
while n < 100:
    if n%4 == 0:
        print(n)
    n = n + 1


print("")
print("================ For ================")
for i in range(4, 100, 4):
    print(i)