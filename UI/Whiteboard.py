from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt, QPoint


class Whiteboard(QtWidgets.QLabel):
    def initalize(self, x=1211, y=841):
        self.canx = x
        self.cany = y
        #self.resize(int(self.parent().width()), int(self.parent().height()))
        self.background_color = QColor(Qt.white)
        self.brushSize = 9
        self.brushColor = Qt.black
        self.reset()


    def blueColor(self):
        self.brushColor = Qt.blue

    def blackColor(self):
        self.brushColor = Qt.black

    def redColor(self):
        self.brushColor = Qt.red

    def greenColor(self):
        self.brushColor = Qt.green

    def purpleColor(self):
        self.brushColor = Qt.magenta

    def grayColor(self):
        self.brushColor = Qt.gray

    def reset(self):
        self.setPixmap(QPixmap(self.canx, self.cany))
        self.pixmap().fill(self.background_color)

    def mousePressEvent(self, event):
        self.last_pos = event.pos()

    def mouseMoveEvent(self, event):
        if hasattr(self, 'last_pos') and self.last_pos:
            painter = QPainter(self.pixmap())
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.last_pos, event.pos())
            self.last_pos = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        self.last_pos = None
