import random
import Card


class CardDeck:
    def __init__(self):
        self._cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self._cards.append(Card.Card(rank, suit, Card.FACE_DOWN))

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        return self._cards.pop()

    def is_empty(self):
        return len(self._cards) == 0
