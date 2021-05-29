import random
from Classes.Card import Card


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.txt()

    def build(self):
        self.cards = []
        for m in ["Clubs", "Spades", "Hearts", "Diamonds"]:
            for v in range(1, 14):
                self.cards.append(Card(m, v))

    # Converts deck to numeric values
    def num(self):
        for c in self.cards:
            c.num()

    # Converts deck to text values
    def txt(self):
        for c in self.cards:
            c.txt()

    def shuffle(self):
        res = []
        while len(self.cards) > 0:
            var = random.randint(0, len(self.cards) - 1)
            res.append(self.cards[var])
            del self.cards[var]
        self.cards = res
