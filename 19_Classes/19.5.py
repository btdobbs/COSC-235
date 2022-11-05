import CardDeck
import Hand


def main():
    card_deck = CardDeck.CardDeck()
    card_deck.shuffle()
    card1 = card_deck.draw()
    card2 = card_deck.draw()
    card2.flip()
    hand = Hand.Hand(card1, card2)
    print(hand)
    hand.flip()
    print(hand)
    while not (hand.is_bust() or hand.is_win()) and (hand.get_card_count() < 10):
        hand.add_card(card_deck.draw())
        hand.flip()
        print(hand)


main()

