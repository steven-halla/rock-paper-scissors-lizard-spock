ROCK = "rock"
SCISSORS = "scissors"
PAPER = "paper"
SPOCK = "spock"
LIZARD = "lizard"

GESTURES = [ROCK, SCISSORS, PAPER, SPOCK, LIZARD]


WINNING_GESTURES = {
    ROCK: [SCISSORS, LIZARD],
    SCISSORS: [PAPER, LIZARD],
    PAPER: [ROCK, SPOCK],
    SPOCK: [SCISSORS, ROCK],
    LIZARD: [SPOCK, PAPER]
}