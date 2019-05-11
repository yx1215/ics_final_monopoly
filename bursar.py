# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bursar.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(620, 220)
        Dialog.setMinimumSize(QtCore.QSize(620, 220))
        Dialog.setMaximumSize(QtCore.QSize(620, 220))
        Dialog.setStyleSheet("border-image: url(:/figure/bursarinfo.png);")
        self.wuk = QtWidgets.QPushButton(Dialog)
        self.wuk.setGeometry(QtCore.QRect(40, 140, 111, 61))
        self.wuk.setStyleSheet("border-image: url(:/figure/5000.png);")
        self.wuk.setText("")
        self.wuk.setObjectName("wuk")
        self.yiw = QtWidgets.QPushButton(Dialog)
        self.yiw.setGeometry(QtCore.QRect(180, 140, 111, 61))
        self.yiw.setStyleSheet("border-image: url(:/figure/10000.png);")
        self.yiw.setText("")
        self.yiw.setObjectName("yiw")
        self.liangw = QtWidgets.QPushButton(Dialog)
        self.liangw.setGeometry(QtCore.QRect(320, 140, 111, 61))
        self.liangw.setStyleSheet("border-image: url(:/figure/20000.png);")
        self.liangw.setText("")
        self.liangw.setObjectName("liangw")
        self.sanw = QtWidgets.QPushButton(Dialog)
        self.sanw.setGeometry(QtCore.QRect(460, 140, 111, 61))
        self.sanw.setStyleSheet("border-image: url(:/figure/50000.png);")
        self.sanw.setText("")
        self.sanw.setObjectName("sanw")
        self.bucun = QtWidgets.QPushButton(Dialog)
        self.bucun.setGeometry(QtCore.QRect(460, 20, 101, 51))
        self.bucun.setStyleSheet("border-image: url(:/figure/no.png);")
        self.bucun.setText("")
        self.bucun.setObjectName("bucun")
        self.bursarassets = QtWidgets.QLabel(Dialog)
        self.bursarassets.setGeometry(QtCore.QRect(180, 70, 121, 21))
        self.bursarassets.setStyleSheet("border-image: url(:/bursarinfo/white.png);\n"
"font: 15pt \"appo paint\";")
        self.bursarassets.setText("")
        self.bursarassets.setObjectName("bursarassets")
        self.maxloan = QtWidgets.QLabel(Dialog)
        self.maxloan.setGeometry(QtCore.QRect(300, 100, 121, 21))
        self.maxloan.setStyleSheet("border-image: url(:/bursarinfo/white.png);\n"
"font: 15pt \"appo paint\";")
        self.maxloan.setText("")
        self.maxloan.setObjectName("maxloan")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

import picture_rc
