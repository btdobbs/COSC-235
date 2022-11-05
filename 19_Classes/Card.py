ACE = 1
JACK = 11
QUEEN = 12
KING = 13

CLUBS = 'Clubs'
DIAMONDS = 'Diamonds'
HEARTS = 'Hearts'
SPADES = 'Spades'

FACE_UP = True
FACE_DOWN = False

RANKS = (ACE, 2, 3, 4, 5, 6, 7, 8, 9, 10, JACK, QUEEN, KING)
SUITS = (CLUBS, DIAMONDS, HEARTS, SPADES)


class Card:
    def __init__(self, rank, suit, is_face_up):
        self._rank = rank
        self._suit = suit
        self._is_face_up = is_face_up

    def flip(self):
        self._is_face_up = not self._is_face_up

    def is_face_up(self):
        return self._is_face_up

    def get_rank(self):
        return self._rank

    def get_suit(self):
        return self._suit

    def get_point_value(self):
        if self.get_rank() in [JACK, QUEEN, KING]:
            return [10]
        if self.get_rank() == ACE:
            return [1, 11]
        return [self.get_rank()]

    def __str__(self):
        if not self.is_face_up():
            return '###'
        rank_names = ('Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen',
                      'King')
        return f'{rank_names[self.get_rank() - 1]} of {self.get_suit()}'
