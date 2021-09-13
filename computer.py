from gestures import GESTURES
from player import Player
import random


class Computer(Player):

    def __init__(self):
        Player.__init__(self)

    def select_gesture(self):
        return random.choice(GESTURES)

