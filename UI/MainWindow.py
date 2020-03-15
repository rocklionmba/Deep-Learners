import PyQt5
'''
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

Form, Window = uic.loadUiType("MainWindow.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()
app.exec_()
'''

from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys

class WbWidget(PyQt5.QtWidgets.QWidget):
    def __init__(self,parent=None):
        PyQt5.QtWidgets.QWidget.__init__(self, parent=parent)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brushSize = 9
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.lastPoint = event.pos()
            # print(self.lastPoint)

    def mouseMoveEvent(self, event):
        if(event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.lastPoint, event.pos())
            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):

        if event.button() == Qt.LeftButton:
            self.drawing = False

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "Paint Application"
        top = 0
        left = 75
        width = 1920
        height = 1080

        icon = "icons/pain.png"

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)
        self.setWindowIcon(QIcon(icon))

        self.mainLayout = QVBoxLayout()
        self.whiteboard = WbWidget(self)
        self.whiteboard.resize(200,200)
        self.setCentralWidget(self.whiteboard)
        self.mousePressEvent

        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")

        saveAction = QAction(QIcon("icons/save.png"), "Save As", self)
        saveAction.setShortcut("Ctrl+S")
        fileMenu.addAction(saveAction)
        saveAction.triggered.connect(self.save)

        clearAction = QAction(QIcon("icons/clear.png"), "Clear", self)
        clearAction.setShortcut("Ctrl+C")
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

    

    def save(self):  # save file function
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save Image", "", "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if filePath == "":
            return
        self.image.save(filePath)

    def clear(self):  # clear screen function
        self.image.fill(Qt.white)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
