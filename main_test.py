import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *
import random


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)

        # main game items
        self.step = QtWidgets.QPushButton(self.centralwidget)
        self.step.setGeometry(QtCore.QRect(683, 140, 65, 56))
        self.step.setStyleSheet("border-image: url(:/figure/stepbott.png);")
        self.step.setText("")
        self.step.setObjectName("step")
        self.yelmoney = QtWidgets.QLabel(self.centralwidget)
        self.yelmoney.setGeometry(QtCore.QRect(240, 185, 71, 21))
        self.yelmoney.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 20pt \"appo paint\";")
        self.yelmoney.setText("")
        self.yelmoney.setObjectName("yelmoney")
        self.yelcash = QtWidgets.QLabel(self.centralwidget)
        self.yelcash.setGeometry(QtCore.QRect(240, 212, 71, 21))
        self.yelcash.setStyleSheet("border-image: url(:/game/white.png);\n"
                                   "font: 20pt \"appo paint\";")
        self.yelcash.setText("")
        self.yelcash.setObjectName("yelcash")
        self.yelhouse = QtWidgets.QLabel(self.centralwidget)
        self.yelhouse.setGeometry(QtCore.QRect(240, 240, 71, 21))
        self.yelhouse.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 20pt \"appo paint\";")
        self.yelhouse.setText("")
        self.yelhouse.setObjectName("yelhouse")
        self.yelname = QtWidgets.QLabel(self.centralwidget)
        self.yelname.setGeometry(QtCore.QRect(193, 156, 121, 21))
        self.yelname.setStyleSheet("border-image: url(:/game/white.png);\n"
                                   "font: 28pt \"appo paint\";")
        self.yelname.setText("")
        self.yelname.setObjectName("yelname")
        self.bluehouse = QtWidgets.QLabel(self.centralwidget)
        self.bluehouse.setGeometry(QtCore.QRect(239, 415, 71, 21))
        self.bluehouse.setStyleSheet("border-image: url(:/game/white.png);\n"
                                     "font: 20pt \"appo paint\";")
        self.bluehouse.setText("")
        self.bluehouse.setObjectName("bluehouse")
        self.bluename = QtWidgets.QLabel(self.centralwidget)
        self.bluename.setGeometry(QtCore.QRect(192, 331, 121, 21))
        self.bluename.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 28pt \"appo paint\";")
        self.bluename.setText("")
        self.bluename.setObjectName("bluename")
        self.bluecash = QtWidgets.QLabel(self.centralwidget)
        self.bluecash.setGeometry(QtCore.QRect(239, 387, 71, 21))
        self.bluecash.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 20pt \"appo paint\";")
        self.bluecash.setText("")
        self.bluecash.setObjectName("bluecash")
        self.bluemoney = QtWidgets.QLabel(self.centralwidget)
        self.bluemoney.setGeometry(QtCore.QRect(239, 360, 71, 21))
        self.bluemoney.setStyleSheet("border-image: url(:/game/white.png);\n"
                                     "font: 20pt \"appo paint\";")
        self.bluemoney.setText("")
        self.bluemoney.setObjectName("bluemoney")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(370, 310, 451, 151))
        self.info.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
                                "font: 40pt \"appo paint\"")
        self.info.setText("")
        self.info.setObjectName("info")
        self.stepnum = QtWidgets.QLabel(self.centralwidget)
        self.stepnum.setGeometry(QtCore.QRect(764, 142, 51, 51))
        self.stepnum.setStyleSheet("font: 40pt \"appo paint\";\n"
                                   "border-image: url(:/game/white.png);")
        self.stepnum.setText("Na")
        self.stepnum.setObjectName("stepnum")
        self.turn = QtWidgets.QLabel(self.centralwidget)
        self.turn.setGeometry(QtCore.QRect(764, 221, 51, 51))
        self.turn.setStyleSheet("font: 40pt \"appo paint\";\n"
                                "border-image: url(:/game/white.png);")
        self.turn.setText("1")
        self.turn.setObjectName("turn")

        self.player1 = QtWidgets.QLabel(self.centralwidget)
        self.player1.setGeometry(QtCore.QRect(10, 50, 41, 51))
        self.player1.setStyleSheet("border-image: url(:/figure/yellowman.png);")
        self.player1.setText("")
        self.player1.setObjectName("player1")

        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(60, 50, 41, 51))
        self.player2.setStyleSheet("border-image: url(:/figure/blueman.png);")
        self.player2.setText("")
        self.player2.setObjectName("player1_2")

        # main game set up
        self.hide_main_game()
        self.connect_buttons()

        # main game variables
        self.player_name1 = None
        self.player_name2 = None
        self.turn_count = 0

    def setName1(self, name):
        self.player_name1 = name

    def setName2(self, name):
        self.player_name2 = name

    def hide_cover(self):
        self.exit.hide()
        self.play.hide()

    def show_cover(self):
        self.exit.show()
        self.play.show()

    def hide_main_game(self):
        self.step.hide()
        self.turn.hide()
        self.yelcash.hide()
        self.yelmoney.hide()
        self.yelname.hide()
        self.yelhouse.hide()
        self.bluecash.hide()
        self.bluehouse.hide()
        self.bluemoney.hide()
        self.bluename.hide()
        self.info.hide()
        self.stepnum.hide()
        self.player1.hide()
        self.player2.hide()

    def show_main_game(self):
        self.step.show()
        self.turn.show()
        self.yelcash.show()
        self.yelmoney.show()
        self.yelname.show()
        self.yelhouse.show()
        self.bluecash.show()
        self.bluehouse.show()
        self.bluemoney.show()
        self.bluename.show()
        self.info.show()
        self.stepnum.show()
        self.player1.show()
        self.player2.show()

    def connect_buttons(self):
        self.play.clicked.connect(self.start)
        self.step.clicked.connect(self.roll)
        self.exit.clicked.connect(self.end)

    def start(self):
        self.graphicsView.setStyleSheet("border-image: url(:/figure/main_game_background.jpg);")
        self.hide_cover()
        self.show_main_game()
        # self.repaint()

    def roll(self):
        self.turn_count += 1
        self.turn.setText("{}".format(self.turn_count // 2 + 1))
        num = random.randint(1, 6)
        self.stepnum.setText("{}".format(num))
        self.repaint()

    def end(self):
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break




