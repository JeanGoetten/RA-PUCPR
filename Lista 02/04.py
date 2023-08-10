# O IMC, índice de massa corporal, é calculado através da seguinte fórmula:
# IMC = massa / altura 2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e mostre o valor do IMC.

print("============== Calculadora IMC ==============")

altura = float(input("Insira a altura (ex.: 1.90): "))
massa = float(input("Insira o peso (ex.: 80): "))

def imc(altura, massa):
    imc = massa/altura**2
    return imc


print(f"IMC: {imc(altura, massa): .2f}")