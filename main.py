import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from Classes.Participant import Participant
from Classes.Deck import Deck


# Handle GUI
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Black Jack'
        self.left = 100
        self.top = 100
        self.width = 1380
        self.height = 620
        self.playerhand = []
        self.househand = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowIcon(QIcon('.\PNG\icon.png'))

        # Create widgets
        self.player1 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player1.setPixmap(pixmap)
        self.playerhand.append(self.player1)

        self.player2 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player2.setPixmap(pixmap)
        self.player2.move(200, 0)
        self.playerhand.append(self.player2)

        self.player3 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player3.setPixmap(pixmap)
        self.player3.move(400, 0)
        self.playerhand.append(self.player3)

        self.player4 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player4.setPixmap(pixmap)
        self.player4.move(600, 0)
        self.playerhand.append(self.player4)

        self.player5 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player5.setPixmap(pixmap)
        self.player5.move(800, 0)
        self.playerhand.append(self.player5)

        self.player6 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player6.setPixmap(pixmap)
        self.player6.move(1000, 0)
        self.playerhand.append(self.player5)

        self.player7 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.player7.setPixmap(pixmap)
        self.player7.move(1200, 0)
        self.playerhand.append(self.player5)

        self.house1 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.house1.setPixmap(pixmap)
        self.house1.move(490, 295)
        self.househand.append(self.house1)

        self.house2 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.house2.setPixmap(pixmap)
        self.house2.move(710, 295)
        self.househand.append(self.house2)

        self.start_button = QPushButton('Press me to start', self)
        self.start_button.move(625, 580)
        self.start_button.resize(130, 25)
        self.start_button.clicked.connect(lambda: self.startgame())

        self.show()

    # Start game func
    def startgame(self):
        self.start_button.deleteLater()

        self.hit_button = QPushButton('Hit', self)
        self.hit_button.move(535, 580)
        self.hit_button.resize(90, 25)
        self.hit_button.clicked.connect(lambda: hit())
        self.hit_button.show()

        self.stand_button = QPushButton('Stand', self)
        self.stand_button.move(755, 580)
        self.stand_button.resize(90, 25)
        self.stand_button.clicked.connect(lambda: stand())
        self.stand_button.show()

        prep()

    # Change image of a label
    @pyqtSlot()
    def change_label(self, label, card):
        pixmap = QPixmap(f'./PNG/{card}.png')
        label.setPixmap(pixmap)

    # Set all cards in GUI to cardbacks
    def clear(self):
        for label in self.playerhand:
            self.change_label(label, 'back')
        for label in self.househand:
            self.change_label(label, 'back')

    def enddial(self, result):
        msg = self.MessageBox(result, self)
        res = msg.exec()
        if res == QMessageBox.Yes:
            self.clear()
            prep()
        elif res == QMessageBox.No:
            sys.exit()

    # Endgame dialog subclass
    class MessageBox(QMessageBox):
        def __init__(self, result, parent=None):
            super().__init__(parent)
            self.setWindowTitle('Result')
            self.setText(f'{result}\nWanna play again?')
            self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.setDefaultButton(QMessageBox.Yes)


# Check if someone won
def check(player, house):
    if player.count == 21 or house.count > 21:
        ex.enddial('You won!')
        return True
    if player.count > 21 or house.count == 21:
        ex.enddial('You lost...')
        return True
    return False


# Choose a winner
def end(player, house):
    if check(player, house):
        return None
    if player.count > house.count:
        ex.enddial('You won!')
        return None
    if player.count < house.count:
        ex.enddial('You lost...')
        return None
    ex.enddial("It's a draw!")


def hit():
    player.draw(deck, ex)
    check(player, house)


def stand():
    house.draw(deck, ex)
    end(player, house)


# Prepare for new game
def prep():
    global deck, player, house
    deck = Deck()
    deck.shuffle()
    player = Participant('player')
    house = Participant('house')
    player.draw(deck, ex)
    house.draw(deck, ex)
    player.draw(deck, ex)
    check(player, house)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())
