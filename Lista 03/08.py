# Em um determinado estacionamento a primeira hora custa R$ 10,00, que é o valor mínimo
# praticado. Após uma hora o valor é fracionado, R$ 1,50 a cada 15 minutos. Elabore um algoritmo
# que leia um número inteiro correspondente a quantidade de minutos usados por um determinado
# cliente do estacionamento e mostre a mensagem “Valor mínimo, R$ 10,00” ou “Valor fracionado,
# R$ x”, no qual x será o valor a pagar calculado pelo algoritmo.

print(" ================ Estacionamento Japonês ==================")

tempo = int(input("Tempo de uso (minutos): "))

if tempo/60 <= 1:
    print("Valor mínimo, R$ 10,00")
else:
    valor_fracionado_apos_primeira_hora = (tempo - 60)/15
    valor = (valor_fracionado_apos_primeira_hora * 1.5) + 10
    print(f"Valor fracionado, R${valor: .2f}")