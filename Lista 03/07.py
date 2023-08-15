# O IMC (Índice de Massa Corporal) é calculado através da seguinte fórmula:
# IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e mostre
# o valor do IMC e se ele está na faixa considerada “normal” segundo o critério apresentado na tabela
# da OMS (Organização Mundial de Saúde): 18,5 ≤ IMC < 25. Caso não esteja, calcule sua massa
# máxima considerada normal (usando o IMC igual a 24,9).

print(" ================ IMC 2.0 ==================")

massa = float(input("Qual seu peso (kg): "))
altura = float(input("Qual sua altura (m): "))

def IMC(massa, altura):
    imc = massa/altura**2
    return imc

def imc_normal(massa):
    if IMC(massa, altura) >= 18.5 and IMC(massa, altura) <= 25:
        print("Normal")
    else:
        massa = 24.9 * altura**2
        print(f"Peso ideal para essa altura: {massa: .1f} Kg")


print(f"IMC: {IMC(massa, altura): .1f}")
imc_normal(massa)