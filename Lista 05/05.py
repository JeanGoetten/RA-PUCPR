# Elabore um algoritmo que leia um número inteiro (n), e se este número atender a condição 1 ≤ n ≤ 99, mostre seu
# valor por extenso (exemplo: para n = 38, a saída será “trinta e oito”); caso contrário mostre “Entrada fora dos limites
# operacionais!”. Empregue separação do número em dezena e unidade (usando mod e div) e seleção encadeada (não usar
# dicionário ou lista de strings, a ideia é reforçar seleção encadeada com diversos prints) [Refaremos este exercício mais a
# frente, com listas e também com dicionário]

print("========== Número para texto da Idade das Pedras ==============")

import math

n = int(input("Insira um número inteiro: "))

def numero_por_extenso(n):
    n_dezena = math.floor(n/10)
    n_unidade = n % 10

    # print(n_dezena)
    # print(n_unidade)

    txt_dezena = ""
    txt_conj = ""
    txt_unidade = ""

    if n_unidade == 0:
        txt_unidade = ""
        txt_conj = ""
    elif n_unidade == 1:
        txt_unidade = "Um"
        txt_conj = "e"
    elif n_unidade == 2:
        txt_unidade = "dois"
        txt_conj = "e"
    elif n_unidade == 3:
        txt_unidade = "tres"
        txt_conj = "e"
    elif n_unidade == 4:
        txt_unidade = "quatro"
        txt_conj = "e"
    elif n_unidade == 5:
        txt_unidade = "cinco"
        txt_conj = "e"
    elif n_unidade == 6:
        txt_unidade = "seis"
        txt_conj = "e"
    elif n_unidade == 7:
        txt_unidade = "sete"
        txt_conj = "e"
    elif n_unidade == 8:
        txt_unidade = "oito"
        txt_conj = "e"
    else:
        txt_unidade = "nove"
        txt_conj = "e"

    if n_dezena == 0:
        txt_dezena = ""
        txt_conj = ""
    elif n_dezena == 1:
        txt_conj = ""
        txt_unidade = ""
        if n_unidade == 0:
            txt_dezena = "Dez"
        elif n_unidade == 1:
            txt_dezena = "Onze"
        elif n_unidade == 2:
            txt_dezena = "Doze"
        elif n_unidade == 3:
            txt_dezena = "Treze"
        elif n_unidade == 4:
            txt_dezena = "Quatorze"
        elif n_unidade == 5:
            txt_dezena = "uinze"
        elif n_unidade == 6:
            txt_dezena = "Dezesseis"
        elif n_unidade == 7:
            txt_dezena = "Dezessete"
        elif n_unidade == 8:
            txt_dezena = "Dezoito"
        else:
            txt_dezena = "Dezenove"
    elif n_dezena == 2:
        txt_dezena = "Vinte"
    elif n_dezena == 3:
        txt_dezena = "Trinta"
    elif n_dezena == 4:
        txt_dezena = "Quarenta"
    elif n_dezena == 5:
        txt_dezena = "Cinquanta"
    elif n_dezena == 6:
        txt_dezena = "Sessenta"
    elif n_dezena == 7:
        txt_dezena = "Setenta"
    elif n_dezena == 8:
        txt_dezena = "Oitenta"
    else:
        txt_dezena = "Noventa"

    if n < 10:
        print(f"{txt_unidade}")
    elif n >= 10:
        print(f"{txt_dezena} {txt_conj} {txt_unidade}")



if 1 <= n <= 99:
    numero_por_extenso(n)
else:
    print("Entrada fora dos limites operacionais!")