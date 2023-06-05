# import pdb

def pick_player():
    player = input("Enter Your Player: X or O")
    # breakpoint()
    # player+=player
    # breakpoint()
    # pdb.set_trace()
    if player in ["X", "O"]:
        return player
    else:
        raise ValueError("Please Provide X or O")


# print(pick_player())
if __name__=="__main__":
    pick_player()
    print("__name__ : ",__name__)
else:
    print("Someone Called Me")
    print("__name__ : ",__name__)