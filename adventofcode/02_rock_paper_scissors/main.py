import re


def game(opponent, you):
    opponent_hand = ["A", "B", "C"]
    your_hand = ["X", "Y", "Z"]
    won = [1, -2]

    shape_score = your_hand.index(you) + 1
    game_spread = your_hand.index(you) - opponent_hand.index(opponent)
    if game_spread in won:
        game_score = 6
    elif game_spread == 0:
        game_score = 3
    else:
        game_score = 0

    return shape_score + game_score


print(game("A", "Y"))

score = 0

with open("strategy.txt", "r") as strat:
    while True:
        turn = strat.readline()
        print(turn)
        if not turn:
            break
        if turn == "\n":
            continue
        moves = turn.split()
        score += game(moves[0], moves[1])


print("total: {}".format(score))
