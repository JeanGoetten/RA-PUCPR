# Uma empresa de câmbio permite a compra de dólares, libras e euros. Elabore um algoritmo que leia o código da moeda
# que o cliente quer comprar e qual o montante que ele deseja adquirir nessa moeda. Mostre então quanto ele deverá pagar
# em reais para concretizar a operação de compra. Além da cotação, a empresa cobra uma comissão de 5% (quando o valor
# for menor que R$ 2.000), ou de 3% (quando maior ou igual a R$ 2.000).
# Opção           Moeda           Cotação
# 1               Dólar           1 dólar dos EUA = 5,09 reais
# 2               Libra           1 libra esterlina = 6,03 reais
# 3               Euro            1 euro = 5,10 reais

print("============================== Cambio monetario =================================")

print("OPCAO ______________________________ MOEDA ______________________________ COTACAO")
print("- 1 ............................. Dolar (USD) ........................ 1 dólar dos EUA = 5,09 reais")
print("- 2 ............................. Libra (GBP) ........................ 1 libra esterlina = 6,03 reais")
print("- 3 ............................. Euro (EUR)  ........................ 1 euro = 5,10 reais")

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

amount = float(input("Valor na moeda selecionada (ex.: 89.75): "))

def custo_para_dolar(amount):
    dolar = 5.09
    custo = (amount * dolar) + taxes(amount)
    return custo


def custo_para_libra(amount):
    libra = 6.03
    custo = (amount * libra) + taxes(amount)
    return custo


def custo_para_euro(amount):
    euro = 5.1
    custo = (amount * euro) + taxes(amount)
    return custo


def taxes(amount):
    taxes = 0
    if amount < 2000:
        taxes = amount * (5 / 100)
    if amount >= 2000:
        taxes = amount * (3 / 100)

    return taxes

if cod == 1:
    print(f"{amount: .2f} USD: {custo_para_dolar(amount): .2f} BRL")
elif cod == 2:
    print(f"{amount: .2f} GBP: {custo_para_libra(amount): .2f} BRL")
else:
    print(f"{amount: .2f} EUR: {custo_para_euro(amount): .2f} BRL")