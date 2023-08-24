# Uma determinada loja de varejo classifica seus produtos utilizando códigos conforme descrito na tabela abaixo.
# Elabore um algoritmo que leia o código de um produto e mostre sua classificação. Para qualquer código inexistente,
# mostre “Código inválido”.
# Código                      Classificação
# 1                           Alimento não perecível
# 2, 3 ou 4                   Alimento perecível
# 5 ou 6                      Vestuário
# 7                           Higiene Pessoal
# 8 até 15                    Limpeza e utensílios domésticos


print("============== Inventario de Loja ==============")

print("CODIGO ........................ CLASSIFICACAO")
print("- 1 ........................... Alimento não perecível")
print("- 2, 3, 4 ..................... Alimento perecível")
print("- 5 ou 6 ...................... Vestuário")
print("- 7 ........................... Higiene Pessoal")
print("- 8 ate 15 .................... Limpeza e utensílios domésticos")



while True:
    cod = int(input("Insira o codigo: "))
    if cod < 1 or cod > 15:
        print("Código inválido")
        continue
    else:
        break

if cod == 1:
    print("Alimento não perecível")
elif cod > 1 and cod < 5:
    print("Alimento perecível")
elif cod > 4 and cod < 7:
    print("Vestuário")
elif cod == 7:
    print("Higiene Pessoal")
elif cod > 7 and cod < 16:
    print("Limpeza e utensílios domésticos")
else:
    print("Envie um email para selbstdenkerdot@hotmail.com")
