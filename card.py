from enum import Enum
class Suit(Enum):
    spade = 1
    club = 2
    heart = 3
    diamond = 4

class Card:

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __call__(self, card):
        self.suit = card.suit
        self.number = card.number
    
    def get_suit(self):
        return self.suit

    def get_number(self):
        return self.number
