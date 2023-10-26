# insirir dificuldade
# sorteio de acordo com a dificuldade
# loop at[e ganhar
# pedir o movimento wasd
# testar se o movimento é possível
# se sim, movimenta e atualiza a matriz
# mostra a matriz
# verifica se ganhou
# parabeniza e termina
#
from random import randint
print("============= Jogo do Quinze =============")
print()

mi = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9,  10, 11, 12],
     [13, 14, 15, 0]]

mj = [[1,  2,  3,  4],
     [5,  6,  7,  8],
     [9,  10, 11, 12],
     [13, 14, 15, 0]]

level = 1

def imprimeMat(m):
    for l in range(4):
        for c in range(4):
            if m[l][c] == 0:
                print(" #")
            else:
                print(f"{m[l][c]:2}", end="  ")
        print()

def embaralhaMat(mj, level):
    #usar o level para fazer mais ou menos sorteios
    l = 3
    c = 3
    total = 2**level
    while total > 0:
        dir = randint(1, 4) # direçoes
        if dir == 1: # cima
            if l>0: #pode mover pra cima
                m[l][c] = m[l-1][c] #abaixa o valor de cima
                l = l-1
                m[l][c] = 0 #move pra cima
        elif dir == 2:
            if c>0:
                #etc


#imprimeMat(mi)