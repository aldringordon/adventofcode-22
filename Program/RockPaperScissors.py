# The score for a single round is the score for the shape you selected
# (1 for Rock, 2 for Paper, and 3 for Scissors)
# plus the score for the outcome of the round
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# [THEM, ME]

ROCK="ROCK"
PAPER="PAPER"
SCISS="SCISSORS"

WIN="WIN"
DRAW="DRAW"
LOSS="LOSS"

CODE = { "A": ROCK, "B": PAPER, "C": SCISS, "X": LOSS, "Y": DRAW, "Z": WIN}
SCORE = { ROCK: 1, PAPER: 2, SCISS: 3, LOSS: 0, DRAW: 3, WIN: 6}

class RockPaperScissors():

    def __init__(self):
        self.guide = []

    def read_data(self, filename):
        self.guide = []
        f = open(filename, "r")
        for l in f:
            if l.strip():
                self.guide.append((l[0], l[2]))
        f.close()
    
    def find_move(self, them, outcome):
        movesIdx = {ROCK: 0, PAPER: 1, SCISS: 2}
        moves = [ROCK, PAPER, SCISS]

        if CODE[outcome] == DRAW:
            return CODE[them]

        themIdx = movesIdx[CODE[them]]
        if CODE[outcome] == LOSS:
            return moves[themIdx - 1]
        else:
            return moves[(themIdx + 1) % len(moves)]
    
    def outcome_score(self, them, me):
        move = self.find_move(them, me)
        return SCORE[move] + SCORE[CODE[me]]

    def calc_score(self):
        return sum([self.outcome_score(x[0], x[1]) for x in self.guide])