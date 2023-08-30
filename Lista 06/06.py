# [6] Imprima uma tabela de conversão de polegadas para centímetros, cuja escala vai de 1 a 20 polegadas.
# A conversão entre estas duas unidades é dada por:

# polegada = centímetro × 2,54

print("================ While ================")
m = 1
while m <= 20:
    pol = m * 2.54
    print(pol)
    m = m + 1


print("")
print("================ For ================")
for i in range(1, 21, 1):
    print(i * 2.54)