class Card:
    def __init__(self, mark, value):
        self.mark = mark
        self.value = value

    # Converts card to numeric value
    def num(self):
        if self.value == "Ace":
            self.value = 1
        elif self.value == "Jack":
            self.value = 11
        elif self.value == "Queen":
            self.value = 12
        elif self.value == "King":
            self.value = 13

    # Converts card to text value
    def txt(self):
        if self.value == 1:
            self.value = "Ace"
        elif self.value == 11:
            self.value = "Jack"
        elif self.value == 12:
            self.value = "Queen"
        elif self.value == 13:
            self.value = "King"

    def name(self):
        return f"{self.value} of {self.mark}"