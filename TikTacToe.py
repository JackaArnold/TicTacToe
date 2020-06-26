board = [0,0,0,
         0,0,0,
         0,0,0]
goal_a = 3
goal_b = 12
a = 1
b = 4
row_1 = [board[0],board[1],board[2]]
row_2 = [board[3],board[4],board[5]]
row_3 = [board[6],board[7],board[8]]
row_4 = [board[0], board[3], board[6]]
row_5 = [board[1], board[4], board[7]]
row_6 = [board[2], board[5], board[8]]
row_7 = [board[0],board[4],board[8]]
row_8 = [board[2],board[4],board[6]]
def update_board():
    global row_1, row_2, row_3, row_4, row_5, row_6, row_7, row_8
    row_1 = [board[0],board[1],board[2]]
    row_2 = [board[3],board[4],board[5]]
    row_3 = [board[6],board[7],board[8]]
    row_4 = [board[0], board[3], board[6]]
    row_5 = [board[1], board[4], board[7]]
    row_6 = [board[2], board[5], board[8]]
    row_7 = [board[0],board[4],board[8]]
    row_8 = [board[2],board[4],board[6]]


def show_board():
    print(row_1)
    print(row_2)
    print(row_3)

def pc_turn():
    global c
    sum_of_all = [sum(row_1),sum(row_2),sum(row_3),sum(row_4),sum(row_5),sum(row_6),sum(row_7),sum(row_8)]
    len_sum_of_all = int(len(sum_of_all))
    c = 1
    for c in range(len_sum_of_all):
        if sum_of_all[7] == 8:
            if board[2] == 0:
                board[2] = 4
                update_board()
                return
            elif board[4] == 0:
                board[4] = 4
                update_board()
                return
            else:
                board[6] = 4
                update_board()
                return
        if sum_of_all[6] == 8:
            if board[0] == 0:
                board[0] = 4
                update_board()
                return
            elif board[4] == 0:
                board[4] = 4
                update_board()
                return
            else:
                board[8] = 4
                update_board()
                return
        # Rows
        if sum_of_all[5] == 8:
            if board[2] == 0:
                board[2] = 4
                update_board()
                return
            elif board[5] == 0:
                board[5] = 4
                update_board()

                return
            else:
                board[8] = 4
                update_board()
                return
        if sum_of_all[4] == 8:
            if board[1] == 0:
                board[1] = 4
                update_board()
                return
            elif board[4] == 0:
                board[4] = 4
                update_board()
                return
            else:
                board[7] = 4
                update_board()
                return
        if sum_of_all[3] == 8:
            if board[0] == 0:
                board[0] = 4
                update_board()
                return
            elif board[3] == 0:
                board[3] = 4
                update_board()
                return
            else:
                board[6] = 4
                update_board()
                return
        # coll
        if sum_of_all[c-1] == 8:
            if board[c - 1] == 0:
                board[i - 1] = 4
                update_board()
                return
            elif board[c] == 0:
                board[c] = 4
                update_board()
                return
            else:
                board[c + 1] = 4
                update_board()
                return

        for i in range(len_sum_of_all):
            # Rows
            if sum_of_all[5] == 2:
                if board[2] == 0:
                    board[2] = 4
                    update_board()
                    return
                elif board[5] == 0:
                    board[5] = 4
                    update_board()
                    return
                else:
                    board[8] = 4
                    update_board()
                    return
            if sum_of_all[4] == 2:
                if board[1] == 0:
                    board[1] = 4
                    update_board()
                    return
                elif board[4] == 0:
                    board[4] = 4
                    update_board()
                    return
                else:
                    board[7] = 4
                    update_board()
                    return
            if sum_of_all[3] == 2:
                if board[0] == 0:
                    board[0] = 4
                    update_board()
                    return
                elif board[3] == 0:
                    board[3] = 4
                    update_board()
                    return
                else:
                    board[6] = 4
                    update_board()
                    return

            if sum_of_all[7] == 2:
                if board[2] == 0:
                    board[2] = 4
                    update_board()
                    return
                elif board[4] == 0:
                    board[4] = 4
                    update_board()
                    return
                else:
                    board[6] = 4
                    update_board()
                    return
            if sum_of_all[6] == 2:
                if board[0] == 0:
                    board[0] = 4
                    update_board()
                    return
                elif board[4] == 0:
                    board[4] = 4
                    update_board()
                    return
                else:
                    board[8] = 4
                    update_board()
                    return
            if sum_of_all[i-1] == 2:
                if board[i-1] == 0:
                    board[i - 1] = 4
                    update_board()
                    return
                elif board[i] == 0:
                    board[i] = 4
                    update_board()
                    return
                else:
                    board[i+1] = 4
                    update_board()
                    return
        for i in range(len_sum_of_all):
            # Rows
            if sum_of_all[5] == 1:
                if board[2] == 0:
                    board[2] = 4
                    update_board()
                    return
                elif board[5] == 0:
                    board[5] = 4
                    update_board()
                    return
                else:
                    board[8] = 4
                    update_board()
                    return
            if sum_of_all[4] == 1:
                if board[1] == 0:
                    board[1] = 4
                    update_board()
                    return
                elif board[4] == 0:
                    board[4] = 4
                    update_board()
                    return
                else:
                    board[7] = 4
                    update_board()
                    return
            if sum_of_all[3] == 1:
                if board[0] == 0:
                    board[0] = 4
                    update_board()
                    return
                elif board[3] == 0:
                    board[3] = 4
                    update_board()
                    return
                else:
                    board[6] = 4
                    update_board()
                    return


            if sum_of_all[i - 1] == 1:
                if sum_of_all[7] == 1:
                    if board[2] == 0:
                        board[2] = 4

                        update_board()
                        return
                    elif board[4] == 0:
                        board[4] = 4

                        update_board()
                        return
                    else:
                        board[6] = 4

                        update_board()
                        return
                if sum_of_all[6] == 1:
                    if board[0] == 0:
                        board[0] = 4

                        update_board()
                        return
                    elif board[4] == 0:
                        board[4] = 4

                        update_board()
                        return
                    else:
                        board[8] = 4
                        update_board()

                        return
                if board[i - 1] == 0:
                    board[i - 1] = 4
                    update_board()
                    return
                elif board[i] == 0:
                    board[i] = 4
                    update_board()
                    return
                else:
                    board[i + 1] = 4
                    update_board()
                    return
        for i in range(len_sum_of_all):
            # Rows
            if sum_of_all[5] == 5:
                if board[2] == 0:
                    board[2] = 4
                    update_board()
                    return
                elif board[5] == 0:
                    board[5] = 4
                    update_board()
                    return
                else:
                    board[8] = 4
                    update_board()
                    return
            if sum_of_all[4] == 5:
                if board[1] == 0:
                    board[1] = 4
                    update_board()
                    return
                elif board[4] == 0:
                    board[4] = 4
                    update_board()
                    return
                else:
                    board[7] = 4
                    update_board()
                    return
            if sum_of_all[3] == 5:
                if board[0] == 0:
                    board[0] = 4
                    update_board()
                    return
                elif board[3] == 0:
                    board[3] = 4
                    update_board()
                    return
                else:
                    board[6] = 4
                    update_board()
                    return

            if sum_of_all[i - 1] == 5:
                if sum_of_all[7] == 1:
                    if board[2] == 0:
                        board[2] = 4

                        update_board()
                        return
                    elif board[4] == 0:
                        board[4] = 4
                        update_board()
                        return
                    else:
                        board[6] = 4

                        update_board()
                        return
                if sum_of_all[6] == 5:
                    if board[0] == 0:
                        board[0] = 4

                        update_board()
                        return
                    elif board[4] == 0:
                        board[4] = 4

                        update_board()
                        return
                    else:
                        board[8] = 4

                        update_board()
                        return
            if sum_of_all[i - 1] == 5:
                if board[i - 1] == 0:
                    board[i - 1] = 4
                    update_board()
                    return
                elif board[i] == 0:
                    board[i] = 4
                    update_board()
                    return
                else:
                    board[i + 1] = 4
                    update_board()
                    return


def test_if_gameover():
    if sum(row_1) == goal_a or sum(row_2) == goal_a or sum(row_3) == goal_a  or sum(row_4) == goal_a  or sum(row_5) == goal_a  or sum(row_6) == goal_a  or sum(row_7) == goal_a  or sum(row_8) == goal_a:
        print("Player Wins")
        quit()
    if sum(row_1) == 12 or sum(row_2) == 12 or sum(row_3) == 12  or sum(row_4) == 12  or sum(row_5) == 12  or sum(row_6) == 12  or sum(row_7) == 12  or sum(row_8) == 12:
        print("Computer Wins")
        quit()

def play():
    global board
    ans = int(input('Where to place'))
    if board[ans-1] > 0:
        print('Invaild')
        play()
    else:
        board[ans-1] = a
        update_board()
        test_if_gameover()
        pc_turn()
        show_board()
        test_if_gameover()
        play()

play()