score = 0

moves = {
    "A": {"name": "Rock", "score": 1, "win": "B", "lose": "C", "draw": "A"},  # Rock
    "B": {"name": "Paper", "score": 2, "win": "C", "lose": "A", "draw": "B"},  # Paper
    "C": {"name": "Scissors", "score": 3, "win": "A", "lose": "B", "draw": "C"},  # Sci
}

results = {
    "X": {"name": "lose", "score": 0},
    "Y": {"name": "draw", "score": 3},
    "Z": {"name": "win", "score": 6},
}

with open("strategy.txt", "r") as strat:
    while True:
        turn = strat.readline()
        print(turn)
        if not turn:
            break
        if turn == "\n":
            continue
        input = turn.split()
        op = input[0]
        res = input[1]
        print(
            "{} wanting to {} I pick {}".format(
                moves[op]["name"],
                results[res]["name"],
                moves[moves[op][results[res]["name"]]]["name"],
            )
        )
        score += results[res]["score"] + moves[moves[op][results[res]["name"]]]["score"]


print("total: {}".format(score))
