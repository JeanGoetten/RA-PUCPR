from random import randint

# lista com diversas strings, no caso frutas, é a base de palavras do jogo
lista = ["abacate", "morango", "uva", "banana", "limao", "ameixa", "coco"]

# sorteia uma posição da lista
pos = randint(0, len(lista) - 1)

# guarda o segredo, uma das strings da lista, a fruta que esta na posição pos
s = lista[pos]

# criando lista tela do mesmo comprimento do segredo
t = ["_"] * len(s)
print(s)

print("\n>>> Jogo da Forca <<<\n")
print("Dica: é uma fruta!\n")
print("Segredo: ", end='')

ganhou = False
perdeu = False
vida = 6

# loop principal do jogo, termina apenas com vitória ou derrota do jogador
while not ganhou and not perdeu:
    for l in t:  # imprimindo a tela
        print(l, end=" ")
    print(f"\nVidas: {vida}")
    c = input("\nQual letra? ")
    for i in range(0, len(s), 1):
        # print(f"Comparando {c} com {s[i]}")
        if c == s[i]:
            t[i] = c

    # testar vitoria
    if "_" not in t:
        ganhou = True
        print(f"Parabéns, voce ganhou! O segredo era '{s}'")

    # testar derrota
    if c not in t:
        vida = vida - 1
        print(f"Perdeu uma vida")

    if vida == 0:
        perdeu = True
        print(f"Lamento, voce perdeu! O segredo era '{s}'")

print()