# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um algoritmo que leia o código da moeda
# que o cliente quer comprar e qual o montante que ele deseja adquirir nessa moeda. Mostre então quanto ele deverá pagar
# em reais para concretizar a operação de compra. Além da cotação, a empresa cobra uma comissão de 5% (quando o valor
# for menor que R$ 2.000), ou de 3% (quando maior ou igual a R$ 2.000).
# Opção           Moeda           Cotação
# 1               Dólar           1 dólar dos EUA = 5,09 reais
# 2               Libra           1 libra esterlina = 6,03 reais
# 3               Euro            1 euro = 5,10 reais

print("======================= Cambio monetario ==========================")

print("OPCAO ______________________ MOEDA ________________________ COTACAO")
print("- 1 ........................ Dolar ........................ 1 dólar dos EUA = 5,09 reais")
print("- 2 ........................ Libra ........................ 1 libra esterlina = 6,03 reais")
print("- 3 ........................ Euro  ........................ 1 euro = 5,10 reais")

print(" ")
print("====== TAXAS ======")
print("<  2.000,00 R$: 5%")
print(">= 2.000,00 R$: 3%")

while True:
    cod = int(input("Insira o codigo: "))
    if cod < 1 or cod > 4:
        print("Código inválido")
        continue
    else:
        break

amount = float(input("Valor na moeda selecionada: "))

def custo_para_dolar(amount):
    dolar = 5.09
    custo = amount * dolar
    return custo
def custo_para_libra(amount):
    libra = 6.03
    custo = amount * libra
    return custo
def custo_para_euro(amount):
    euro = 5.1
    custo = amount * euro
    return custo



