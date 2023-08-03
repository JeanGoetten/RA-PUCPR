# Exercicio 01 RA

# Um estudante tem 2 notas: um trabalho e uma prova
# A primeira vale 40% e a segunda vale 60%
# Elabore um algoritmo que leia as duas notas e mostre a media do estudante

nota01 = int(input("Insira a nota do trabalho: "))
nota02 = int(input("Insira a nota da prova: "))

media_pond = (nota01*40 + nota02*60)/100

print(f"A media final eh: {media_pond}")

