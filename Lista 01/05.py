# ler preço de catálogo de um produto e então mostrar os
# valores com 5% de acréscimo em 3 parcelas
# preço de tabela em 2 parcelas
# preço à vista com 5% de desconto

print("============== No caixa da loja ==============")

price = input("Insira o preço do produto: ")
price_number = float(price)

def tres_parcelas_com_juros(a):
    tot_com_juros = a + (a * 0.05)
    valor_parcela = tot_com_juros/3
    return valor_parcela


def duas_parcelas_sem_juros(a):
    valor_parcela = a/2
    return valor_parcela


def a_vista_com_desconto(a):
    valor_com_desconto = a - (a * 0.05)
    return valor_com_desconto

price_3x_com_juros = tres_parcelas_com_juros(price_number)
price_2x_sem_juros = duas_parcelas_sem_juros(price_number)
price_a_vista_com_desconto = a_vista_com_desconto(price_number)

print(f"O Valor da parcela em 3 vezes com 5% de acréscimo é de R${price_3x_com_juros: .2f}")
print(f"O valor da parcela em 2 vezes sem juros é de R${price_2x_sem_juros: .2f}")
print(f"O valor à vista com 5% de desconto é de R${price_a_vista_com_desconto: .2f}")