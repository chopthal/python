import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, flags=Qt.Widget)
        self.setupUi()

    def setupUi(self):
        # groupbox = QGroupBox(self)

        grid = QGridLayout(self)
        # grid.setRowStretch(0, 1)
        # grid.addWidget(QLabel('TR2 voltages'), 0, 0)
        # grid.setColumnStretch(0, 2)

        for i in range(1, 9):
            # grid.setRowStretch(i, i + 1)
            grid.addWidget(QLabel('Tube' + str(i)), i, 1)
            grid.addWidget(QLineEdit(), i, 2)
            grid.addWidget(QLabel('mV'), i, 3)

        label = QLabel('TR2 voltages')
        grid.addWidget(label, 0, 0)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()