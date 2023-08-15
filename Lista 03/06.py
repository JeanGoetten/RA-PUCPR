# Tendo como dados de entrada a altura (h) e o sexo (s) de uma pessoa (use 1 - masculino e 2 -
# feminino) elabore um algoritmo que calcule o peso ideal (p) do usuário utilizando as seguintes
# fórmulas:
# • para homens: p = (72.7 × h) - 58
# • para mulheres: p = (62.1 × h) - 44.7

print(" ================ Peso ideal por sexo ==================")

try:

    h = int(input("Qual a altura (cm): "))
    s = int(input("Qual o sexo (1 - masculino e 2 - feminino): "))

    def peso_ideal(s, h):
        if s == 1:
            p = (72.7 * h/100) - 58
        if s == 2:
            p = (62.1 * h/100) - 44.7
        return p


    print(f"Peso ideal: {peso_ideal(s, h): .2f}")
except:
    print("Falha: o usuário não sabe ler")

