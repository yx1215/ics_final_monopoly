# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(960, 600)
        MainWindow.setMinimumSize(QtCore.QSize(960, 600))
        MainWindow.setMaximumSize(QtCore.QSize(960, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.exit = QtWidgets.QPushButton(self.centralwidget)
        self.exit.setGeometry(QtCore.QRect(716, 482, 220, 80))
        self.exit.setStyleSheet("border-image: url(:/figure/exit.png);")
        self.exit.setText("")
        self.exit.setObjectName("exit")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(0, 0, 960, 600))
        self.graphicsView.setStyleSheet("border-image: url(:/figure/ics_game_cover.jpg);")
        self.graphicsView.setObjectName("graphicsView")
        self.play = QtWidgets.QPushButton(self.centralwidget)
        self.play.setGeometry(QtCore.QRect(716, 395, 220, 80))
        self.play.setStyleSheet("border-image: url(:/figure/start.png);")
        self.play.setText("")
        self.play.setObjectName("play")
        self.graphicsView.raise_()
        self.exit.raise_()
        self.play.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

import picture_rc
