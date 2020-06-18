import sys
import os
from PIL import Image, ImageQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QRectF, Qt, QCoreApplication
from PyQt5 import uic

form_class = uic.loadUiType("Graphics.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.imgQ = []
        self.selDir = os.path.dirname(os.path.realpath(__file__))
        self.scene = QGraphicsScene()
        self.ROIRect = QGraphicsRectItem(QRectF(0, 0, 100, 100))
        # self.ROIRect.setFlag(QGraphicsItem.ItemIsMovable, True)

        self.pushButton.clicked.connect(self.pushButton_clicked)
        self.pushButton_2.clicked.connect(self.pushButton_2_clicked)
        self.pushButton_3.clicked.connect(self.pushButton_3_clicked)

    def pushButton_clicked(self):
        dialogRes = QFileDialog.\
            getOpenFileName(self, "Open an image file",
                            self.selDir, "Images (*.png *.jpg *.bmp)")

        if dialogRes[0]:
            self.selDir = os.path.dirname(dialogRes[0])
            print('image loaded')
        else:
            print('load failed')
            return
        img = Image.open(dialogRes[0])
        self.displayImage(img)

    def pushButton_2_clicked(self):
        self.scene.clear()

    def pushButton_3_clicked(self):
        print('pushbutton_3_clicked')
        # Make a ROI rectangle
        self.drawROIRect()
        # TODO

    def displayImage(self, img):
        self.scene.clear()
        width, height = img.size
        self.imgQ = ImageQt.ImageQt(img)
        pixMap = QPixmap.fromImage(self.imgQ)
        self.scene.addPixmap(pixMap)
        self.scene.update()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatio)

    def drawROIRect(self):
        # TODO
        self.scene.addItem(self.ROIRect)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()