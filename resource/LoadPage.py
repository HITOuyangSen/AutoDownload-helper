# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoadPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LoadPage(object):
    def setupUi(self, LoadPage):
        LoadPage.setObjectName("LoadPage")
        LoadPage.resize(600, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoadPage.sizePolicy().hasHeightForWidth())
        LoadPage.setSizePolicy(sizePolicy)
        LoadPage.setMinimumSize(QtCore.QSize(600, 400))
        LoadPage.setMaximumSize(QtCore.QSize(600, 400))
        LoadPage.setStyleSheet("#LoadPage{\n"
"    border-image: url(:/load/images/background.bmp);\n"
"}")
        LoadPage.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(LoadPage)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(110, 60, 401, 291))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.ForgetPassword = QtWidgets.QPushButton(self.frame)
        self.ForgetPassword.setGeometry(QtCore.QRect(110, 250, 75, 23))
        self.ForgetPassword.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.ForgetPassword.setObjectName("ForgetPassword")
        self.lineEdit_Account = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Account.setGeometry(QtCore.QRect(120, 80, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lineEdit_Account.setFont(font)
        self.lineEdit_Account.setObjectName("lineEdit_Account")
        self.lineEdit_Password = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_Password.setGeometry(QtCore.QRect(120, 140, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.lineEdit_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.Load = QtWidgets.QPushButton(self.frame)
        self.Load.setGeometry(QtCore.QRect(170, 200, 75, 23))
        self.Load.setAutoFillBackground(False)
        self.Load.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Load.setObjectName("Load")
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
        self.Register.setGeometry(QtCore.QRect(230, 250, 75, 23))
        self.Register.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Register.setObjectName("Register")
        LoadPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(LoadPage)
        QtCore.QMetaObject.connectSlotsByName(LoadPage)

    def retranslateUi(self, LoadPage):
        _translate = QtCore.QCoreApplication.translate
        LoadPage.setWindowTitle(_translate("LoadPage", "用户登录"))
        self.ForgetPassword.setText(_translate("LoadPage", "忘记密码"))
        self.lineEdit_Account.setPlaceholderText(_translate("LoadPage", "账户"))
        self.lineEdit_Password.setPlaceholderText(_translate("LoadPage", "密码"))
        self.Load.setText(_translate("LoadPage", "登录"))
        self.Title.setText(_translate("LoadPage", "自动下载助手"))
        self.Register.setText(_translate("LoadPage", "注册"))
import pic_rc

if __name__ == "__main__":
    import sys
    import PyQt5
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    LoadPage = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_LoadPage()
    ui.setupUi(LoadPage)
    LoadPage.show()
    sys.exit(app.exec_())
