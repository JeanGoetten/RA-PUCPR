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

print("================== Jogo da Senha ==================")

password = str()
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
sum = int()
def pass_analyser(password):
    for i in range(0, len(password) - 1):
        for j in range(0, len(numbers) - 1):
            if password[i] == numbers[j]:
                sum = sum + int(password[i])
        


while True:
    print(f"Senha: {password }")
    if len(password) < 5:
        password = input("Insira uma senha com 5 caracteres: ")
    else:
