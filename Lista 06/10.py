# [10] Imprima os números múltiplos de 3 entre li (limite inicial) e lf (limite final). Os valores inteiros de li e lf devem
# ser informados pelo usuário e não pertencem ao intervalo, ou seja, intervalo aberto: ]li, lf[

print("============== while loop ================")
li = int(input("Valor inicial: "))
lf = int(input("Valor final: "))
wli = li + 1
while wli < lf:
    if wli%3 == 0:
        print(wli)
    wli = wli + 1

print("")
print("================ for loop ================")
for i in range(li + 1, lf):
    if i % 3 == 0:
        print(i)
    i = i + 1