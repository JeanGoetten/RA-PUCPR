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

print("================== Jogo da Senha ==================")

password = str()

special_char = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
roman_char = ["I", "V", "X", "L", "C", "D", "M"]

def subtitle_progress():
    subtitle = str(len(password)) + " caracteres"
    if is_number(password):
        subtitle += " - Número: ok"
    if is_upper(password):
        subtitle += " - Maiúscula: ok"
    if is_special(password):
        subtitle += " - Char especial: ok"
    if is_roman(password):
        subtitle += " - Número romano: ok"
    if have_sum(password) == 25:
        subtitle += " - Soma: ok"
    return subtitle


def is_number(senha_number):
    number = False
    for x in senha_number:
        if x.isnumeric():
            number = True
            break
        else:
            number = False
    return number


def have_sum(senha_sum):
    sum_digit = 0
    for x in senha_sum:
        if x.isdigit():
            z = int(x)
            sum_digit = sum_digit + z
    print(sum_digit)
    return sum_digit


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
    special = False
    for i in senha_special:
        for j in special_char:  # verifica se contém caracteres especiais
            if j == i:
                special = True
                break
            else:
                special = False

    return special


def is_roman(senha_roman):
    roman = False
    for i in senha_roman:
        for j in roman_char:  # verifica se contém números romanos
            if i == j:
                roman = True
                break
            else:
                roman = False

    return roman


while True:
    for char in password:
        print(char)
    print(f"Senha: {password} - {subtitle_progress()}")
    if len(password) < 5:
        password = input("Insira uma senha com 5 caracteres: ")
    else:
        if not is_number(password):
            str_number = input("Insira um número: ")
            if is_number(str_number):
                if int(str_number) > -1:
                    password += str_number
        else:
            if not is_upper(password):
                str_upper = input("Insira uma letra maiúscula: ")
                if str_upper.isupper():
                    password += str_upper
            else:
                if not is_special(password):
                    str_special = input("Insira um caracter especial: ")
                    if is_special(str_special):
                        password += str_special
                else:
                    if not is_roman(password):
                        str_roman = input("Insira um número romano: ")
                        if is_roman(str_roman):
                            password += str_roman
                    else:
                        if have_sum(password) != 25:
                            str_sum = input("Insira digitos para a senha somar 25: ")
                            if str_sum.isnumeric():
                                soma_sum = have_sum(str_sum) + have_sum(password)
                                if soma_sum == 25:
                                    password += str_sum
                        else:
                            break

