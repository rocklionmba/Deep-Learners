from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt, QPoint
CANVAS_DIMENSIONS = 1050,580
class Whiteboard(QtWidgets.QLabel):

    def initalize(self):
        self.background_color = QColor(Qt.white)
        self.brushSize = 9
        self.brushColor = Qt.black
        self.reset()

    def reset(self):
        self.setPixmap(QPixmap(*CANVAS_DIMENSIONS))
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