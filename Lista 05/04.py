# O plano cartesiano está divido em quatro partes pelos eixos X (eixo das abscissas - coordenada horizontal) e Y (eixo
# das ordenadas - coordenada vertical) chamadas de quadrantes. O quadrante superior da direita é o primeiro, o superior
# esquerdo é o segundo, o inferior esquerdo é o terceiro e o inferior direito é o quarto. Elabore um algoritmo que leia os
# valores de uma coordenada (x, y) do plano cartesiano e informe em qual quadrante este ponto se encontra.

print("===================== Batalha Naval Pós Racionalista ==========================")

import random

map_min_x = random.randint(0, 999)
map_max_x = random.randint(0, 999)
map_min_y = random.randint(0, 999)
map_max_y = random.randint(0, 999)

map_min_x = map_min_x * (-1)
map_min_y = map_min_y * (-1)

print("Fontes de inteligência informam que o inimigo está se aproximando dos mares do sul.")
print("Suas ordens são para exterminá-lo. ")
print(f"Os aviões estão sobrevoando a região que vai de: ")
print(f"ponto {map_min_y} ao {map_max_y} de norte ao sul  ")
print(f"ponto {map_min_x} ao {map_max_x} de lest ao oeste  ")
print("Informe as coordenadas para que possam disparar corretamente!")

enemy_pos = [0, 0]

x = int(input("Coordenada norte/sul: "))
y = int(input("Coordenada leste/oeste: "))

def quadrante_externo(x, y):
    if x > map_max_x and y > map_max_y:
        quadrante = "primeiro"
    elif x < map_max_x and y > map_max_y:
        quadrante = "segundo"
    elif x < map_max_x/2 and y < map_max_y/2:
        quadrante = "terceiro"
    elif x > map_max_x and y < map_max_y/2:
        quadrante = "quarto"
    else:
        return

    return quadrante

def quadrante(x, y):
    if x > (map_max_x + abs(map_min_x))/2 and y > (map_max_y + abs(map_min_y))/2:
        quadrante = "primeiro"
    elif x < (map_max_x + abs(map_min_x))/2 and y > (map_max_y + abs(map_min_y))/2:
        quadrante = "segundo"
    elif x < (map_max_x + abs(map_min_x))/2 and y < (map_max_y + abs(map_min_y))/2:
        quadrante = "terceiro"
    else:
        quadrante = "quarto"

    return quadrante


if x > (map_max_x + abs(map_min_x))/2 and x < map_max_x:
    if y > (map_max_y + abs(map_min_y))/2 and y < map_max_y:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
    else:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
elif x < (map_max_x + abs(map_min_x))/2 and x > map_min_x:
    if y > (map_max_y + abs(map_min_y))/2 and y < map_max_y:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
    else:
        print(f"Disparo no {quadrante(x, y)} quadrante realizado. Aguardando relatório de combate...")
elif x == 0 and y == 0:
    print("Godam! Você bombardeou a si mesmo!")
else:
    print(f"Você errou feio, errou rude, acertou um país aliado vizinho no {quadrante_externo(x, y)} quadrante. Agora a coisa ficou feia!")


def enemy_position():
    enemy_x = random.randint(map_min_x, map_max_x)
    enemy_y = random.randint(map_min_y, map_max_y)
    enemy_position = [enemy_x, enemy_y]
    return enemy_position


def combate(x, y):
    enemy_pos = enemy_position()
    if x == enemy_pos[0] and y == enemy_pos[1]:
        print(f"WoW! Na mosca! Você acertou o inimigo em {enemy_pos}")
    else:
        print(f"Derrota! O Inimigo atacou a partir do {quadrante(enemy_pos[0], enemy_pos[1])} quadrante nas coordenadas {enemy_pos}")


combate(x, y)