# Considerando que a conversão de grau Celsius (°C) para grau Farenheit (°F) é dada pela seguinte fórmula:
# °F = (9 /5 ) °C + 32
# Elabore um algoritmo que leia uma temperatura em Celsius e mostre seu valor em Farenheit.

print("============== Conversor Celsius para Farenheit ==============")

celsius = float(input("Insira a temperatura em Celsius: "))

def celsius_to_farenheit(celsius):
    F = ((9 / 5) * celsius) + 32
    return F


print(f"{celsius_to_farenheit(celsius)} F")