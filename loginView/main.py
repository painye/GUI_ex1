from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from login import loginControl
from face import faceControl


class ViewController:
    def loadLoginView(self):
        self.viewlogin = loginControl()
        self.viewlogin.loginSignal.connect(self.loadFaceView)
        self.viewlogin.show()
        print("I am login")

    def loadFaceView(self, str):
        self.viewFace = faceControl()
        self.viewFace.setWindowTitle("faceRec")
        self.viewFace.exitSignal.connect(self.loadLoginView)
        self.viewFace.show()
        print("I am face")
        print(str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    view = ViewController()
    view.loadLoginView()
    sys.exit(app.exec())