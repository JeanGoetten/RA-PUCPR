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
import  re
print("================== Jogo da Senha ==================")

password = str()

special_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
roman_char = ["I", "V", "X", "L", "C", "D", "M"]

message_sum = "Insira digitos para a senha somar 25"
def subtitle_progress():
    subtitle = str(len(password)) + " caracteres" + " - Soma: " + str(have_sum(password, True))
    if is_number(password):
        subtitle += " - Número: ok"
    if is_upper(password):
        subtitle += " - Maiúscula: ok"
    if is_special(password):
        subtitle += " - Char especial: ok"
    if is_roman(password):
        subtitle += " - Número romano: ok"
        subtitle += " - Número aleatório: ok"
    return subtitle


def is_number(senha_number):
    for x in senha_number:
        if x.isdigit():
            return True


def have_sum(senha_sum, sum):
    sum_digit = 0
    for x in senha_sum:
        if x.isnumeric():
            z = int(x)
            sum_digit = sum_digit + z
    return sum_digit


def have_sub(senha_sub):
    sub_index = 0
    global password
    password_list = list(password)
    for x in range(0, len(password) - 1):
        if password[x].isnumeric():
            if sub_index < len(senha_sub):
                print(f"{senha_sub[sub_index]} for {x}")
                password_list[x] = senha_sub[sub_index]
                sub_index += 1
    password = ''.join(password_list)


def is_upper(senha_upper):
    upper = False
    for i in senha_upper:
        if i.isupper():  # verifica maiúsculas
            upper = True
            break
        else:
            upper = False

    return upper


def is_special(senha_special):
    for i in senha_special:
        for j in special_char:  # verifica se contém caracteres especiais
            if j == i:
                return True


def is_roman(senha_roman):
    for i in senha_roman:
        for j in roman_char:  # verifica se contém números romanos
            if i == j:
                return True


def make_random():
    return random.randint(11, 99)


while True:
    print(f"Senha: {password} - {subtitle_progress()}")
    if len(password) < 5:
        password = input("Insira uma senha com 5 caracteres: ")

    elif not is_number(password):
        str_number = input("Insira um número: ")
        if is_number(str_number):
            if int(str_number) > -1:
                password += str_number

    elif not is_upper(password):
        str_upper = input("Insira uma letra maiúscula: ")
        if str_upper.isupper():
            password += str_upper

    elif not is_special(password):
        str_special = input("Insira um caracter especial: ")
        if is_special(str_special):
            password += str_special

    elif have_sum(password, True) != 25:
        if have_sum(password, True) > 25:
            str_sum = input(f"Substitua números para a senha somar 25: ")
            if str_sum.isnumeric():
                have_sub(str_sum)
        else:
            str_sum = input(f"Adicione números para a senha somar 25: ")
            if str_sum.isnumeric():
                soma_sum = have_sum(str_sum, True) + have_sum(password, True)
                if soma_sum == 25:
                    password += str_sum

    elif not is_roman(password):
        str_roman = input("Insira um número romano: ")
        if is_roman(str_roman):
            password += str_roman
            password += str(random.randint(11, 99))

    else:
        break

