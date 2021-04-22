import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from faceView import Ui_face_window


class faceControl(QMainWindow, Ui_face_window):
    exitSignal = pyqtSignal()

    def __init__(self, parent=None):
        super(faceControl, self).__init__(parent)
        print("yes, this is face")
        self.setupUi(self)
        self.pushButton_face.clicked.connect(self.face)
        self.pushButton_check.clicked.connect(self.check)
        self.exitSignal.connect(lambda: print("emit"))

    def face(self):
        print("this is my face")

    def check(self, a0: QtGui.QCloseEvent) -> None:
        print("i will check")
        self.exitSignal.emit()
        self.close()


"""if __name__ == "__main__":
    app =QApplication(sys.argv)
    face_window = QMainWindow()
    ui = Ui_face_window()
    ui.setupUi(face_window)
    face_window.show()

    ui.pushButton_face.clicked.connect(partial(face, ui))
    ui.pushButton_check.clicked.connect(partial(check, ui))

    sys.exit(app.exec_())"""