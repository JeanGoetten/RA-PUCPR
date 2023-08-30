# [11] Imprima uma PA na qual são fornecidos o primeiro termo (a1), a razão (r) e a quantidade de termos (n)
# desejada.
# Lembrete: an = a1 + (n -1) × r

a1 = int(input("Primeiro termo: "))
r = int(input("Razão: "))
n = int(input("Quantidade de termos: "))
wa1 = a1
w_soma_dos_termos = 0
soma_dos_termos = 0
i = 1
index = 1
print("============== while loop ================")
while True:
    if i == 1:
        progress = wa1
        print(f"Índice {i}: {progress}")
        w_soma_dos_termos = wa1
        i = i + 1
    elif 1 < i <= n:
        progress = wa1 + r
        print(f"Índice {i}: {progress}")
        w_soma_dos_termos = w_soma_dos_termos + progress
        wa1 =  wa1 + r
        i = i + 1
    else:
        break

print(f"Soma dos termos da PA: {w_soma_dos_termos}")

print("")
print("================ for loop ================")
for i in range(a1, n + a1):
    if index == 1:
        progress = a1
        print(f"Índice {index}: {progress}")
        soma_dos_termos = a1
        index = index + 1
    else:
        progress = a1 + r
        print(f"Índice {index}: {progress}")
        soma_dos_termos = soma_dos_termos + progress
        a1 = a1 + r
        index = index + 1

print(f"Soma dos termos da PA: {soma_dos_termos}")