

class Utility:

    def __init__(self, deck_size):
        pass

    def create_deck(self):

        deck_options = {
            24 : {},
            32 : {},
            36 : {}

        }



    def shuffle_deck(self):
        pass


    def initialize_game(self):

        self.shuffle_deck()
    


class Player(Utility):

    def __init__(self, cards, partnerID):
        # stuff
        self.cards = cards

    def __call__(self, cards):
        self.cards = cards

    def shuffle(self):
        #shuffle the cards
        pass

    def submits_card(self, suit):
        pass

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        

from enum import Enum
class Suit(Enum):
    spade = 1
    club = 2
    heart = 3
    diamond = 4
