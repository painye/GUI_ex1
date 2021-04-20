import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

from faceView import Ui_face_window

def face(ui):
    print("this is my face")


def check(ui):
    print("i will check")


if __name__ == "__main__":
    app =QApplication(sys.argv)
    face_window = QMainWindow()
    ui = Ui_face_window()
    ui.setupUi(face_window)
    face_window.show()

    ui.pushButton_face.clicked.connect(partial(face, ui))
    ui.pushButton_check.clicked.connect(partial(check, ui))

    sys.exit(app.exec_())