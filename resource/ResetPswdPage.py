# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ResetPswdPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ResetPswdPage(object):
    def setupUi(self, ResetPswdPage):
        ResetPswdPage.setObjectName("ResetPswdPage")
        ResetPswdPage.resize(600, 395)
        ResetPswdPage.setMinimumSize(QtCore.QSize(600, 395))
        ResetPswdPage.setMaximumSize(QtCore.QSize(600, 395))
        ResetPswdPage.setStyleSheet("#ResetPswdPage{\n"
"    border-image: url(:/reset/images/background.bmp);\n"
"}")
        ResetPswdPage.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralWidget = QtWidgets.QWidget(ResetPswdPage)
        self.centralWidget.setObjectName("centralWidget")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setGeometry(QtCore.QRect(100, 60, 401, 291))
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
        self.Reset_Password = QtWidgets.QLineEdit(self.frame)
        self.Reset_Password.setGeometry(QtCore.QRect(170, 120, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Reset_Password.setFont(font)
        self.Reset_Password.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Reset_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Reset_Password.setObjectName("Reset_Password")
        self.Title = QtWidgets.QLabel(self.frame)
        self.Title.setGeometry(QtCore.QRect(110, 10, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.Reset = QtWidgets.QPushButton(self.frame)
        self.Reset.setGeometry(QtCore.QRect(170, 240, 75, 23))
        self.Reset.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.Reset.setObjectName("Reset")
        self.Acct_label = QtWidgets.QLabel(self.frame)
        self.Acct_label.setGeometry(QtCore.QRect(80, 60, 91, 31))
        self.Acct_label.setObjectName("Acct_label")
        self.Pswd_label = QtWidgets.QLabel(self.frame)
        self.Pswd_label.setGeometry(QtCore.QRect(80, 120, 91, 31))
        self.Pswd_label.setObjectName("Pswd_label")
        self.Reset_Password1 = QtWidgets.QLineEdit(self.frame)
        self.Reset_Password1.setGeometry(QtCore.QRect(170, 180, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.Reset_Password1.setFont(font)
        self.Reset_Password1.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.Reset_Password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Reset_Password1.setObjectName("Reset_Password1")
        self.Pswd1_label = QtWidgets.QLabel(self.frame)
        self.Pswd1_label.setGeometry(QtCore.QRect(80, 180, 91, 31))
        self.Pswd1_label.setObjectName("Pswd1_label")
        ResetPswdPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(ResetPswdPage)
        QtCore.QMetaObject.connectSlotsByName(ResetPswdPage)

    def retranslateUi(self, ResetPswdPage):
        _translate = QtCore.QCoreApplication.translate
        ResetPswdPage.setWindowTitle(_translate("ResetPswdPage", "用户密码重置"))
        self.Account.setPlaceholderText(_translate("ResetPswdPage", "账户"))
        self.Reset_Password.setPlaceholderText(_translate("ResetPswdPage", "密码"))
        self.Title.setText(_translate("ResetPswdPage", "用户密码重置"))
        self.Reset.setText(_translate("ResetPswdPage", "修改密码"))
        self.Acct_label.setText(_translate("ResetPswdPage", "请输入用户名："))
        self.Pswd_label.setText(_translate("ResetPswdPage", "请输入密码："))
        self.Reset_Password1.setPlaceholderText(_translate("ResetPswdPage", "密码"))
        self.Pswd1_label.setText(_translate("ResetPswdPage", "请确认密码："))
import pic_rc

if __name__ == "__main__":
    import sys,PyQt5
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_ResetPswdPage()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())