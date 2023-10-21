import csv
import random
from unidecode import unidecode

print("=============== Jogo do Termo ===============")
print("================== VERDE ====================")
print("================== IGUAL ====================")
print("================== \033[32mTERMO\033[0m ====================")
print("================== JOGOS ====================")
print("================== FAZER ====================")
print("================== SOBRE ====================")

# iMPORT AND CONVERT CSV FILE
with open('termos.csv', encoding="utf8") as csv_file:
    csv_termos = csv.reader(csv_file)
    list_termos = []
    for row in csv_termos:
        list_termos.append(row[0])

# VAR INIT
palavra_semi_secreta = "-----"
tentativas = 6
tentativas_list = []
player_try ="-----"

# RANDOM TERMO FROM TERMO LIST
r_number = random.randint(0, len(list_termos))
palavra_secreta = list_termos[r_number]

print(palavra_secreta)
def verifica_palavra(player_try):
    global palavra_semi_secreta
    global resultado
    global letter
    palavra_semi_secreta_list = list(palavra_semi_secreta)
    if len(player_try) == 5:
        for i in range(len(palavra_secreta)):
            if unidecode(player_try[i].upper()) == palavra_secreta[i]:                     #certo
                palavra_semi_secreta_list[i] = player_try[i].upper()
                print('\033[32m' + player_try[i].upper(), end='' + '\033[0m')
            elif unidecode(player_try[i].upper()) in palavra_secreta:                      # quse certo
                palavra_semi_secreta_list[i] = "-"
                print('\033[33m' + player_try[i].upper(), end='' + '\033[0m')
            else:                                                               # errado
                palavra_semi_secreta_list[i] = "-"
                print('\033[31m' + player_try[i].upper(), end='' + '\033[0m')
        print()
    else:
        print("O termo precisa ter 5 letras")
        return
    palavra_semi_secreta = ''.join(palavra_semi_secreta_list)
    return


while True:
    if unidecode(palavra_semi_secreta) == palavra_secreta:
            print(f"Parabéns, você descobriu o termo secreto {player_try} em {6 - tentativas} tentativas")
            break
    elif tentativas > 0:
        player_try = input(f"Advinhe o termo (5 letras - {tentativas} tentativas restantes): ")
        verifica_palavra(player_try)
        tentativas -= 1

    else:
        print(f"As tentativas se esgotaram. A palavra secreta era {palavra_secreta}. Reinicie para tentar de novo. ")
        break