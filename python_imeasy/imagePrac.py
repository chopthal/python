import sys
import os
from PIL import Image, ImageQt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QPen, QTransform
from PyQt5.QtCore import QRectF, Qt, QPoint, QPointF
from PyQt5 import uic

form_class = uic.loadUiType("Graphics.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.scene = GraphicsScene(self)
        # view = QGraphicsView(scene)
        # self.setCentralWidget(view)

        self.imgQ = []
        self.selDir = os.path.dirname(os.path.realpath(__file__))
        # self.scene = GraphicsScene(self)
        # self.ROIRect = []
        # self.ROIRect = QGraphicsRectItem(QRectF(0, 0, 100, 100))
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
        # self.scene.update()
        self.graphicsView.setScene(self.scene)
        self.graphicsView.fitInView(QRectF(0, 0, width, height), Qt.KeepAspectRatio)

    # def drawROIRect(self):
    #     # TODO
    #     rect = QRectF(0, 0, 300, 200)
    #     self.ROIRect = self.scene.addRect(rect)
    #     self.ROIRect.setPen(QPen(Qt.red, 2))
    #     self.ROIRect.setFlags(QGraphicsItem.ItemIsSelectable
    #                           | QGraphicsItem.ItemIsMovable
    #                           | QGraphicsItem.ItemIsFocusable
    #                           | QGraphicsItem.ItemSendsGeometryChanges
    #                           | QGraphicsItem.ItemSendsScenePositionChanges)
    #     self.ROIRect.setPos(QPointF(100, 100))
    #     self.scene.addItem(self.ROIRect)
    #     # self.graphicsView.setScene(self.scene)


class GraphicsScene(QGraphicsScene):
    def __init__(self, parent=None):
        super(GraphicsScene, self).__init__(QRectF(-500, -500, 1000, 1000), parent)
        self._start = QPointF()
        self._current_rect_item = None

    def mousePressEvent(self, event):
        if self.itemAt(event.scenePos(), QTransform()) is None:
            self._current_rect_item = QGraphicsRectItem()
            self._current_rect_item.setBrush(Qt.red)
            self._current_rect_item.setFlag(QGraphicsItem.ItemIsMovable, True)
            self.addItem(self._current_rect_item)
            self._start = event.scenePos()
            r = QRectF(self._start, self._start)
            self._current_rect_item.setRect(r)
        super(GraphicsScene, self).mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self._current_rect_item is not None:
            r = QRectF(self._start, event.scenePos()).normalized()
            self._current_rect_item.setRect(r)
        super(GraphicsScene, self).mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self._current_rect_item = None
        super(GraphicsScene, self).mouseReleaseEvent(event)

#
# class MainWindow(QMainWindow):
#     def __init__(self, parent=None):
#         super(MainWindow, self).__init__(parent)
#         scene = GraphicsScene(self)
#         view = QGraphicsView(scene)
#         self.setCentralWidget(view)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()