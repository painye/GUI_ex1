import sys

from loginView import Ui_login_ui
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

def rejister(ui):
    username = ui.lineEdit_username.text()
    print(username)
    password = ui.lineEdit_password.text()
    print(password)
    path = "F:\\bishe\\ideaWork\\GUI_ex1\\loginView\\account\\"
    with open (path + username+".txt", 'w') as file:
        file.write(password+"\n")

def login(ui):
    username = ui.lineEdit_username.text()
    print(username)
    password = ui.lineEdit_password.text()
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


if __name__ == '__main__':
    # 每一个Qt程序都需要有一个QApplication对象，调用*.exec_()方法进入该程序的主循环（即事件循环）
    app = QApplication(sys.argv)
    login_Window = QMainWindow()
    ui = Ui_login_ui()
    ui.setupUi(login_Window)
    login_Window.show()

    ui.pushButton_rejister.clicked.connect(partial(rejister, ui))   # 注册按钮触发
    ui.pushButton_login.clicked.connect(partial(login, ui))       # 登录按钮触发

    sys.exit(app.exec_())