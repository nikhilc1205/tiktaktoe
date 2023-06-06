import random


def play_game(player):
    list_player = ["X", "O"]
    if list_player[0] == player:
        non_player = list_player[1]
    else:
        non_player = list_player[0]
    board = ["" for i in range(9)]
    for i in range(9):
        if random.choice(list_player) == player:
            board[i] = player
        else:
            board[i] = non_player

    return board

    # goal=random.choice([0,1])
    # if goal==1:
    #     return player
    # else:
    #     return non_player
    # return [player for _ in range(9) if random.choice(list_player)==player else list_player.remove(player)]


print(play_game("X"))
