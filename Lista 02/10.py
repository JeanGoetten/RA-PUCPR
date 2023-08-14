# Elabore um algoritmo que leia três valores inteiros a, b e c. Em seguida, encontre e mostre o maior dos
# três valores usando a fórmula: maiorAB = (a + b + abs (a - b) ) / 2
# Sendo o abs o valor absoluto.

print("============== Maior valor entre 3 inteiros ==============")

a = int(input("Insira o valor de a: "))
b = int(input("Insira o valor de b: "))
c = int(input("Insira o valor de c: "))

def maior_3(a, b, c):
    maiorAB = (a + b + abs(a - b)) / 2
    maiorCAbs = (maiorAB + c + abs(maiorAB - c)) / 2
    return maiorCAbs


print(f"O maior é: {maior_3(a, b, c): .0f}")