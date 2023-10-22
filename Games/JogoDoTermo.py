import csv
import random
from unidecode import unidecode         # CONVERTE CARACTERES ESPECIAIS EM NORMAIS

print("=============== Jogo do Termo ===============")
print("================== VERDE ====================")
print("================== IGUAL ====================")
print("================== \033[32mTERMO\033[0m ====================")
print("================== JOGOS ====================")
print("================== FAZER ====================")
print("================== SOBRE ====================")

# iMPORT FILE AND CONVERT CSV TO LIST
with open('termos.csv', encoding="utf8") as csv_file:
    csv_termos = csv.reader(csv_file)
    list_termos = []
    for row in csv_termos:
        list_termos.append(row[0])

# VAR INIT
palavra_semi_secreta = "-----"
tentativas = 6
player_try ="-----"
letras_erradas = ""
letras_posicao_errada = ""

# RANDOM TERMO FROM TERMO LIST
r_number = random.randint(0, len(list_termos) - 1)
palavra_secreta = list_termos[r_number]

print(palavra_secreta) # DEBUG

# FUNÇÃO QUE VERIFICA CADA LETRA DO INPUT EM RELAÇÃO AO TERMO SECRETO
def verifica_palavra(player_try):
    global palavra_semi_secreta
    global letras_erradas
    global letras_posicao_errada

    palavra_semi_secreta_list = list(palavra_semi_secreta)      # CONVERTE A STRING PARA LISTA

    if len(player_try) != 5:            # VERIFICA SE O INPUT TEM O TAMNHO EXIGIDO
        print("O termo precisa ter 5 letras")
        return
    elif not none_termo(player_try):    # VERIFICA SE O INPUT É UMA PALAVRA EXISTENTE (NA LISTA)
        print("Termo inválido")
        return
    else:                               # VERIFICA O VALOR (DE JOGO) DE CADA LETRA NO INPUT
        for i in range(len(palavra_secreta)):
            if unidecode(player_try[i].upper()) == palavra_secreta[i]:                     # CERTO
                palavra_semi_secreta_list[i] = player_try[i].upper()
                print('\033[32m' + player_try[i].upper(), end='' + '\033[0m')
            elif unidecode(player_try[i].upper()) in palavra_secreta:                      # QUASE CERTO
                palavra_semi_secreta_list[i] = "-"
                letras_posicao_errada += player_try[i].upper()
                print('\033[33m' + player_try[i].upper(), end='' + '\033[0m')
            else:                                                                           # ERRADO
                palavra_semi_secreta_list[i] = "-"
                letras_erradas += player_try[i].upper()
                print('\033[31m' + player_try[i].upper(), end='' + '\033[0m')
        print()
    palavra_semi_secreta = ''.join(palavra_semi_secreta_list)                               # CONVERTE A LISTA PARA STRING
    return


def none_termo(termo_verificar):                # VERIFICA SE O INPUT É UMA PALAVRA VÁLIDA (NA LISTA)
    for x in list_termos:
        #print(f"{x} == {unidecode(termo_verificar.upper())}")          # DEBUG
        if x == unidecode(termo_verificar.upper()):
            return True
    return False


while True:
    if unidecode(palavra_semi_secreta) == palavra_secreta:      #COMPARA A PALAVRA CONSTRUIDA PELO JOGADOR É IGUAL À SECRETA
            print(f"Parabéns, você descobriu o termo secreto {player_try} em {6 - tentativas} tentativas")
            break
    elif tentativas > 0:        # MANTÉM O JOGO ENQUANTO HÁ TENTATIVAS
        print(f"Letras erradas: \033[31m{letras_erradas}\033[0m | "
              f"Posição errada: \033[33m{letras_posicao_errada}\033[0m | "
              f"Acertos: \033[32m{palavra_semi_secreta}\033[0m")        # DISPLAY DE INFORMAÇÕES AO JOGADOR

        player_try = input(f"Advinhe o termo (5 letras - {tentativas} tentativas restantes): ")
        verifica_palavra(player_try)
        tentativas -= 1

    else:       # ENCERRA O JOGO QUANDO AS TENTATIVAS ACABAM
        print(f"As tentativas se esgotaram. A palavra secreta era {palavra_secreta}. Reinicie para tentar de novo. ")
        break