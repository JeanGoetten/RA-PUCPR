# calcular a quantidade de latas de tinta necessárias e o custo para pintar tanques cilíndricos
# a partir de sua  altura e raio
# dado que: lata de tinta custa $ 50.00
#           lata contém 5 litros
#           1 litro de tinta pinta 3m^2

# dados de entrada: altura e raio
# dados de saída: custo em R$ e quantidade de latas
# Dado que: 2π r h + 2π r²

import math
print("============== Calculadora de Pintor ==============")

# Variáveis
h = float(input("Insira a altura do tanque: "))
r = float(input("Insira o raio do tanque: "))

lata_price = 50.00 # $
lata_size = 5 # litros
tinta_rendimento_por_litro = 3 # m²

# Funções
def superficie_cilindro(h, r):
    area_superficie = (2 * math.pi * r * h) + (2 * math.pi * (r**2))
    return area_superficie


def quantidade_de_latas():
    rendimento_por_lata = lata_size * tinta_rendimento_por_litro
    qtd_latas = superficie_cilindro(h, r)/rendimento_por_lata
    return qtd_latas


def custo():
    custo = quantidade_de_latas() * lata_price
    return custo

def custo_arredondado_lata_inteira():
    custo = math.ceil(quantidade_de_latas()) * lata_price
    return custo

# Saídas
print(f"O custo para pintar um tanque de{superficie_cilindro(h, r): .1f}m² é de ${custo(): .2f} com{quantidade_de_latas(): .1f} latas de tinta (5L)")
print(f"O custo para pintar um tanque de{superficie_cilindro(h, r): .1f}m² é de ${custo_arredondado_lata_inteira(): .2f} com {math.ceil(quantidade_de_latas())} latas de tinta (5L)")