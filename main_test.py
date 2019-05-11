import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5.QtCore import QPropertyAnimation, QRect
from Building import Building, Player
from test import *
from bursar import *
import random
from chat_utils import *
import json


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, s, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.s = s
        self.bursar_window = QDialog()
        self.bursar_dialog = Ui_Dialog()
        self.bursar_dialog.setupUi(self.bursar_window)
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
        self.yelname.setGeometry(QtCore.QRect(233, 156, 121, 21))
        self.yelname.setStyleSheet("border-image: url(:/game/white.png);\n"
                                   "font: 20pt \"appo paint\";")
        self.yelname.setText("")
        self.yelname.setObjectName("yelname")
        self.bluehouse = QtWidgets.QLabel(self.centralwidget)
        self.bluehouse.setGeometry(QtCore.QRect(239, 415, 71, 21))
        self.bluehouse.setStyleSheet("border-image: url(:/game/white.png);\n"
                                     "font: 20pt \"appo paint\";")
        self.bluehouse.setText("")
        self.bluehouse.setObjectName("bluehouse")
        self.bluename = QtWidgets.QLabel(self.centralwidget)
        self.bluename.setGeometry(QtCore.QRect(233, 331, 121, 21))
        self.bluename.setStyleSheet("border-image: url(:/game/white.png);\n"
                                    "font: 20pt \"appo paint\";")
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
        self.info.setGeometry(QtCore.QRect(370, 351, 451, 41))
        self.info.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
                                "font: 18pt \"appo paint\"")
        self.info.setText("")
        self.info.setObjectName("info")
        self.buy_info = QtWidgets.QLabel(self.centralwidget)
        self.buy_info.setGeometry(QtCore.QRect(370, 390, 231, 71))
        self.buy_info.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
                                    "font: 18pt \"appo paint\"")
        self.buy_info.setText("")
        self.buy_info.setObjectName("buy_info")
        self.fate = QtWidgets.QLabel(self.centralwidget)
        self.fate.setGeometry(QtCore.QRect(370, 310, 451, 41))
        self.fate.setStyleSheet("border-image: url(:/game/infoframe.png);\n"
                                "font: 18pt \"appo paint\"")
        self.fate.setText("")
        self.fate.setObjectName("fate")
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

        self.player1 = Player(self.centralwidget)
        self.player1.set_name("alice")
        self.player1.initiate_color(1)
        self.player1.setGeometry(QtCore.QRect(10, 55, 41, 51))
        self.player1.setStyleSheet("border-image: url(:/figure/yellowman.png);")
        self.player1.setText("")
        self.player1.setObjectName("player1")

        self.player2 = Player(self.centralwidget)
        self.player2.set_name("bob")
        self.player2.initiate_color(2)
        self.player2.setGeometry(QtCore.QRect(60, 55, 41, 51))
        self.player2.setStyleSheet("border-image: url(:/figure/blueman.png);")
        self.player2.setText("")
        self.player2.setObjectName("player2")

        self.yes = QtWidgets.QPushButton(self.centralwidget)
        self.yes.setGeometry(QtCore.QRect(630, 410, 71, 31))
        self.yes.setStyleSheet("border-image: url(:/figure/yes.png);")
        self.yes.setText("")
        self.yes.setObjectName("yes")

        self.no = QtWidgets.QPushButton(self.centralwidget)
        self.no.setGeometry(QtCore.QRect(730, 410, 71, 31))
        self.no.setStyleSheet("border-image: url(:/figure/no.png);")
        self.no.setText("")
        self.no.setObjectName("no")

        # main game variables
        self.bdposition = [[60, 55], [150, 55], [270, 55], [360, 55], [480, 55], [580, 55], [680, 55], [780, 55],
                           [900, 55], [900, 140], [900, 235], [900, 335], [900, 445], [900, 550],
                           [780, 550], [680, 550], [580, 550], [480, 550], [360, 550], [270, 550],
                           [150, 550], [60, 550], [60, 445], [60, 335], [60, 235], [60, 150]]

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

        # buildings
        self.green_center = Building(self.centralwidget)
        self.green_center.setGeometry(QtCore.QRect(121, 105, 88, 15))
        self.green_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.green_center.setText("")
        self.green_center.setObjectName("green_center")
        self.public_safety = Building(self.centralwidget)
        self.public_safety.setGeometry(QtCore.QRect(209, 105, 103, 15))
        self.public_safety.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.public_safety.setText("")
        self.public_safety.setObjectName("public_safety")
        self.student_life = Building(self.centralwidget)
        self.student_life.setGeometry(QtCore.QRect(312, 105, 138, 15))
        self.student_life.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.student_life.setText("")
        self.student_life.setObjectName("student_life")
        self.Room110_Gallery = Building(self.centralwidget)
        self.Room110_Gallery.setGeometry(QtCore.QRect(450, 105, 103, 15))
        self.Room110_Gallery.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Room110_Gallery.setText("")
        self.Room110_Gallery.setObjectName("Room110_Gallery")
        self.mail_room = Building(self.centralwidget)
        self.mail_room.setGeometry(QtCore.QRect(553, 105, 100, 15))
        self.mail_room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mail_room.setText("")
        self.mail_room.setObjectName("mail_room")
        self.luckin = Building(self.centralwidget)
        self.luckin.setGeometry(QtCore.QRect(653, 105, 103, 15))
        self.luckin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.luckin.setText("")
        self.luckin.setObjectName("luckin")
        self.cafeteria = Building(self.centralwidget)
        self.cafeteria.setGeometry(QtCore.QRect(755, 105, 85, 15))
        self.cafeteria.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cafeteria.setText("")
        self.cafeteria.setObjectName("cafeteria")
        self.auditorium = Building(self.centralwidget)
        self.auditorium.setGeometry(QtCore.QRect(842, 200, 13, 92))
        self.auditorium.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.auditorium.setText("")
        self.auditorium.setObjectName("auditorium")
        self.the_box = Building(self.centralwidget)
        self.the_box.setGeometry(QtCore.QRect(842, 120, 13, 80))
        self.the_box.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.the_box.setText("")
        self.the_box.setObjectName("the_box")
        self.cafe = Building(self.centralwidget)
        self.cafe.setGeometry(QtCore.QRect(842, 292, 13, 92))
        self.cafe.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cafe.setText("")
        self.cafe.setObjectName("cafe")
        self.bursar = Building(self.centralwidget)
        self.bursar.setGeometry(QtCore.QRect(842, 384, 13, 92))
        self.bursar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.bursar.setText("")
        self.bursar.setObjectName("bursar")
        self.IT_center = Building(self.centralwidget)
        self.IT_center.setGeometry(QtCore.QRect(754, 480, 85, 15))
        self.IT_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.IT_center.setText("")
        self.IT_center.setObjectName("IT_center")
        self.library = Building(self.centralwidget)
        self.library.setGeometry(QtCore.QRect(651, 480, 103, 15))
        self.library.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.library.setText("")
        self.library.setObjectName("library")
        self.arc = Building(self.centralwidget)
        self.arc.setGeometry(QtCore.QRect(553, 480, 99, 15))
        self.arc.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.arc.setText("")
        self.arc.setObjectName("arc")
        self.advisor_office = Building(self.centralwidget)
        self.advisor_office.setGeometry(QtCore.QRect(452, 480, 101, 15))
        self.advisor_office.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.advisor_office.setText("")
        self.advisor_office.setObjectName("adviser_office")
        self.H_W_center = Building(self.centralwidget)
        self.H_W_center.setGeometry(QtCore.QRect(348, 480, 104, 15))
        self.H_W_center.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.H_W_center.setText("")
        self.H_W_center.setObjectName("H_W_center")
        self.CDC = Building(self.centralwidget)
        self.CDC.setGeometry(QtCore.QRect(208, 480, 140, 15))
        self.CDC.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.CDC.setText("")
        self.CDC.setObjectName("CDC")
        self.mac_lab = Building(self.centralwidget)
        self.mac_lab.setGeometry(QtCore.QRect(106, 480, 102, 15))
        self.mac_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.mac_lab.setText("")
        self.mac_lab.setObjectName("mac_lab")
        self.ally_lounge = Building(self.centralwidget)
        self.ally_lounge.setGeometry(QtCore.QRect(0, 480, 106, 15))
        self.ally_lounge.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ally_lounge.setText("")
        self.ally_lounge.setObjectName("ally_lounge")
        self.fos_lab = Building(self.centralwidget)
        self.fos_lab.setGeometry(QtCore.QRect(105, 387, 15, 94))
        self.fos_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.fos_lab.setText("")
        self.fos_lab.setObjectName("fos_lab")
        self.piano_room = Building(self.centralwidget)
        self.piano_room.setGeometry(QtCore.QRect(105, 293, 15, 94))
        self.piano_room.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.piano_room.setText("")
        self.piano_room.setObjectName("piano_room")
        self.ima_lab = Building(self.centralwidget)
        self.ima_lab.setGeometry(QtCore.QRect(105, 199, 15, 94))
        self.ima_lab.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ima_lab.setText("")
        self.ima_lab.setObjectName("ima_lab")
        self.f15 = Building(self.centralwidget)
        self.f15.setGeometry(QtCore.QRect(105, 122, 15, 77))
        self.f15.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.f15.setText("")
        self.f15.setObjectName("f15")

        self.bdposition = [[60, 55], [150, 55], [270, 55], [360, 55], [480, 55], [580, 55], [680, 55], [780, 55],
                           [900, 55], [900, 140], [900, 235], [900, 335], [900, 445], [900, 550],
                           [780, 550], [680, 550], [580, 550], [480, 550], [360, 550], [270, 550],
                           [150, 550], [60, 550], [60, 425], [60, 335], [60, 235], [60, 150]]
        self.building_dic = {(60, 55): None, (150, 55): self.green_center, (270, 55): self.public_safety, (360, 55): self.student_life,
                             (480, 55): self.Room110_Gallery, (580, 55): self.mail_room, (680, 55): self.luckin, (780, 55): self.cafeteria,
                             (900, 55): None, (900, 140): self.the_box, (900, 235): self.auditorium, (900, 335): self.cafe,
                             (900, 445): self.bursar, (900, 550): None, (780, 550): self.IT_center, (680, 550): self.library,
                             (580, 550): self.arc, (480, 550): self.advisor_office, (360, 550): self.H_W_center, (270, 550): self.CDC,
                             (150, 550): self.mac_lab, (60, 550): self.ally_lounge, (60, 425): self.fos_lab, (60, 335): self.piano_room,
                             (60, 235): self.ima_lab, (60, 150): self.f15}

        # main game set up
        self.hide_main_game()
        self.connect_buttons()

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
        for v in self.building_dic.values():
            if v is not None:
                v.hide()
        self.yes.hide()
        self.no.hide()
        self.buy_info.hide()
        self.fate.hide()

    def set_player1_info(self):
        self.yelname.setText(str(self.player1.name))
        self.yelcash.setText(str(self.player1.cash))
        self.yelmoney.setText(str(self.player1.get_money()))
        self.yelhouse.setText(str(self.player1.land))

    def set_player2_info(self):
        self.bluename.setText(str(self.player2.name))
        self.bluecash.setText(str(self.player2.cash))
        self.bluemoney.setText(str(self.player2.get_money()))
        self.bluehouse.setText(str(self.player2.land))

    def show_main_game(self):
        self.set_player1_info()
        self.set_player2_info()
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
        for v in self.building_dic.values():
            if v is not None:
                v.show()
        # self.yes.show()
        # self.no.show()
        self.buy_info.show()
        self.fate.show()

    def connect_buttons(self):
        self.play.clicked.connect(self.start)
        self.step.clicked.connect(self.roll)
        self.exit.clicked.connect(self.end)
        self.no.clicked.connect(self.reject)

    def start(self):
        # d = {"action": "gaming", "update": "start"}
        # mysend(self.s, json.dumps(d))
        self.graphicsView.setStyleSheet("border-image: url(:/figure/main_game_background.jpg);")
        self.hide_cover()
        self.show_main_game()
        # self.bursar_window.show()
        # self.repaint()

    def roll(self):
        if self.anim1.state() != self.anim1.Running and self.anim2.state() != self.anim2.Running:
            num = random.randint(1, 6)
            num = 3
            if self.turn_count % 2 == 0:
                curr_x, curr_y = self.bdposition[self.player1_count]
                next_count = (self.player1_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player1_count = next_count
                self.anim1.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim1.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim1.start()
                self.pass_building(self.player1, next_x, next_y)
            else:
                curr_x, curr_y = self.bdposition[self.player2_count]
                next_count = (self.player2_count + num) % 26
                next_x, next_y = self.bdposition[next_count]
                self.stepnum.setText("{}".format(num))
                self.player2_count = next_count
                self.anim2.setStartValue(QRect(curr_x, curr_y, 41, 51))
                self.anim2.setEndValue(QRect(next_x, next_y, 41, 51))
                self.anim2.start()
                self.pass_building(self.player2, next_x, next_y)

            self.step.setEnabled(False)
            # d = {"action": "gaming", "update": "roll", "num": num}
            # mysend(self.s, json.dumps(d))
            self.turn.setText("{}".format(self.turn_count // 2 + 1))
            self.turn_count += 1

    def pass_building(self, player, x, y):
        assert isinstance(player, Player)
        if player.name == self.player_name1:
            other = self.player2
        else:
            other = self.player1
        building = self.building_dic[(x, y)]
        if building is not None:
            # fate part
            if building.objectName() == "bursar":
                self.bursar_window.show()
                # player.cash += 1000
                # self.fate.setText("Get funded by bursar.")
                self.yes.show()
                self.yes.clicked.connect(self.reject)
            # other fates here
            elif building.objectName() == "CDC":
                pass
            elif building.objectName() == "student_life":
                destiny = self.destiny(player)
                self.fate.setText(destiny)
                self.yes.show()
                self.yes.clicked.connect(self.reject)
            # update once after fate.

            # buy land
            # if building.objectName() not in ["bursar", "CDC", "student_life"]:
            else:
                if building.owner is None:
                    building_name = building.objectName()
                    self.info.setText("You are passing {0}.".format(building_name))
                    self.buy_info.setText("Do you want to buy?")
                    self.yes.clicked.connect(lambda: self.buy(player, building))
                    self.buy_info.show()
                    self.info.show()
                    self.yes.show()
                    self.no.show()

                # passing others' building: fined
                elif player.name != building.owner:
                    fined_money = player.fine_money(building.level)
                    other.cash += fined_money
                    self.info.setText("You are passing others building, fined ${}.".format(fined_money))
                    self.info.show()
                    self.yes.show()
                    self.yes.clicked.connect(self.reject)
                    # self.step.setEnabled(True)
                    # print(self.step.isEnabled())
                    # self.step.repaint()
                    # print(self.step.isEnabled())

                # passing my building: upgrade
                elif player.name == building.owner:
                    self.info.setText("You are passing your own building.")
                    self.buy_info.setText("Do you want to upgrade?")
                    self.buy_info.show()
                    self.info.show()
                    self.yes.clicked.connect(lambda: self.buy(player, building))
                    self.yes.show()
                    self.no.show()
            self.fate.show()
            self.set_player1_info()
            self.set_player2_info()
        else:
            self.info.setText("No buildings to buy here.")
            self.info.show()
            self.yes.show()
            self.yes.clicked.connect(self.reject)

    def buy(self, player, building):
        assert isinstance(player, Player)
        assert isinstance(building, Building)
        try:
            player.buy_building(building)
            self.info.hide()
            self.set_player1_info()
            self.set_player2_info()
        except ValueError:
            self.info.setText("No enough money.")
        self.yes.disconnect()
        self.yes.hide()
        self.no.hide()
        self.buy_info.hide()
        self.fate.hide()
        self.step.setEnabled(True)

    def reject(self):
        self.fate.hide()
        self.fate.setText("")
        self.yes.hide()
        self.no.hide()
        self.yes.disconnect()
        self.buy_info.hide()
        self.info.hide()
        self.step.setEnabled(True)

    def destiny(self, player):
        assert isinstance(player, Player)
        # list_destiny = [['You need to go to the ARC to revise your essay.', 2],
                        # ['You find hair in your meal and decide to go to Health & Wellness for psychological relief.',
                        #  1],
                        # ['You were reported for your behavior when participating the student union election.', 1],
                        # ['You need to go to the eastern-oasis for military training.', 2],
                        # ['You were asked to participate in the graduation ceremony at the Oriental Pearl Tower.', 1],
                        # ['You plan to practice your piano at the piano room.', 1],
                        # ['You plan to buy luck-in coffee.', 1],
                        # ['You were collapsed by the smell of the moor besom in front of AB.', 1],
        list_destiny = [['Your stuff in 314 has been removed \nand lost, you lost $2000.', 2000],
                        ['You are informed to pay \ntuition fee for $3000.', 3000],
                        ['You bought Mate Tea for $2000 during \nGPS to get rid of sleepiness.', 2000],
                        ['You missed shuttle and get a \ntaxi back to the dorm for $5000.', 5000],
                        ['You bought bubble tea for $1000.', 1000],
                        ['You purchased textbook for $5000.', 5000],
                        ['You lost your campus card,  \nyou have to go to Public Safety \nto replace it for $5000.', 5000],
                        ['You bought tickets and clothes \nfor Spring Formal for $1000.', 1000]]
        chosen_destiny = random.choice(list_destiny)
        if chosen_destiny[1] > 10:
            lost = chosen_destiny[1]
            player.cash -= lost
        return chosen_destiny[0]

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
        # d = {"action": "gaming", "update": "stop"}
        # mysend(self.s, json.dumps(d))
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




