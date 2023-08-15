# O IMC, Índice de Massa Corporal, é calculado através da seguinte fórmula:
# IMC = massa / altura2
# Elabore um algoritmo que leia a massa (em quilogramas) e a altura (em metros) do usuário e mostre o valor do IMC e qual sua condição
# segundo o critério apresentado na tabela da OMS (Organização Mundial de Saúde):
# Condição IMC em adultos
# abaixo do peso abaixo de 18,5
# no peso normal entre 18,5 e 25
# acima do peso entre 25 e 30
# Obeso acima de 30

print(" ================ IMC 3.0 ==================")

massa = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

def IMC(massa, altura):
    imc = massa / altura**2
    return imc


if IMC(massa, altura) < 18.5:
    print(f"Abaixo do peso. IMC: {IMC(massa, altura): .1f}")
if IMC(massa, altura) >= 18.5 and IMC(massa, altura) <= 25:
    print(f"Normal. IMC: {IMC(massa, altura): .1f}")
if IMC(massa, altura) > 25 and IMC(massa, altura) <= 30:
    print(f"Acima do peso. IMC: {IMC(massa, altura): .1f}")
if IMC(massa, altura) > 30:
    print(f"Obeso. IMC: {IMC(massa, altura): .1f}")
