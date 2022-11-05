import random


class CubeDie:

    def __init__(self):
        self._top = 1

    def get_top(self):
        return self._top

    def roll(self):
        self._top = random.randint(1,6)

    def __str__(self):
        print("[",self._top,"]",sep="")
