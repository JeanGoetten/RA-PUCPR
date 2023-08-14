# Um caixa automático possui as seguintes cédulas disponíveis: 50, 20, 10, 5, 2 e 1. Faça um algoritmo que
# leia o valor de um saque e mostre a quantidade de bilhetes de cada nota necessários para comporem o valor
# solicitado pelo usuário.

import math
print("============== Caixa automático ==============")

valor_saque = int(input("Valor a sacar (apenas valores inteiros): "))


cedulas_50 = valor_saque/50
cedulas_20 = valor_saque/20
cedulas_10 = valor_saque/10
cedulas_5 = valor_saque/5
cedulas_2 = valor_saque/2
cedulas_1 = valor_saque/1

print(f"Cédulas de 50: {cedulas_50}")
print(f"Cédulas de 20: {cedulas_20}")
print(f"Cédulas de 10: {cedulas_10}")
print(f"Cédulas de 5: {cedulas_5}")
print(f"Cédulas de 2: {cedulas_2}")
print(f"Cédulas de 1: {cedulas_1}")