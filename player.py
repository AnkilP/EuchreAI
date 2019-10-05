from card import Card as card

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
