# Construa um algoritmo que seja capaz de concluir qual dentre os seguintes animais foi escolhido, através de perguntas
# e respostas. Animais possíveis: leão, cavalo, homem, macaco, morcego, baleia, avestruz, pinguim, pato, águia, tartaruga,
# crocodilo e cobra. A ideia é usar seleção encadeada e fazer as perguntas de acordo com as respostas do usuário e concluir
# qual é o animal selecionado.
# Exemplos:
# É mamífero? Sim.
# É quadrúpede? Sim.
# É carnívoro? Não.
# É herbívoro? Sim.
# Então o animal escolhido foi o cavalo.
# Utilize as seguintes classificações:


print("================== Noah - The chosen One =====================")

animal = ["leão", "cavalo", "homem", "macaco", "morcego",
          "baleia", "avestruz", "pinguim", "pato", "águia",
          "tartaruga", "cocrodilo", "cobra", ]

print(f"0 - {animal[0]}; 1 - {animal[1]}; 2 - {animal[2]}; 3 - {animal[3]}; 4 - {animal[4]};")
print(f"5 - {animal[5]}; 6 - {animal[6]}; 7 - {animal[7]}; 8 - {animal[8]}; 9 - {animal[9]};")
print(f"10 - {animal[10]}; 11 - {animal[11]}; 12 - {animal[12]};")

while True:
    escolha = int(input("Escolha um animal da lista acima (não se preocupe, não saberei qual é): "))
    if 0 > escolha > 12:
        print("Escolha um animal válido...")
        continue
    else:
        break

mamifero = input("É mamífero (Sim; Não)?")

if mamifero.upper() == "SIM":
    quadrupede = input("É quadrupede (Sim; Não)?")
    if quadrupede.upper() == "SIM":
        carnivoro = input("É carnivoro (Sim; Não)?")
        if carnivoro.upper() == "SIM":
            print("Leão")
        else:
            print("Cavalo")
    else:
        bipede = input("É bipede (Sim; Não)?")
        if bipede.upper() == "SIM":
            onivoro = input("É onivoro (Sim; Não)?")
            if onivoro.upper() == "SIM":
                print("Homem")
            else:
                print("Macaco")
        else:
            voador = input("É voador (Sim; Não)?")
            if voador.upper() == "SIM":
                print("Morcego")
            else:
                print("Baleia")
else:
    ave = input("É ave (Sim; Não)?")
    if ave.upper() == "SIM":
        nao_voadora = input("É nao-voadora (Sim; Não)?")
        if nao_voadora.upper() == "SIM":
            tropical = input("É tropical (Sim; Não)?")
            if tropical.upper() == "SIM":
                print("Avestruz")
            else:
                print("Pinguim")
        else:
            nadadora = input("É nadadora (Sim; Não)?")
            if nadadora.upper() == "SIM":
                print("Pato")
            else:
                print("Águia")
    else:
        casco = input("Tem casco (Sim; Não)?")
        if casco.upper() == "SIM":
            print("Tartaruga")
        else:
            sem_patas = input("É sem patas (Sim; Não)?")
            if sem_patas.upper() == "SIM":
                print("Cobra")
            else:
                print("Crocodilo")