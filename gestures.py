ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"
SPOCK = "spock"
LIZARD = "lizard"

GESTURES = [ROCK, SCISSORS, PAPER, SPOCK, LIZARD]

# map keyed by gestures and a list of gestures that they win against.
# i.e. ROCK wins against SCISSORS
# and SPOCK wins against SCISSORS or LIZARD
WINNING_GESTURES = {
    ROCK: [SCISSORS, LIZARD],
    SCISSORS: [PAPER, LIZARD],
    PAPER: [ROCK, SPOCK],
    SPOCK: [SCISSORS, ROCK],
    LIZARD: [SPOCK, PAPER]
}