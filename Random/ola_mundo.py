import datetime

nome = input("Qual seu nome? ")
nasc = int(input("Ano de nascimento: "))
data_agora = datetime.datetime.today()
ano = data_agora.year
idade = ano - nasc
print(f"Bom dia {nome}")
print(f"Em {ano} vc faz {idade} anos")
