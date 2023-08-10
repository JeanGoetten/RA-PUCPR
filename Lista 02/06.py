# No sistema de medidas imperiais (adotado no Reino Unido), um pé (medida de comprimento)
# corresponde a doze polegadas, e três pés são uma jarda. Considerando que uma polegada corresponde a 2,54
# centímetros, elabore um algoritmo que leia o valor de uma medida de comprimento (em metros), e mostre o
# valor equivalente em pés, polegadas e jardas.

print("============== Conversor sistema decimal para sistema imperial ==============")

metros = float(input("Comprimento (metros): "))

cm = metros*100

pol = cm/2.54
pes = pol/12
jar = pes/3

print(f"polegadas: {pol: .2f}")
print(f"pés: {pes: .2f}")
print(f"jardas: {jar: .2f}")