# Construa um algoritmo que calcule o valor de uma conta de energia elétrica de uma cidade hipotética
# considerando: leitura do mês anterior (em Kwh) e leitura do mês atual (em Kwh). O valor do kWh é de
# R$ 0,38 e a taxa de taxa de ICMS de 27%.

print("============== Calculadora COPEL ==============")

leitura_mes_anterior = float(input("Insira a leitura do mes anterior (kwh): "))
leitura_mes_atual = float(input("Insira a leitura do mes atual (kwh): "))

dif_mes_atual = leitura_mes_atual - leitura_mes_anterior

valor_fatura_atual = (dif_mes_atual * 0.38)
impostos = (valor_fatura_atual * 27)/100

valor_fatura_atual_com_impostos = valor_fatura_atual + impostos

print(f"Fatura do mes atual com impostos: R${valor_fatura_atual_com_impostos: .2f}")