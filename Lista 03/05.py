# Em uma determinada papelaria a fotocópia custa R$ 0,25, caso sejam tiradas menos de 100
# cópias. A partir de 100 cópias, o valor de cada fotocópia tirada reduz para R$ 0,20. Elabore um
# algoritmo que leia o número de cópias que serão feitas e mostre o valor a pagar pelo serviço.

print(" ================ Papelaria Xeroc Holmes ==================")

numero_de_copias = int(input("Qual a quantidade de cópias? "))

def valor_total(numero_de_copias):
    if numero_de_copias < 100:
        valor_por_copia = 0.25
    else:
        valor_por_copia = 0.2

    valor = numero_de_copias * valor_por_copia
    return valor


print(f"Valor total: R${valor_total(numero_de_copias): .2f}")