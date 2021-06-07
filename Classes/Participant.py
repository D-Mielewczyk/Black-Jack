class Participant:
    def __init__(self, name):
        self.hand = []
        self.count = 0
        self.name = name

    # Draw card while adding its value to keep track of the score
    def draw(self, deck, App):
        self.count += points(deck.cards[0].value, self.count)
        self.hand.append(deck.cards[0])
        # Show card in GUI
        if self.name == 'player':
            App.change_label(App.playerhand[len(self.hand) - 1], deck.cards[0].name())
        elif self.name == 'house':
            App.change_label(App.househand[len(self.hand) - 1], deck.cards[0].name())
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
