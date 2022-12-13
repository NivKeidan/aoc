ROCK = "r"
PAPER = "p"
SCISSORS = "s"
WIN = "Z"
DRAW = "Y"
LOSE = "X"

trans_op={}
trans_op["A"] = ROCK
trans_op["B"] = PAPER
trans_op["C"] = SCISSORS

# trans_result={}
# trans_you["X"] = ROCK
# trans_you["Y"] = PAPER
# trans_you["Z"] = SCISSORS

def score_selection(s):
    if s == ROCK:
        return 1
    if s == PAPER:
        return 2
    if s == SCISSORS:
        return 3
    raise Exception("score scelection: %s", s)

def get_result(op, you):
    if op == you:
        return DRAW
    if op == ROCK and you == PAPER:
        return WIN
    if op == PAPER and you == SCISSORS:
        return WIN
    if op == SCISSORS and you == ROCK:
        return WIN
    return LOSE

def get_round_score(op, you):
    score = score_selection(you)
    result = get_result(op, you)
    if result == WIN:
        score += 6
    elif result == DRAW:
        score += 3
    return score

def get_you(op, result):
    if result == DRAW:
        return op
    if result == WIN:
        if op == SCISSORS:
            return ROCK
        if op == ROCK:
            return PAPER
        if op == PAPER:
            return SCISSORS
    if result == LOSE:
        if op == SCISSORS:
            return PAPER
        if op == ROCK:
            return SCISSORS
        if op == PAPER:
            return ROCK
    raise Exception("uknown result %s", result)

    
total_score = 0    
with open('inp1') as f:
    for i, l in enumerate(f.readlines()):
        l = l.strip()
        oponent, result = l.split(" ")
        oponent = trans_op[oponent]
        you = get_you(oponent, result)
        total_score += get_round_score(oponent, you)
print(total_score)