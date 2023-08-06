# ler a razão (q) de uma PG e o seu primeiro termo
# calcular o 25º termo
# dado que an = a1 * q^n-1

print("============== Calculadora PG ==============")

q = int(input("Insira o valor da razão (q): "))
a1 = int(input("Insira o valor do primeiro termo: "))


def calculadora_PG(q, a1):
    a25 = a1 * q**(25-1)
    return a25


print(f"O 25º termo dessa PG tem o valor de {calculadora_PG(q, a1)}")