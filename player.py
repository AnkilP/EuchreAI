class player:

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

    