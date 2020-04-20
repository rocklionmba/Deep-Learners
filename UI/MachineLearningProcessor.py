import PyQt5,sys
from PyQt5 import QtCore,QtGui
sys.path.append('../Machine_Learning')
import Machine_Learning as ml

class MachineLearningProcessor(QtCore.QObject):
    finished = QtCore.pyqtSignal()
    dataReady = QtCore.pyqtSignal(str)

    @QtCore.pyqtSlot(list, list)
    def processImgs(self, imgs, answers):
        mlResponse = []
        responseBank = ""
        i = 0
        for file in imgs:
            mlResponse.append(ml.check_if_correct(eval(answers[i]),ml.get_number(ml.detector(file))))
            i += 1

        for j in range(len(self.problemArr)):
                responseBank += ("Problem " + '{a}'.format(a=j+1) + ": " + '{b}'.format(
                    b=self.problemArr[j]) + " = " + '{c}'.format(c=mlResponse[j])+"\n")
        self.dataReady.emit(responseBank)
        self.finished.emit()
