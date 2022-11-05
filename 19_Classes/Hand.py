class Hand:
    def __init__(self, card1, card2):
        self._cards = []
        self._cards.append(card1)
        self._cards.append(card2)

    def add_card(self, card):
        self._cards.append(card)

    def has_hidden_card(self):
        for card in self._cards:
            if not card.is_face_up():
                return True
        return False

    def flip(self):
        for card in self._cards:
            if not card.is_face_up():
                card.flip()

    def get_card_count(self):
        return len(self._cards)

    def get_point_value(self):
        point_values = []
        for card in self._cards:
            if card.is_face_up():
                point_value = card.get_point_value()
                if len(point_value) == 1:
                    point_values.append(point_value[0])
                else:
                    point_values.append(point_value)
            else:
                point_values.append('?')
        if self.has_hidden_card():
            return point_values
        simple_point_sum = 0
        for point_value in point_values:
            if type(point_value) is list:
                return point_values
            else:
                simple_point_sum += int(point_value)
        return [simple_point_sum]

    def is_bust(self):
        point_value = self.get_point_value()
        if len(point_value) == 1:
            return point_value[0] > 21
        else:
            return None

    def is_win(self):
        point_value = self.get_point_value()
        if len(point_value) == 1:
            return point_value[0] == 21
        else:
            return None

    def __str__(self):
        hand = f'Point value: {str(self.get_point_value())}\n'
        for card in self._cards:
            hand += str(card) + '\n'
        if self.is_bust():
            hand += "bust\n"
        if self.is_win():
            hand += "win\n"
        return hand
