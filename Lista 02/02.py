# Elabore um algoritmo para calcular o consumo médio de um automóvel (medido em km/l), solicitando
# como dados de entrada a distância total percorrida (em km) e o volume de combustível consumido para
# percorrê-la (em litros).

print("============== Calculadora de consume médio de combustível ==============")

distancia_total_percorrida = float(input("Insira a distancia total percorrida (km): "))
volume_total_combustivel = float(input("Insira o volume total de combustível (L): "))

def consumo_medio(km, l):
    media = km/l
    return media


print(f"O consumo médio foi de {consumo_medio(distancia_total_percorrida, volume_total_combustivel)}Km/L")