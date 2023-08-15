# Elabore um algoritmo que leia um número inteiro e verifique se ele é par ou ímpar.


print(" ================ Par ou ímpar ==================")

try: # apenas uma alternativa a erro de entrada parte 1
    not_a_int_number = input("Insira um número inteiro: ")
    number = int(not_a_int_number) # apenas um tratamento da entrada
    def par_ou_impar(number):
        dif = number % 2
        if dif == 0:
            result = "par"
        else:
            result = "impar"
        return result


    print(f"O número {number} é {par_ou_impar(number)}")
except: # apenas uma alternativa a erro de entrada parte 2
    print(f"'{not_a_int_number}' não é um número inteiro!")