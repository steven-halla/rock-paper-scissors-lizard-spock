from computer import Computer
from gestures import WINNING_GESTURES
from human import Human
from player import Player


class Game:

    def __init__(self):
        self.player = Player()
        self.player_1 = Human()
        self.player_2 = Computer()

    def start(self):
        self.set_player_2()
        self.display_rules()
        self.play()
        self.play_again()


    def set_player_2(self):
        players = input("Please select Single Player[1] or Multi-Player[2] Please Type: '1' or '2'.")
        if players == "1":
            self.player_2 = Computer()
        elif players == "2":
            self.player_2 = Human()
        else:
            return self.set_player_2()


    def display_rules(self):
        print("Welcome to Rock, Paper, Scissors, Lizard, Spock.")
        print("The rules of the game are:")
        print("Rock crushes Scissors")
        print("Scissors cut Paper")
        print("Paper covers Rock")
        print("Rock crushes Lizard")
        print("Lizard poisons Spock")
        print("Spock smashes Scissors")
        print("Scissors decapitate Lizard")

    def play(self):
        p1_score = 0
        p2_score = 0
        round = 1
        while p1_score < 2 and p2_score < 2:
            print("Round " + str(round) + " - " + str(p1_score) + " vs " + str(p2_score))

            print("Player 1's turn")
            p1_input = self.player_1.select_gesture()
            print("Player 1 picked: " + p1_input)

            print("Player 2's turn")
            p2_input = self.player_2.select_gesture()
            print("Player 2 picked: " + p2_input)

            result = self.evaluate_round(p1_input, p2_input)
            if result == 0:
                print("draw")
            elif result == 1:
                print("player 1 won")
                p1_score += 1
                round += 1
            elif result == 2:
                print("player 2 won")
                p2_score += 1
                round += 1

    def play_again(self):
        print("would you like to play again")

        please_continue = input("press 1 for yes 2 for no.")
        if please_continue == "1":
            self.play()
        elif please_continue == "2":
            print("ending game")
        else:
            self.play_again()


    def evaluate_round(self, p1_input, p2_input):
        # check if p1 wins
        if p2_input in WINNING_GESTURES[p1_input]:
            return 1
        # now check if p1 wins
        if p1_input in WINNING_GESTURES[p2_input]:
            return 2
        # must be a draw
        return 0

    def display_winnner(self):
        pass
