# ler o ano de nascimento, calcular e mostrar a idade no ano corrente

import datetime

nasc = int(input("Ano de nascimento: "))
data_agora = datetime.datetime.today()
ano = data_agora.year
idade = ano - nasc

print(f"Em {ano} vc faz {idade} anos")