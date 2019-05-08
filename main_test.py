import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QRect
from test import *
import random
from chat_utils import *
import json


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, s, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.s = s
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
        self.player1.setGeometry(QtCore.QRect(10, 55, 41, 51))
        self.player1.setStyleSheet("border-image: url(:/figure/yellowman.png);")
        self.player1.setText("")
        self.player1.setObjectName("player1")

        self.player2 = QtWidgets.QLabel(self.centralwidget)
        self.player2.setGeometry(QtCore.QRect(60, 55, 41, 51))
        self.player2.setStyleSheet("border-image: url(:/figure/blueman.png);")
        self.player2.setText("")
        self.player2.setObjectName("player2")

        # main game set up
        self.hide_main_game()
        self.connect_buttons()

        # main game variables
        self.bdposition = [[60, 55], [150, 55], [270, 55], [360, 55], [480, 55], [580, 55], [680, 55], [780, 55],
                           [900, 55], [900, 150], [900, 245], [900, 340], [900, 445], [900, 550],
                           [780, 550], [680, 550], [580, 550], [480, 550], [360, 550], [270, 550],
                           [150, 550], [60, 550], [60, 445], [60, 340], [60, 245], [60, 150]]
        self.player_name1 = None
        self.player_name2 = None
        self.player1_count = 0
        self.player2_count = 0
        self.turn_count = 0

        #
        self.anim1 = QPropertyAnimation(self.player1, b"geometry")
        self.anim1.setDuration(1000)
        self.anim2 = QPropertyAnimation(self.player2, b"geometry")
        self.anim2.setDuration(1000)

    def turn(self):
        return self.player_name1 if self.turn_count % 2 == 0 else self.player_name2

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
        d = {"action": "gaming", "update": "start"}
        mysend(self.s, json.dumps(d))
        self.graphicsView.setStyleSheet("border-image: url(:/figure/main_game_background.jpg);")
        self.hide_cover()
        self.show_main_game()
        # self.repaint()

    def roll(self):
        if self.anim1.state() != self.anim1.Running and self.anim2.state() != self.anim2.Running:
            num = random.randint(1, 6)
            if self.turn_count % 2 == 0:
                curr_x, curr_y = self.bdposition[self.player1_count]
                next_count = (self.player1_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player1_count = next_count
                self.anim1.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim1.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim1.start()
            else:
                curr_x, curr_y = self.bdposition[self.player2_count]
                next_count = (self.player2_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player2_count = next_count
                self.anim2.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim2.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim2.start()
            self.step.setEnabled(False)
            d = {"action": "gaming", "update": "roll", "num": num}
            mysend(self.s, json.dumps(d))
            self.turn.setText("{}".format(self.turn_count // 2 + 1))
            self.turn_count += 1

    def update_board(self, msg):
        if msg["update"] == "roll":
            num = msg["num"]
            if self.turn_count % 2 == 0:
                curr_x, curr_y = self.bdposition[self.player1_count]
                next_count = (self.player1_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player1_count = next_count
                self.anim1.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim1.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim1.start()
            else:
                curr_x, curr_y = self.bdposition[self.player2_count]
                next_count = (self.player2_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player2_count = next_count
                self.anim2.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim2.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim2.start()
            self.step.setEnabled(True)
            self.turn.setText("{}".format(self.turn_count // 2 + 1))
            self.turn_count += 1
        elif msg["update"] == "start":
            self.graphicsView.setStyleSheet("border-image: url(:/figure/main_game_background.jpg);")
            self.hide_cover()
            self.show_main_game()
            self.step.setEnabled(False)
        elif msg["update"] == "stop":
            self.hide()

    def end(self):
        d = {"action": "gaming", "update": "stop"}
        mysend(self.s, json.dumps(d))
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow(None)
    app.startingUp()
    myWin.show()

    while True:
        app.processEvents()
        if myWin.isHidden():
            app.exit()
            break




