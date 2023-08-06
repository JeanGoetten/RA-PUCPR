# ler valor dos 2 catetos e calcular a hipotenusa

import math

print("============== Arquitetura Egípcia Simulator ==============")

cateto_oposto = float(input("Insira o valor do cateto oposto: "))
cateto_adjacente = float(input("Insira o valor do cateto adjacente: "))

def teorema_de_pitagoras(a, b):
    hipotenusa = math.sqrt((a ** 2) + (b ** 2))
    return hipotenusa


print(f"O valor da hipotenusa para esse triângulo é{teorema_de_pitagoras(cateto_oposto, cateto_adjacente): .2f}")