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
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint
import sys
from Whiteboard import Whiteboard

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
        self.whiteboard = Whiteboard()
        self.whiteboard.initalize()
        self.whiteboard.setMouseTracking(True)
        self.whiteboard.setFocusPolicy(Qt.StrongFocus)
        self.setCentralWidget(self.whiteboard)

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
            self, "Save Image", "", "PNG Image file (*.png)")

        if filePath:
            pixmap = self.whiteboard.pixmap()
            pixmap.save(filePath, "PNG" )

    def clear(self):  # clear screen function
        self.whiteboard.reset()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
