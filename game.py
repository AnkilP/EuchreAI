from __future__ import absolute_import
from table import Table
from card import Card

class Game:

    def __init__(self, number_of_players):
        self.number_of_players = number_of_players
        self.tables = Table(next(self.decide_trump()))
        
    def decide_trump(self):
        while True:
            for suit in self.tables.suits:
                yield suit

    def next_turn(self):
        while True:
            self.index = self.index + 1
            yield self.index

    def decide_winner(self):
        return self.tables.winning_card