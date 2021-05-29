import sys
from Classes.Participant import Participant
from Classes.Deck import Deck


# Print situation on board
def show(player, house):
    print("Your cards are:")
    res = []
    for c in player.hand:
        res.append(f"{c.value} of {c.mark}")
    print(res)
    print("\nEnemy cards are:")
    res = []
    for c in house.hand:
        res.append(f"{c.value} of {c.mark}")
    print(res)


# Check if someone won
def check(player, house):
    if player.count == 21 or house.count > 21:
        return "\nYou won!"
    if player.count > 21 or house.count == 21:
        return "\nYou lost!"
    return False


# Choosing a winner
def end(player, house):
    if check(player, house):
        return check(player, house)
    if player.count > house.count:
        return "You won!"
    if player.count < house.count:
        return "You lost!"
    return "draw!"


def turn(player, house, deck):
    while True:
        print("\n#############################\n")
        show(player, house)
        if check(player, house):
            print(check(player, house))
            sys.exit()
        if input("h - hit, s - stand") == "s":
            house.draw(deck)
            print("\n#############################\n")
            show(player, house)
            if check(player, house):
                print(check(player, house))
            else:
                print(end(player, house))
            sys.exit()
        player.draw(deck)


def main():
    deck = Deck()
    deck.shuffle()
    player = Participant()
    house = Participant()
    player.draw(deck)
    house.draw(deck)
    player.draw(deck)
    turn(player, house, deck)
    pass


if __name__ == "__main__":
    main()
