import random


class Hopper:
    def __init__(self, values):
        self._hopper = list(values)

    def draw(self):
        b = random.choice(self._hopper)
        self._hopper.remove(b)
        return b


def main():
    white_hopper = Hopper(range(1, 70))
    red_hopper = Hopper(range(1, 27))
    wb1 = white_hopper.draw()
    wb2 = white_hopper.draw()
    wb3 = white_hopper.draw()
    wb4 = white_hopper.draw()
    wb5 = white_hopper.draw()
    rb = red_hopper.draw()
    print('Picks:', wb1, wb2, wb3, wb4, wb5, rb)


main()

