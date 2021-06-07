import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import pyqtSlot

from Classes.Participant import Participant
from Classes.Deck import Deck


# from main.py import hit, stand


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Black Jack'
        self.left = 100
        self.top = 100
        self.width = 980
        self.height = 620
        self.playerhand = []
        self.househand = []
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

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

        self.house1 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.house1.setPixmap(pixmap)
        self.house1.move(300, 295)
        self.househand.append(self.house1)

        self.house2 = QLabel(self)
        pixmap = QPixmap('./PNG/back.png')
        self.house2.setPixmap(pixmap)
        self.house2.move(500, 295)
        self.househand.append(self.house2)

        self.start_button = QPushButton('Press me to start', self)
        self.start_button.move(425, 580)
        self.start_button.resize(130, 25)
        self.start_button.clicked.connect(lambda: self.startgame())

        self.show()

    def startgame(self):
        self.start_button.deleteLater()

        self.hit_button = QPushButton('Hit', self)
        self.hit_button.move(345, 580)
        self.hit_button.resize(90, 25)
        self.hit_button.clicked.connect(lambda: hit(player, house, deck, ex))
        self.hit_button.show()

        self.stand_button = QPushButton('Stand', self)
        self.stand_button.move(545, 580)
        self.stand_button.resize(90, 25)
        self.stand_button.clicked.connect(lambda: stand(player, house, deck, ex))
        self.stand_button.show()

        prep()

    # Change imag of a label
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

    # Endgame function
    def enddial(self, result):
        msg = self.MessageBox(result, self)
        res = msg.exec()
        if res == QMessageBox.Yes:
            print('yes')
        elif res == QMessageBox.No:
            print('no')

    # Endgame dialog class
    class MessageBox(QMessageBox):
        def __init__(self, result, parent=None):
            super().__init__(parent)
            self.setWindowTitle('Result')
            self.setText(f'{result}\nWanna play again?')
            self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            self.setDefaultButton(QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    ex = App()
    sys.exit(app.exec_())
