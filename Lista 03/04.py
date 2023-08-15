# Um produtor de abóboras deve verificar a classificação dos seus produtos para posterior
# empacotamento e venda. Um de seus clientes compra apenas abóboras médias (aquelas que possuem
# o diâmetro (d) no intervalo 15 cm ≤ d < 20 cm). Elabore um algoritmo que leia o diâmetro de uma
# abóbora e mostre se ela é do tipo média ou não. Caso ela não se encaixe na classificação, informe
# “produto fora das medidas”.

print(" ================ Classificador de Abóboras ==================")

d = float(input("Insira o diâmetro da sua abóbora: "))

def classificador_de_abobora(d):
    if d >= 15 and d <= 20:
        print("Sua abóbora é do tipo média!")
    else:
        print("Produto fora das medidas!")


classificador_de_abobora(d)