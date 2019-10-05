from card import Card as card

class Table:

    def __init__(self, trump):
        self.central_cards = []

    def recieve_cards(self, player_card):
        #update suit
        self.who_s_winning(player_card)
        self.central_cards.append(player_card.suit)

    def who_s_winning(self, player_card):
        if len(self.central_cards)== 0:
            self.winning_card = Card(null)
        else:

