# O plano cartesiano está divido em quatro partes pelos eixos X (eixo das abscissas - coordenada horizontal) e Y (eixo
# das ordenadas - coordenada vertical) chamadas de quadrantes. O quadrante superior da direita é o primeiro, o superior
# esquerdo é o segundo, o inferior esquerdo é o terceiro e o inferior direito é o quarto. Elabore um algoritmo que leia os
# valores de uma coordenada (x, y) do plano cartesiano e informe em qual quadrante este ponto se encontra.

print("===================== Batalha Naval ==========================")

print("Fontes de inteligência informam que o inimigo está se aproximando dos mares do sul.")
print("Suas ordens são para exterminá-lo. ")
print("Os aviões estão sobrevoando a região que vai do ponto 100 ao -100 norte e sul e leste ao oeste. ")
print("Informe as coordenadas para que possam disparar corretamente!")

import random

enemy_pos = [0, 0]

x = int(input("Coordenada norte/sul: "))
y = int(input("Coordenada leste/oeste: "))

def quadrante_externo(x, y):
    quadrante = ""
    if x > 100 and y > 100:
        quadrante = "primeiro"
    elif x < -100 and y > 100:
        quadrante = "segundo"
    elif x < -100 and y < -100:
        quadrante = "terceiro"
    elif x > 100 and y < -100:
        quadrante = "quarto"
    else:
        return

    return quadrante

def quadrante(x, y):
    quadrante = ""
    if x > 0 and y > 0:
        quadrante = "primeiro"
    elif x < 0 and y > 0:
        quadrante = "segundo"
    elif x < 0 and y < 0:
        quadrante = "terceiro"
    else:
        quadrante = "quarto"

    return quadrante

if x > 0 and x <= 100:
    if y > 0 and y <= 100:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
    else:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
elif x < 0 and x > -100:
    if y > 0 and y <= 100:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
    else:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
elif x == 0 and y == 0:
    print("Godam! Você bombardeou a si mesmo!")
else:
    print(f"Você errou feio, errou rude, acertou um país aliado vizinho no {quadrante_externo(x, y)} quadrante. Agora a coisa ficou feia!")


def enemy_position():
    enemy_x = random.randint(-100, 100)
    enemy_y = random.randint(-100, 100)
    enemy_position = [enemy_x, enemy_y]
    return enemy_position


def combate(x, y):
    enemy_pos = enemy_position()
    if x == enemy_pos[0] and y == enemy_pos[1]:
        print(f"WoW! Na mosca! Você acertou o inimigo em {enemy_pos}")
    else:
        print(f"Derrota! O Inimigo atacou a partir do {quadrante(enemy_pos[0], enemy_pos[1])} quadrante nas coordenadas {enemy_pos}")


combate(x, y)