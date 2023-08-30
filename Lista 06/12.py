# [12] Considerando que a conversão de graus Celsius (°C) para graus Fahrenheit (°F) é dada pela seguinte fórmula:
# °F = °C × 1,8 + 32
# Elabore um algoritmo que leia uma temperatura (T) em graus Celsius e mostre as conversões para
# graus Fahrenheit em uma escala que vai de T-10 até T+10, de 1 em 1 grau.

print("============== while loop ================")
T = float(input("Temperatura em Celsius: "))
Fmin = -10
F = T * 1.8 + 32
F = int(F)
Fmin = F - 10
Fmax = F + 10
while True:
    # START FIRULA
    if Fmin < F and Fmin >= F - 5:
        color = '\033[96m'              # ciano
    elif Fmin < F - 5:
        color = '\033[94m'              # azul
    elif Fmin > F and Fmin <= F + 5:
        color = '\033[93m'              # amarelo
    elif Fmin > F + 5:
        color = '\033[91m'              # vermelho
    else:
        color = '\033[92m'              # verde
    # END FIRULA

    if Fmin <= Fmax and Fmin != F:
        print(f"{color}{Fmin} °F \033[0m")
    elif Fmin == F:
        print(f"{color}{F} °F <= \033[0m")
    else:
        break
    Fmin = Fmin + 1

print("")
print("================ for loop ================")
Fmin = F - 10
for i in range(int(Fmin), int(Fmax) + 1, 1):
    # START FIRULA
    if F > i >= F - 5:
        color = '\033[96m'  # ciano
    elif i < F - 5:
        color = '\033[94m'  # azul
    elif F < i <= F + 5:
        color = '\033[93m'  # amarelo
    elif i > F + 5:
        color = '\033[91m'  # vermelho
    else:
        color = '\033[92m'  # verde
    # END FIRULA

    if i <= Fmax and i != F:
        print(f"{color}{i} °F \033[0m")
    else:
        print(f"{color}{F} °F <= \033[0m")