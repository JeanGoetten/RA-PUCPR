# ler nome de usuário e então mostrar "Bem-vindo NOME! Seu nome tem 4 letras"

name = input("Insira seu nome: ")

name_uppercase = name.upper()
name_letter_count = len(name)

print(f"Bem-vindo {name_uppercase}! Seu nome tem {name_letter_count} letras")
