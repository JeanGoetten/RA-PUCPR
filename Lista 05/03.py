# Escreva um algoritmo que jogue Joquempô (Pedra, Papel e Tesoura) com o usuário; o programa escolhe
# randomicamente a jogada do computador, depois lê a opção do usuário e finalmente mostra o resultado da rodada: vitória
# do computador, vitória do usuário ou empate (pesquise sobre números randômicos em Python, em particular sobre randint
# e associe um número inteiro a cada opção do jogo, como seleção encadeada descubra o vencedor ou se houve empate)

# pedra = 1
# papel = 2
# tesoura = 3

print("============== Joquempo ==============")

import random

print("1 - Pedra")
print("2 - Papel")
print("3 - Tesoura")

skills = ["pedra", "papel", "tesoura"]

while True:
    player_play = int(input("Jogar: "))
    if player_play < 1 or player_play > 3:
        print("Vc perdeu. Jogue novamente!")
        continue
    else:
        break


def computer_play():
    play = random.randint(1, 3)
    return play


def game():
    cpu_play = computer_play()
    # pega a string da jogada do cpu na lista
    if cpu_play == 1:
        cpu_play_name = skills[0]
    elif cpu_play == 2:
        cpu_play_name = skills[1]
    else:
        cpu_play_name = skills[2]
    # pega a string da jogada do player na lista
    if player_play == 1:
        player_play_name = skills[0]
    elif player_play == 2:
        player_play_name = skills[1]
    else:
        player_play_name = skills[2]
    print(f"Player jogou: {player_play_name}")
    print(f"CPU jogou: {cpu_play_name}")
    if cpu_play == 1:
        if player_play == 1:
            print("Empate!")
        elif player_play == 2:
            print("Vc Ganhou!")
        else:
            print("Vc Perdeu!")
    elif cpu_play == 2:
        if player_play == 1:
            print("Vc Perdeu!")
        elif player_play == 2:
            print("Empatou!")
        else:
            print("Vc Ganhou!")
    else:
        if player_play == 1:
            print("Vc Ganhou!")
        elif player_play == 2:
            print("Vc Perdeu!")
        else:
            print("Vc Empatou!")

game()