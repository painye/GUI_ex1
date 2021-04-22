import sys

from loginView import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from functools import partial


class loginControl(QMainWindow, Ui_login_ui):
    # Qwidget是所有用户界面对象的基类
    # 声明一个无参数的信号
    loginSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(loginControl, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_rejister.clicked.connect(self.rejister)
        self.pushButton_login.clicked.connect(self.login)

    def rejister(self):
        username = self.lineEdit_username.text()
        print(username)
        password = self.lineEdit_password.text()
        print(password)
        path = "F:\\bishe\\ideaWork\\GUI_ex1\\loginView\\account\\"
        with open (path + username+".txt", 'w') as file:
            file.write(password+"\n")
        self.loginSignal.emit("rejister")
        self.close()

    def login(self):
        username = self.lineEdit_username.text()
        print(username)
        password = self.lineEdit_password.text()
        print(password)
        path = "F:\\bishe\\ideaWork\\GUI_ex1\\loginView\\account\\"
        try:
            with open(path + username + ".txt", 'r') as file:
                myPassword = file.readline()
                print(myPassword)
                if myPassword == password+"\n":
                    print("登陆成功")
        except FileNotFoundError:
            print("we can't found the file")
        self.loginSignal.emit("login")
        self.close()


"""if __name__ == '__main__':
    # 每一个Qt程序都需要有一个QApplication对象，调用*.exec_()方法进入该程序的主循环（即事件循环）
    app = QApplication(sys.argv)
    login_Window = QMainWindow()
    ui = Ui_login_ui()
    ui.setupUi(login_Window)
    login_Window.show()

    ui.pushButton_rejister.clicked.connect(partial(rejister, ui))   # 注册按钮触发
    ui.pushButton_login.clicked.connect(partial(login, ui))       # 登录按钮触发

    sys.exit(app.exec_())"""

