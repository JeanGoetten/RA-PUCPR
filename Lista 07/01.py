# [1] Anacleto tem 1,50 metro e cresce 2 centímetros por ano, enquanto Felisberto tem 1,10 metro e cresce 3 centímetros
# por ano. Construa um algoritmo que calcule e mostre quantos anos serão necessários para que Felisberto seja maior
# que Anacleto.

import numpy as np

print("============== while loop ================")
felisberto = 1.1
analecto = 1.5
w_anos = 0
anos = 0

while felisberto <= analecto:
    felisberto += 0.03
    analecto += 0.02
    w_anos += 1


print(f"Ano: {w_anos}")

print("============== for loop ================")
analecto = 1.5
felisberto = 1.1


def dynamic_range(felis, anal, ano):
    felis += 0.03
    anal += 0.02
    ano += 1
    anos = 1
    print(f"{ano}")
    if felis <= anal:  # Modify the condition based on your requirement
        dynamic_range(felis, anal, ano)  # Recursively call with an incremented stop value



dynamic_range(felisberto, analecto, anos)  # Initial stop value
# print(f"Ano: {anos}")