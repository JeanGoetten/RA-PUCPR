# [8] Considerando que 1 milha vale exatamente 1.609,344 metros, imprima uma tabela de conversão de metros (m)
# para milhas (mi.), de 20 km até 160 km, de 10 em 10 kilômetros.

print("================ While ================")
m = 20
while m <= 160:
    milha = m * 1609.344
    print(milha)
    m = m + 10


print("")
print("================ For ================")
for i in range(20, 161, 10):
    print(i * 1609.344)