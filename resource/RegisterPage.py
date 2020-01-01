# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegisterPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RegisterPage(object):
    def setupUi(self, RegisterPage):
        RegisterPage.setObjectName("RegisterPage")
        RegisterPage.resize(600, 393)
        RegisterPage.setMinimumSize(QtCore.QSize(600, 393))
        RegisterPage.setMaximumSize(QtCore.QSize(600, 393))
        RegisterPage.setStyleSheet("#RegisterPage{\n"
                                   "        border-image: url(:/register/images/background.bmp);\n"
                                   "}")
        RegisterPage.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(RegisterPage)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(110, 60, 401, 291))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.Account = QtWidgets.QLineEdit(self.frame)
        self.Account.setGeometry(QtCore.QRect(170, 60, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Account.setFont(font)
        self.Account.setObjectName("Account")
        self.Register_Password = QtWidgets.QLineEdit(self.frame)
        self.Register_Password.setGeometry(QtCore.QRect(170, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Register_Password.setFont(font)
        self.Register_Password.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Register_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Register_Password.setObjectName("Register_Password")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(110, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Register = QtWidgets.QPushButton(self.frame)
        self.Register.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.Register.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Register.setObjectName("Register")
        self.Acct_label = QtWidgets.QLabel(self.frame)
        self.Acct_label.setGeometry(QtCore.QRect(80, 60, 91, 31))
        self.Acct_label.setObjectName("Acct_label")
        self.Pswd_label = QtWidgets.QLabel(self.frame)
        self.Pswd_label.setGeometry(QtCore.QRect(80, 120, 91, 31))
        self.Pswd_label.setObjectName("Pswd_label")
        self.Register_Password1 = QtWidgets.QLineEdit(self.frame)
        self.Register_Password1.setGeometry(QtCore.QRect(170, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Register_Password1.setFont(font)
        self.Register_Password1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Register_Password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Register_Password1.setObjectName("Register_Password1")
        self.Pswd1_label = QtWidgets.QLabel(self.frame)
        self.Pswd1_label.setGeometry(QtCore.QRect(80, 180, 91, 31))
        self.Pswd1_label.setObjectName("Pswd1_label")
        RegisterPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(RegisterPage)
        QtCore.QMetaObject.connectSlotsByName(RegisterPage)

    def retranslateUi(self, RegisterPage):
        _translate = QtCore.QCoreApplication.translate
        RegisterPage.setWindowTitle(_translate("RegisterPage", "用户注册"))
        self.Account.setPlaceholderText(_translate("RegisterPage", "账户"))
        self.Register_Password.setPlaceholderText(_translate("RegisterPage", "密码"))
        self.Title.setText(_translate("RegisterPage", "用户注册"))
        self.Register.setText(_translate("RegisterPage", "注册"))
        self.Acct_label.setText(_translate("RegisterPage", "请输入用户名："))
        self.Pswd_label.setText(_translate("RegisterPage", "请输入密码："))
        self.Register_Password1.setPlaceholderText(_translate("RegisterPage", "密码"))
        self.Pswd1_label.setText(_translate("RegisterPage", "请确认密码："))


import pic_rc

if __name__ == "__main__":
    import sys, PyQt5

    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_RegisterPage()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
