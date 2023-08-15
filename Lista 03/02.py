# A partir do ano de nascimento informado pelo usuário, elabore um algoritmo que informe a
# idade que completará (ou já completou) no ano atual (pega ano do sistema via Python). Verifique
# se ele já pode fazer a carteira de motorista ou não, informando sua situação.

print(" ================ Já pode fazer a CNH? ==================")

import datetime

nasc = int(input("Ano de nascimento: "))
data_agora = datetime.datetime.today()
ano = data_agora.year
idade = ano - nasc
if idade >= 18:
    print(f"Já pode fazer a CNH!")
else:
    print(f"Ainda não pode fazer a CNH!")