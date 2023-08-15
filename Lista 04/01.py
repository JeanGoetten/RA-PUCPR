# A partir da leitura da idade de uma pessoa, elabore um algoritmo que informe a sua classe eleitoral,
# sabendo que menores de 16 não votam (não votante), que o voto é obrigatório para adultos entre 18 e 65 anos
# (eleitor obrigatório) e que o voto é opcional para eleitores entre 16 e 18, ou maiores de 65 anos (eleitor facultativo)

print(" ================ Classificação eleitoral ==================")

idade = int(input("Idade: "))

if idade < 16:
    print("Não votante")
elif idade >= 16 | idade < 18 or idade > 65:
    print("Eleitor facultativo")
else:
    print("Eleitor obrigatório")

