# 1) Your password must be at least 5 characters.
# 2) Your password must include a number.
# 3) Your password must include an uppercase letter.
# 4) Your password must include a special character.
# 5) The digits in your password must add up to 25.
# 6) Your password must include a roman numeral.
# 7) Incluir número sorteado (11..99)
# 8) escolha livre
# 9) escolha livre
# 10) escolha livre

import random
from string import punctuation

print("================== Jogo da Senha ==================")

password = str()

roman_char = ["I", "V", "X", "L", "C", "D", "M"]

def subtitle_progress():
    subtitle = str(len(password)) + " caracteres"
    if have_sum(password) > -1:
        subtitle += " - Número: ok"
    if is_upper(password):
        subtitle += " - Maiúscula: ok"
    if is_special(password):
        subtitle += " - Char especial: ok"
    if is_roman(password):
        subtitle += " - Número romano: ok"

    return subtitle


def have_sum(senha_sum):
    sum_digit = -1
    for x in senha_sum:
        if x.isdigit():
            z = int(x)
            sum_digit = sum_digit + z

    return sum_digit


def is_upper(senha_upper):
    upper = False
    for i in senha_upper:
        if i.isupper():  # verifica maiúsculas
            upper = True
        else:
            upper = False

    return upper


def is_special(senha_special):
    special = False
    for i in range(0, len(senha_special) - 1):
        for j in range(0, len(punctuation) - 1):  # verifica se contém caracteres especiais
            if senha_special[i] == punctuation[j]:
                special = True
            else:
                special = False

        return special


def is_roman(senha_roman):
    roman = False
    for i in range(0, len(senha_roman) - 1):
        for j in range(0, len(roman_char) - 1):  # verifica se contém números romanos
            if senha_roman[i] == roman_char[j]:
                roman = True
            else:
                roman = False

    return roman


while True:
    print(f"Senha: {password} - {subtitle_progress()}")
    if len(password) < 5:
        password = input("Insira uma senha com 5 caracteres: ")
    else:
        if have_sum(password) < 0:
            str_number = input("Insira um número positivo: ")
            if str_number.isnumeric():
                password += str_number
        else:
            if not is_upper(password):
                str_upper = input("Insira uma letra maiúscula: ")
                if str_upper.isupper():
                    password += str_upper
                else:
                    print(f"Maiúscula: ok")
                    break
