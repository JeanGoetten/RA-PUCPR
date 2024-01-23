my_dict = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [0, 3], 5: [1, 0], 6: [1, 1], 7: [1, 2], 8: [1, 3],
       9: [2, 0], 10: [2, 1], 11: [2, 2], 12: [2, 3], 13: [3, 0], 14: [3, 1], 15: [3, 2], 0: [3, 3]}

mais_perto = 1000

def find_position(matriz_b, value):
    my_list = []
    for i in range(len(matriz_b)):
        for j in range(len(matriz_b[i])):
            if matriz_b[i][j] == value:
                my_list = [i, j]
    return my_list


def distancia(pos_atual, pos_original):
    dist = 0
    if pos_atual[0] < 0 or pos_atual[0] > 3:
        return
    elif pos_atual[1] < 0 or pos_atual[1] > 3:
        return
    else:
        #print(pos_atual)
        dist = abs(pos_original[0] - pos_atual[0]) + abs(pos_original[1] - pos_atual[1])
        return dist


def resolve(dic, matriz):
    global mais_perto
    blanc_pos_list = find_position(matriz, 0) #posição do zero
    #print(blanc_pos_list)
    #print()

    if_w_move_pos = blanc_pos_list.copy()
    if_w_move_pos[0] = if_w_move_pos[0] - 1
    #print(if_w_move_pos)

    if_a_move_pos = blanc_pos_list.copy()
    if_a_move_pos[1] = if_a_move_pos[1] - 1
    #print(if_a_move_pos)

    if_s_move_pos = blanc_pos_list.copy()
    if_s_move_pos[0] = if_s_move_pos[0] + 1
    #print(if_s_move_pos)

    if_d_move_pos = blanc_pos_list.copy()
    if_d_move_pos[1] = if_d_move_pos[1] + 1
    #print(if_d_move_pos)

    if if_w_move_pos[0] >= 0:
        w_value = matriz[if_w_move_pos[0]][if_w_move_pos[1]]
    else:
        w_value = matriz[if_w_move_pos[0]][if_w_move_pos[1]]
    #print(w_value)
    if if_a_move_pos[1] >= 0:
        a_value = matriz[if_a_move_pos[0]][if_a_move_pos[1]]
    else:
        a_value = matriz[if_a_move_pos[0]][if_a_move_pos[1]]
        #print(a_value)
    if if_s_move_pos[0] <= 3:
        s_value = matriz[if_s_move_pos[0]][if_s_move_pos[1]]
    else:
        s_value = matriz[if_s_move_pos[0]][if_s_move_pos[1]]
        #print(s_value)
    if if_d_move_pos[0] <= 3:
        d_value = matriz[if_d_move_pos[0]][if_d_move_pos[1]]
    else:
        d_value = matriz[if_d_move_pos[0]][if_d_move_pos[1]]
        #print(d_value)

    w_original_pos = dic[w_value]
    a_original_pos = dic[a_value]
    s_original_pos = dic[s_value]
    d_original_pos = dic[d_value]

    w_distancia = distancia(if_w_move_pos, w_original_pos)

    a_distancia = distancia(if_a_move_pos, a_original_pos)
    s_distancia = distancia(if_s_move_pos, s_original_pos)
    d_distancia = distancia(if_d_move_pos, d_original_pos)

    move = [5, 5]

    if w_distancia < mais_perto:
        mais_perto = w_distancia
        move = if_w_move_pos
    elif a_distancia < mais_perto:
        mais_perto = a_distancia
        move = if_a_move_pos
    elif s_distancia < mais_perto:
        mais_perto = s_distancia
        move = if_s_move_pos
    elif d_distancia < mais_perto:
        mais_perto = d_distancia
        move = if_d_move_pos
    else:
        print("move qualquer um")

    matriz[blanc_pos_list[0]][blanc_pos_list[1]] = matriz[move[0]][move[1]]
    matriz[move[0]][move[1]] = 0




