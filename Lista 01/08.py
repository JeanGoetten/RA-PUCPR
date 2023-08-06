# ler a razão (r) de uma PA e seu primeiro termo
# calcular o 15º termo
# dado que: an = a1 + (n-1) * r


print("============== Calculadora PA ==============")

r = int(input("Insira o valor de r: "))
a1 = int(input("Insira o valor do primeiro termo: "))


def calculadora_PA(r, a1):
    a15 = a1 + (15 - 1)*r
    return a15


print(calculadora_PA(r, a1))