# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bursar.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()

        self.result = 0
        self.setObjectName("Dialog")
        self.resize(620, 220)
        self.setMinimumSize(QtCore.QSize(620, 220))
        self.setMaximumSize(QtCore.QSize(620, 220))
        self.setStyleSheet("border-image: url(:/figure/bursarinfo.png);")
        self.wuqian = QtWidgets.QPushButton(self)
        self.wuqian.setGeometry(QtCore.QRect(40, 140, 111, 61))
        self.wuqian.setStyleSheet("border-image: url(:/figure/5000.png);")
        self.wuqian.setText("")
        self.wuqian.setObjectName("wuqian")
        self.yiwan = QtWidgets.QPushButton(self)
        self.yiwan.setGeometry(QtCore.QRect(180, 140, 111, 61))
        self.yiwan.setStyleSheet("border-image: url(:/figure/10000.png);")
        self.yiwan.setText("")
        self.yiwan.setObjectName("yiwan")
        self.liangwan = QtWidgets.QPushButton(self)
        self.liangwan.setGeometry(QtCore.QRect(320, 140, 111, 61))
        self.liangwan.setStyleSheet("border-image: url(:/figure/20000.png);")
        self.liangwan.setText("")
        self.liangwan.setObjectName("liangwan")
        self.wuwan = QtWidgets.QPushButton(self)
        self.wuwan.setGeometry(QtCore.QRect(460, 140, 111, 61))
        self.wuwan.setStyleSheet("border-image: url(:/figure/50000.png);")
        self.wuwan.setText("")
        self.wuwan.setObjectName("wuwan")
        self.reject = QtWidgets.QPushButton(self)
        self.reject.setGeometry(QtCore.QRect(460, 20, 101, 51))
        self.reject.setStyleSheet("border-image: url(:/figure/no.png);")
        self.reject.setText("")
        self.reject.setObjectName("reject")
        self.bursarassets = QtWidgets.QLabel(self)
        self.bursarassets.setGeometry(QtCore.QRect(180, 70, 121, 21))
        self.bursarassets.setStyleSheet("border-image: url(:/bursarinfo/white.png);\n"
"font: 15pt \"appo paint\";")
        self.bursarassets.setText("")
        self.bursarassets.setObjectName("bursarassets")
        self.maxloan = QtWidgets.QLabel(self)
        self.maxloan.setGeometry(QtCore.QRect(300, 100, 121, 21))
        self.maxloan.setStyleSheet("border-image: url(:/bursarinfo/white.png);\n"
"font: 15pt \"appo paint\";")
        self.maxloan.setText("")
        self.maxloan.setObjectName("maxloan")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        self.wuqian.clicked.connect(self.get_wuqian)
        self.yiwan.clicked.connect(self.get_yiwan)
        self.liangwan.clicked.connect(self.get_liangwan)
        self.wuwan.clicked.connect(self.get_wuwan)
        self.limit = 0

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Dialog"))

    def set_info_text(self, maxloan, asset):
        self.limit = maxloan
        self.maxloan.setText(str(maxloan))
        self.bursarassets.setText(str(asset))

    def get_wuwan(self):
        if self.limit >= 50000:
            self.result = 50000
        else:
            self.result = None
        self.hide()

    def get_liangwan(self):
        if self.limit >= 50000:
            self.result = 50000
        else:
            self.result = None
        self.hide()

    def get_yiwan(self):
        if self.limit >= 50000:
            self.result = 50000
        else:
            self.result = None
        self.hide()

    def get_wuqian(self):
        if self.limit >= 50000:
            self.result = 50000
        else:
            self.result = None
        self.hide()

    def get_zero(self):
        self.result = 0
        self.hide()

import picture_rc
