import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from test import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.fun1)

    def fun1(self):
        self.graphicsView.setStyleSheet("")
        self.pushButton_2.deleteLater()
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    app.startingUp()
    myWin.show()
    sys.exit(app.exec_())



