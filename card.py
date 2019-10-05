class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __call__(self, card):
        self.suit = card.suit
        self.number = card.number
