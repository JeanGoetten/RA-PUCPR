# ler um número inteiro e escrever seu sucessor e antecessor

numero_inteiro = int(input("Insira um número inteiro: "))


def numeroantecessor(a):
    b = a - 1
    return b


def numerosucessor(a):
    b = a + 1
    return b


numero_antecessor = numeroantecessor(numero_inteiro)
numero_sucessor = numerosucessor(numero_inteiro)

print(f"O número antecessor é {numero_antecessor} e o número sucessor é {numero_sucessor}")

