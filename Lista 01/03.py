# ler o valor do salário e calcular quantos salários mínimos equivale

print("============== Salário em salários mínimos ==============")

salario = input("Insira o valor de seu salário: ")

def converte_para_salario_minimo(a):
    b = float(a)
    salarios_minimos = b/1320
    return salarios_minimos


salario_convertido = converte_para_salario_minimo(salario)
print(f'Você recebe {salario_convertido:.2f} salários mínimos')