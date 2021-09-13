from gestures import GESTURES
from player import Player


class Human(Player):

    # what is has
    def __init__(self):
        Player.__init__(self)

    def select_gesture(self):
        raw_user_input = input("Please enter a gesture from list: " + str(GESTURES))
        user_input = raw_user_input.lower()  # make lower case because all GESTURES are lowercase

        if user_input not in GESTURES:
            print("Entry invalid. Please Try again")
            return self.select_gesture()

        return user_input
