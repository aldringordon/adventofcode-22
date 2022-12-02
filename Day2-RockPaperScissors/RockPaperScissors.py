# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# [THEM, ME]

# 8 1 6 = 15

# A ROCK
# B PAPER
# C SCISSORS

# X ROCK
# Y PAPER
# Z SCISSORS


ROCK="ROCK"
PAPER="PAPER"
SCISS="SCISSORS"

WIN="WIN"
DRAW="DRAW"
LOSS="LOSS"

def outcome(them, me):

    play = { "A": ROCK, "B": PAPER, "C": SCISS, "X": ROCK, "Y": PAPER, "Z": SCISS}

    score = { ROCK: 1, PAPER: 2, SCISS: 3, LOSS: 0, DRAW: 3, WIN: 6}

    print()
    print(them, me)

    them = play[them]
    me = play[me]

    outcome = LOSS

    # Draw
    if them == me:
        print(them, me)
        outcome = DRAW

    if them == ROCK:
        if me == PAPER:
            outcome = WIN

    if them == PAPER:
        if me == SCISS:
            outcome = WIN

    if them == SCISS:
        if me == ROCK:
            outcome = WIN
    
    print(outcome)
    return score[outcome] + score[me]

def read_data(filename):
    guide = []

    f = open(filename, "r")
    for l in f:
        if l.strip():
            guide.append((l[0], l[2]))

    f.close()
    return guide

def calc_score(guide):
    sum = 0
    for x in guide:
        them = x[0]
        me = x[1]
        sum = sum + outcome(them, me)

    return sum

if __name__=="__main__":

    guide = read_data("Data.txt")
    print(guide)

    score = calc_score(guide)

    print("score:")
    print(score)