import os
from time import sleep
from random import randint

print("================= Jogo do Quinze =================")


l = 3
c = 3

checkPlay = ""
def embaralhaMat(m, dificuldade):
    global l
    global c
    total = 10**dificuldade # em funcao da dificuldade
    anterior = 0 # registra o movimento anterior
    while total > 0:
        dir = randint(1, 4) #1-sobe, 2-direita, 3-desce, 4-esquerda
        if abs(dir - anterior) != 2: #confere zig zag
            if dir == 1: # sorteio deu mover para cima?
                # print("sobe")
                if l > 0: # é possível mover para cima?
                    m[l][c] = m[l-1][c] # baixa o valor da peça
                    l = l - 1 # sobe uma linha
                    m[l][c] = 0 # coloca o vazio em seu novo lugar

                    total = total - 1
                    anterior = dir
            elif dir == 2:
                # print("direita")
                if c < 3: # é possível mover para direita?
                    m[l][c] = m[l][c + 1] # muda para a direita o valor da peça
                    c = c + 1 # para a direita uma coluna
                    m[l][c] = 0 # coloca o vazio em seu novo lugar

                    total = total - 1
                    anterior = dir
            elif dir == 3:
                # print("desce")
                if l < 3: # é possível mover para baixo?
                    m[l][c] = m[l + 1][c] # sobe o valor da peça
                    l = l + 1 # desce uma linha
                    m[l][c] = 0 # coloca o vazio em seu novo lugar

                    total = total - 1
                    anterior = dir
            else:
                # print("esquerda")
                if c > 0: # é possível mover para esquerda?
                    m[l][c] = m[l][c - 1] # muda para a esuqerda o valor da peça
                    c = c - 1 # para a esquerda uma coluna
                    m[l][c] = 0 # coloca o vazio em seu novo lugar

                    total = total - 1
                    anterior = dir

        # precisa de uma lógica para contar
        # apenas sorteios que contribuam para a dificuldade ou uma função específica
        # print("\nTotal: ", total)
        # imprimeMat(m)
        #sleep(1)
        #os.system('clear') # limpa tela macOS Linux
        # os.system('cls') # par windows
def imprimeMat(m):
    for l in range(4):
        for c in range(4):
            if m[l][c] == 0:
                print(" # ",end="")
            else:
                print(f"{m[l][c]:2}", end=" ")
        print()

def move(play, m):
    global checkPlay
    global l
    global c
    if play.upper() == "W":
        if l > 0:

            m[l][c] = m[l - 1][c]  # baixa o valor da peça
            l = l - 1  # sobe uma linha
            m[l][c] = 0  # coloca o vazio em seu novo lugar

            checkPlay = ""
        else:
            checkPlay = "Jogada inválida"
    elif play.upper() == "A":
        if c > 0:

            m[l][c] = m[l][c - 1]  # muda para a esuqerda o valor da peça
            c = c - 1  # para a esquerda uma coluna
            m[l][c] = 0  # coloca o vazio em seu novo lugar

            checkPlay = ""
        else:
            checkPlay = "Jogada inválida"
    elif play.upper() == "S":
        if l < 3:

            m[l][c] = m[l + 1][c]  # sobe o valor da peça
            l = l + 1  # desce uma linha
            m[l][c] = 0  # coloca o vazio em seu novo lugar

            checkPlay = ""
        else:
            checkPlay = "Jogada inválida"
    elif play.upper() == "D":
        if c < 3:

            m[l][c] = m[l][c + 1]  # muda para a direita o valor da peça
            c = c + 1  # para a direita uma coluna
            m[l][c] = 0  # coloca o vazio em seu novo lugar

            checkPlay = ""
        else:
            checkPlay = "Jogada inválida"

    else:
        checkPlay = "Jogada inválida"


def verificaVit(mj, mi):
    if mj == mi:
        return True

def autoResolve(mj, mi):
    printCheck = True
    while mj != mi:
        os.system('cls')
        print()

        imprimeMat(mj)

        if printCheck:
            print("Aguarde enquanto o computador resolve...")
            printCheck = False
        else:
            print("Aguarde enquanto o computador resolve..")
            printCheck = True

        print()

        sleep(1)


# matriz inicial e que será usada para a função testar vitória
mi = [[1, 2, 3, 4],
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 0]] # peça vazia -> 0
# matriz para embaralhar e jogar
mj = [[1, 2, 3, 4], # era para usar copy....
      [5, 6, 7, 8],
      [9, 10, 11, 12],
      [13, 14, 15, 0]] # peça vazia -> 0

# programa principal
opcao = int(input("Escolha a dificuldade (1 - fácil; 2 - médio; 3 - difícil): "))
embaralhaMat(mj, opcao)
# input("Tecle <enter> quando pronto para jogar")
vitoria = False
# loop até ganhar
while not vitoria:
    os.system('cls')
    print()
    imprimeMat(mj)
    print()
    if checkPlay:
        print(f"\033[1;31;40m{checkPlay}\033[0;37;40m")

    play = input("Insira W: cima - A: esquerda - S: baixo - D: direita - R: auto resolve - e aperte enter: ")
    if play.upper() == "R":
        autoResolve(mj, mi)
    else:
        move(play, mj)
    if verificaVit(mj, mi):
        os.system('cls')
        print("Parabéns, você ganhou!")
        vitoria = True