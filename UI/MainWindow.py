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
from PyQt5 import uic, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QColor, QPixmap
from PyQt5.QtCore import Qt, QPoint
import sys
from Whiteboard import Whiteboard


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        #title = "Paint Application"
        #top = 0
        #left = 75
        #width = 1920
        #height = 1080

        #icon = "icons/pain.png"
        self.filePath = ""
        self.setWindowTitle("Whiteboard Application")

        ui = uic.loadUi("MainWindow.ui", self)

        # All findChild should go here
        self.whiteboardMainButton = self.findChild(QtWidgets.QPushButton, 'whiteboardMainButton')
        self.mathgameMainButton = self.findChild(QtWidgets.QPushButton, 'mathgameMainButton')
        self.mainStackedWidget = self.findChild(QtWidgets.QStackedWidget, 'mainStackedWidget')
        self.backButton = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.clearButton = self.findChild(QtWidgets.QPushButton, 'clearButton')
        self.mainWhiteboard = self.findChild(Whiteboard, 'mainWhiteboard')
        self.scratchPaperWhiteboard = self.findChild(Whiteboard, 'scratchPaperWhiteboard')
        self.answerBoxWhiteboard = self.findChild(Whiteboard, 'answerBoxWhiteboard')
        self.newWhiteboard = self.findChild(QtWidgets.QAction, 'actionWhiteboard')
        self.saveWhiteboard = self.findChild(QtWidgets.QAction, 'actionSave')
        self.saveAsWhiteboard = self.findChild(QtWidgets.QAction, 'actionSave_As')
        self.closeWhiteboard = self.findChild(QtWidgets.QAction, 'actionClose')
        self.openWhiteboard = self.findChild(QtWidgets.QAction, 'actionOpen')
        #self.operatorComboBox = self.findChild(QtWidgets.QComboBox, 'operatorComboBox')
        # End findChild

        self.mainWhiteboard.initalize()
        self.mainWhiteboard.setMouseTracking(True)
        self.mainWhiteboard.setFocusPolicy(Qt.StrongFocus)

        self.scratchPaperWhiteboard.initalize(691, 581)
        self.scratchPaperWhiteboard.setMouseTracking(True)
        self.scratchPaperWhiteboard.setFocusPolicy(Qt.StrongFocus)

        self.answerBoxWhiteboard.initalize(361, 231)
        self.answerBoxWhiteboard.setMouseTracking(True)
        self.answerBoxWhiteboard.setFocusPolicy(Qt.StrongFocus)

        if (type(self.mainStackedWidget) == "NoneType"):
            print("none")

        self.whiteboardMainButton.clicked.connect(lambda: self.setNewWhiteboard())
        self.mathgameMainButton.clicked.connect(lambda: self.setNewMathgame())
        self.backButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.backButton_3.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.clearButton.clicked.connect(lambda: self.clear())
        self.clearButton_3.clicked.connect(lambda: self.clear())
        self.newWhiteboard.triggered.connect(lambda: self.setNewWhiteboard())
        self.openWhiteboard.triggered.connect(lambda: self.openExistingWhiteboard())
        self.saveWhiteboard.triggered.connect(lambda: self.save())
        self.saveAsWhiteboard.triggered.connect(lambda: self.saveAs())
        self.closeWhiteboard.triggered.connect(lambda: self.setCloseWhiteboard())

    def setNewWhiteboard(self):
        self.mainStackedWidget.setCurrentIndex(1)
        self.setWindowTitle("Whiteboard Application - New Project")
        self.mainWhiteboard.reset()

    def openExistingWhiteboard(self):
        self.filePath, _ = QFileDialog.getOpenFileName(
            self, "Open Whiteboard", "", "Whiteboard file (*.wtbd)")

        pixmap = QPixmap()
        pixmap.load(self.filePath)
        self.setNewWhiteboard()
        self.setWindowTitle("Whiteboard Application - " + self.filePath)
        self.mainWhiteboard.setPixmap(pixmap)

    def save(self):  # save file function
        if (self.filePath == ""):
            self.filePath, _ = QFileDialog.getSaveFileName(
                self, "Save Whiteboard", "", "Whiteboard file (*.wtbd)")

        pixmap = self.mainWhiteboard.pixmap()
        self.setWindowTitle("Whiteboard Application - " + self.filePath)
        pixmap.save(self.filePath, "PNG")

    def saveAs(self):  # save file function
        self.filePath, _ = QFileDialog.getSaveFileName(
            self, "Save Whiteboard", "", "Whiteboard file (*.wtbd)")

        pixmap = self.mainWhiteboard.pixmap()
        self.setWindowTitle("Whiteboard Application - " + self.filePath)
        pixmap.save(self.filePath, "PNG")

    def clear(self):  # clear screen function
        self.mainWhiteboard.reset()
        self.scratchPaperWhiteboard.reset()
        self.answerBoxWhiteboard.reset()

    def setCloseWhiteboard(self):
        self.mainWhiteboard.reset()
        self.filePath = ""
        self.setWindowTitle("Whiteboard Application")
        self.mainStackedWidget.setCurrentIndex(0)

    def setNewMathgame(self):
        self.mainStackedWidget.setCurrentIndex(2)
        self.setWindowTitle("Whiteboard Application - Math Game")
        self.scratchPaperWhiteboard.reset()
        self.answerBoxWhiteboard.reset()


"""
        operator = str(operatorComboBox.currentText())
        print(operator)

    if(operator == "Addition"):
        operatorText.
"""

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
