import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultVal = 10000
        self.label.setText(str(self.resultVal))

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)

    def pushButton_clicked(self):
        self.resultVal = self.resultVal - 1
        self.label.setText(str(self.resultVal))

    def pushButton_2_clicked(self):
        self.resultVal = self.resultVal + 1
        self.label.setText(str(self.resultVal))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()