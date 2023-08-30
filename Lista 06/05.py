# [5] Imprima os números ímpares de 1 até n, sendo n fornecido pelo usuário. Intervalo fechado [1, n]

n = int(input("Insira um valor final (inteiro): "))
print("================ While ================")
m = 1
while m <= n:
    if m%2 > 0:
        print(m)
    m = m + 1


print("")
print("================ For ================")
for i in range(1, n, 2):
    print(i)