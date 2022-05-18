import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.resultVal = 10000
        self.selDir = os.path.dirname(os.path.realpath(__file__))

        self.label.setText(str(self.resultVal))
        self.label_2.setText(self.selDir)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)
        self.pushButton_4.clicked.connect(self.pushButton_4_clicked)

    def pushButton_clicked(self):
        self.resultVal = self.resultVal - 1
        self.label.setText(str(self.resultVal))

    def pushButton_2_clicked(self):
        self.resultVal = self.resultVal + 1
        self.label.setText(str(self.resultVal))

    def pushButton_4_clicked(self):
        tmpDir = QFileDialog.getExistingDirectory(self, 'Select Directory', self.selDir)
        if tmpDir:
            self.selDir = tmpDir
        else:
            return
        self.label_2.setText(self.selDir)

    def pushButton_3_clicked(self):
        os.system(f'start {self.selDir}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()