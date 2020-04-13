import PyQt5
from PyQt5 import uic, QtWidgets, QtNetwork
from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QVBoxLayout
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush, QColor, QPixmap, QPalette
from PyQt5.QtCore import Qt, QPoint, QSize, QThread, QTimer
import sys
from Whiteboard import Whiteboard

import random
import datetime
import os
import glob
import uuid


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        # icon = "icons/pain.png"
        self.filePath = ""
        self.tVal = 10
        self.difficulty = 0
        self.problemArr = []
        self.resultsUUID = 0
        self.setWindowTitle("Whiteboard Application")

        ui = uic.loadUi("UI/MainWindow.ui", self)

        # All findChild should go here

        # QPushButton
        self.whiteboardMainButton = self.findChild(QtWidgets.QPushButton, 'whiteboardMainButton')
        self.mathgameMainButton = self.findChild(QtWidgets.QPushButton, 'mathgameMainButton')
        self.backButton = self.findChild(QtWidgets.QPushButton, 'backButton')
        self.clearButton = self.findChild(QtWidgets.QPushButton, 'clearButton')
        self.clearAnswer = self.findChild(QtWidgets.QPushButton, 'clearAnswer')
        self.startButton = self.findChild(QtWidgets.QPushButton, 'startButton')
        self.nextButton = self.findChild(QtWidgets.QPushButton, 'nextButton')

        # StackedWidget
        self.mainStackedWidget = self.findChild(QtWidgets.QStackedWidget, 'mainStackedWidget')

        # Whiteboard
        self.mainWhiteboard = self.findChild(Whiteboard, 'mainWhiteboard')
        self.scratchPaperWhiteboard = self.findChild(Whiteboard, 'scratchPaperWhiteboard')
        self.answerBoxWhiteboard = self.findChild(Whiteboard, 'answerBoxWhiteboard')

        # QAction
        self.newWhiteboard = self.findChild(QtWidgets.QAction, 'actionWhiteboard')
        self.saveWhiteboard = self.findChild(QtWidgets.QAction, 'actionSave')
        self.saveAsWhiteboard = self.findChild(QtWidgets.QAction, 'actionSave_As')
        self.closeWhiteboard = self.findChild(QtWidgets.QAction, 'actionClose')
        self.openWhiteboard = self.findChild(QtWidgets.QAction, 'actionOpen')

        # QComboBox
        self.operatorComboBox = self.findChild(QtWidgets.QComboBox, 'operatorComboBox')
        self.difficultyComboBox = self.findChild(QtWidgets.QComboBox, 'difficultyComboBox')
        self.timeComboBox = self.findChild(QtWidgets.QComboBox, 'timeComboBox')

        # QLabel
        self.operatorText = self.findChild(QtWidgets.QLabel, 'operatorText')
        self.scoreResults = self.findChild(QtWidgets.QLabel, 'scoreResults')
        self.questionResults = self.findChild(QtWidgets.QLabel, 'questionResults')
        self.promptLabel = self.findChild(QtWidgets.QLabel, 'promptLabel')

        # QGroupBox
        self.timeUpBox = self.findChild(QtWidgets.QGroupBox, 'timeUpBox')

        # QDialogButtonBox
        self.timeUpOk = self.findChild(QtWidgets.QDialogButtonBox, 'timeUpOk')
        # End findChild

        self.mainWhiteboard.initalize()
        self.mainWhiteboard.setMouseTracking(True)
        self.mainWhiteboard.setFocusPolicy(Qt.StrongFocus)

        self.scratchPaperWhiteboard.initalize(761, 781)
        self.scratchPaperWhiteboard.setMouseTracking(True)
        self.scratchPaperWhiteboard.setFocusPolicy(Qt.StrongFocus)

        self.answerBoxWhiteboard.initalize(461, 421)
        self.answerBoxWhiteboard.setMouseTracking(True)
        self.answerBoxWhiteboard.setFocusPolicy(Qt.StrongFocus)

        if (type(self.mainStackedWidget) == "NoneType"):
            print("none")

        # home Screen actions
        self.whiteboardMainButton.clicked.connect(lambda: self.setNewWhiteboard())
        self.mathgameMainButton.clicked.connect(lambda: self.setNewMathgame())

        # back and clear actions whiteboard and math game
        self.backButton.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.backButton_3.clicked.connect(lambda: self.mainStackedWidget.setCurrentIndex(0))
        self.clearButton.clicked.connect(lambda: self.clear())
        self.clearButton_3.clicked.connect(lambda: self.clear())
        self.clearAnswer.clicked.connect(lambda: self.clearAnswerBoard())

        # actions for file new, open, save, save as, close
        self.newWhiteboard.triggered.connect(lambda: self.setNewWhiteboard())
        self.openWhiteboard.triggered.connect(lambda: self.openExistingWhiteboard())
        self.saveWhiteboard.triggered.connect(lambda: self.save())
        self.saveAsWhiteboard.triggered.connect(lambda: self.saveAs())
        self.closeWhiteboard.triggered.connect(lambda: self.setCloseWhiteboard())

        # actions for selecting pen Color
        self.blueButton.clicked.connect(lambda: self.mainWhiteboard.blueColor())
        self.redButton.clicked.connect(lambda: self.mainWhiteboard.redColor())
        self.greenButton.clicked.connect(lambda: self.mainWhiteboard.greenColor())
        self.blackButton.clicked.connect(lambda: self.mainWhiteboard.blackColor())
        self.purpleButton.clicked.connect(lambda: self.mainWhiteboard.purpleColor())
        self.grayButton.clicked.connect(lambda: self.mainWhiteboard.grayColor())

        # actions for Math game comboxes and timer
        self.operatorComboBox.currentIndexChanged.connect(lambda i: self.setOperator(i))
        self.difficultyComboBox.currentIndexChanged.connect(lambda d: self.setDifficulty(d))
        self.timeComboBox.currentIndexChanged.connect(lambda t: self.setTime(t))
        self.startButton.clicked.connect(lambda: self.startMathGame())
        self.nextButton.clicked.connect(lambda: self.nextProblem())
        self.timeUpOk.clicked.connect(lambda: self.timeUpBox.setVisible(False))

        self.nextButton.setEnabled(False)  # next button
        self.timeUpBox.setVisible(False)  # popup box

    def clearTmp(self):
        # delete tmp files
        files = glob.glob('tmp/*')
        for f in files:
            os.remove(f)

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

    def clearAnswerBoard(self):  # clear answer function
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

    def setOperator(self, i):
        # print(i)
        if i == 0:
            self.operatorText.setText("+")
            self.operator = "add"
        else:
            self.operatorText.setText("*")
            self.operator = "multiply"
        # print(operator)

    def setDifficulty(self, d):
        # print(d)
        self.difficulty = d
        # print(difficulty)

    def setTime(self, t):
        if(t == 0):
            self.tVal = 10  # 10 secs
        elif(t == 1):
            self.tVal = 15  # 15 secs
        elif(t == 2):
            self.tVal = 30  # 30 secs
        elif(t == 3):
            self.tVal = 45  # 45 secs
        elif(t == 4):
            self.tVal = 60  # 1 min
        elif(t == 5):
            self.tVal = 120  # 2 mins
        self.timerCountdown.display(self.tVal)

    def startMathGame(self):
        self.clearTmp()
        self.problemArr.clear()
        self.operatorText.text()
        self.timerCountdown.display(self.tVal)
        self.countdownTimer = QTimer()
        self.countdownTimer.timeout.connect(lambda: self.timerControl())
        self.createNewProblem()
        self.promptLabel.setText("Question 1:")
        self.countdownTimer.start(1000)

    def createNewProblem(self):
        self.nextButton.setDisabled(False)
        self.promptLabel.setText("Question " + str(len(self.problemArr)+1) + ":")
        probRange = self.difficulty * 10 + 11
        a = random.randrange(probRange)
        b = random.randrange(probRange)
        self.aValue.display(a)
        self.bValue.display(b)
        self.problemArr.append('{a} '.format(a=a) + self.operatorText.text() + ' {b}'.format(b=b))
        print('{a} '.format(a=a) + self.operatorText.text() + ' {b}'.format(b=b))
        print(eval('{a} '.format(a=a) + self.operatorText.text() + ' {b}'.format(b=b)))

    def timerControl(self):

        answerBank = ""

        self.timerCountdown.display(self.timerCountdown.intValue() - 1)
        print(self.timerCountdown.intValue())
        if self.timerCountdown.intValue() == 0:
            self.countdownTimer.stop()
            print("done")
            self.nextButton.setEnabled(False)  # disable submissions
            self.timeUpBox.setVisible(True)  # show popup box

            # show results onto self.scoreResults text Box
            for i in range(len(self.problemArr)):
                print("Problem", i+1, ": ", self.problemArr[i], "=", eval(self.problemArr[i]), "\n")

                answerBank += ("Problem " + '{a}'.format(a=i+1) + ": " + '{b}'.format(
                    b=self.problemArr[i]) + " = " + '{c}'.format(c=eval(self.problemArr[i]))+"\n")
                print(answerBank)

            self.questionResults.setText('{d}'.format(d=answerBank))

            # call getResults() function

    def nextProblem(self):
        path = "UI/tmp/answer_" + str(len(self.problemArr)) + ".png"
        pixmap = self.answerBoxWhiteboard.pixmap()
        pixmap.save(path, "PNG")
        self.clear()
        self.clearAnswerBoard()
        self.createNewProblem()

    def getResults(self):
        self.resultsUUID = uuid.uuid4()
        url = PyQt5.QtCore.QUrl('http://localhost:3000/qwertytest1');
        data = { "uuid": self.resultsUUID }
        files = {}
        for filename in os.listdir('UI/tmp'):
            file = PyQt5.QtCore.QFile(filename)
            file.open(PyQt5.QtCore.QFile.ReadOnly)
            files[filename[:-4]] = file
        multipart = construct_multipart(data, files)
        request = QtNetwork.QNetworkRequest(url)
        request.setHeader(QtNetwork.QNetworkRequest.ContentTypeHeader,'multipart/form-data; boundary=%s' % multipart.boundary())
        manager = QtNetwork.QNetworkAccessManager()
        manager.finished.connect(lambda reply: self.response(reply))
        submit = manager.post(request, multipart)

    def construct_multipart(self, data, files):
        multiPart = QtNetwork.QHttpMultiPart(QtNetwork.QHttpMultiPart.FormDataType)
        for key, value in data.items():
            textPart = QtNetwork.QHttpPart()
            textPart.setHeader(QtNetwork.QNetworkRequest.ContentDispositionHeader,"form-data; name=\"%s\"" % key)
            textPart.setBody(value)
            multiPart.append(textPart)

        for key, file in files.items():
            imagePart = QtNetwork.QHttpPart()
            #imagePart.setHeader(QNetworkRequest::ContentTypeHeader, ...);
            fileName = PyQt5.QtCore.QFileInfo(file.fileName()).fileName()
            imagePart.setHeader(QtNetwork.QNetworkRequest.ContentDispositionHeader,"form-data; name=\"%s\"; filename=\"%s\"" % (key, fileName))
            imagePart.setBodyDevice(file);
            multiPart.append(imagePart)
        return multiPart

    def response(self, reply):
        pass



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
