# Em uma determinada loja de eletrodomésticos, os produtos podem ser adquiridos optando-se por uma das seguintes formas
# de pagamento:
# Opção Condição Cálculo
# 1 à vista 8% de desconto
# 2 em 2 parcelas 4% de desconto, dividido em duas vezes iguais
# 3 em 3 parcelas sem desconto, dividido em três vezes iguais
# 4 em 4 parcelas 4% de acréscimo, dividido em quatro vezes iguais
# Elabore um algoritmo que leia a opção do cliente e o preço de tabela do produto, mostrando então o valor calculado
# conforme a condição escolhida.

print(" ================ Loja socialista ==================")
print("1 - à vista 8% de desconto ")
print("2 - 2 parcelas 4% de desconto, dividido em duas vezes iguais ")
print("3 - 3 parcelas sem desconto, dividido em três vezes iguais ")
print("4 - 4 parcelas 4% de acréscimo, dividido em quatro vezes iguais ")


while True:
    option = int(input("Opção: "))
    if option < 1 or option > 4:
        print("Selecione uma opção válida")
        continue
    else:
        break

price = float(input("Preço de tabela: "))

match option:
    case 1:
        dif = (price * 0.08) * (-1)
        final_price = price + dif
        print(f"Preço final: R${final_price: .2f}")
    case 2:
        dif = (price * 0.04) * (-1)
        final_price = (price + dif) / 2
        print(f"Preço final: 2x R${final_price: .2f}")
    case 3:
        final_price = price / 3
        print(f"Preço final: 3x R${final_price: .2f}")
    case 4:
        dif = (price * 0.04)
        final_price = (price + dif) / 4
        print(f"Preço final: 4x R${final_price: .2f}")

    case _:
        print("Erro desconhecido. Reinicie o programa")
