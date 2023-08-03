# Exercicio 01 RA

# Um estudante tem 2 notas: um trabalho e uma prova
# A primeira vale 40% e a segunda vale 60%
# Elabore um algoritmo que leia as duas notas e mostre a media do estudante

nota_trabalho = float(input("Insira a nota do trabalho: "))
nota_prova = float(input("Insira a nota da prova: "))

media_pond = (nota_trabalho*40 + nota_prova*60)/100

print(f"A media final eh: {media_pond}")

