import sys
from PyQt5.QtWidgets import *


class EmptyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle("Pushbuttonwindow")

        btn = QPushButton("Click me", self)
        btn.move(20, 20)
        btn.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        QMessageBox.about(self, "Message", "Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmptyWindow()
    window.show()
    app.exec_()
