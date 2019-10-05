import table
import card

class Game:

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.suits = []

    def decide_trump(self):
        while True:
            for suit in self.suits:
                yield suit