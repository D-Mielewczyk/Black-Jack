class Participant:
    def __init__(self):
        self.hand = []
        self.count = 0

    # Draws card while adding its value to keep track of the score
    def draw(self, deck):
        self.count += points(deck.cards[0].value, self.count)
        self.hand.append(deck.cards[0])
        del deck.cards[0]


# Check the value of a card
def points(card, count):
    if type(card) == str or card > 10:
        return 10
    if card > 1:
        return card
    if count + 11 > 21:
        return 1
    return 11
