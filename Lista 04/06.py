# A partir das informações contidas na tabela abaixo, elabore um algoritmo que leia a massa em kg de um boxeador e mostre
# a qual categoria ele pertence. Caso ele não se encaixe, informe “Categoria inferior a Super-médio”.
# Lembrando que 1 quilograma = 2,20462262 libras

# Massa Categoria
# 201 lb ou mais Peso-pesado
# 176 até 200 lb Cruzador
# 169 até 175 lb Meio-pesado
# 161 até 168 lb Super-médio

print(" ================ Categoria no boxe ==================")

massa = float(input("Peso (kg): "))

peso = massa * 2.20462262

if peso >= 201:
    print("Peso-pesado")
elif peso < 201 and peso >= 176:
    print("Cruzador")
elif peso < 175 and peso >= 169:
    print("Meio-pesado")
elif peso < 168 and peso >= 161:
    print("Super-médio")
else:
    print("Categoria inferior a Super-médio")