# -*- coding: utf-8 -*-

"""
Module implementing MainWindow.
"""

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from MainPage_business import MainPage
from RegisterPage_business import RegisterPage
from ResetPswdPage__business import ResetPswdPage
from SqlConn import SqlConn
from resource.LoadPage import Ui_LoadPage


class Ui_LoadPage(QMainWindow, Ui_LoadPage):
    """
    Class documentation goes here.
    """
    show_register_signal = pyqtSignal()
    show_resetpswd_signal = pyqtSignal()
    show_mainwindow_signal = pyqtSignal()

    def __init__(self, parent=None, *args, **kwargs):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(Ui_LoadPage, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)

    def message(self, str0: str):
        QMessageBox.information(self, 'Hi', '{}'.format(str0), QMessageBox.Yes)  # 提示信息对话窗
        return

    @pyqtSlot()
    def on_Register_clicked(self):
        self.show_register_signal.emit()

    @pyqtSlot()
    def on_ForgetPassword_clicked(self):
        self.show_resetpswd_signal.emit()

    @pyqtSlot()
    def on_Load_clicked(self):
        acct = self.lineEdit_Account.text()
        pswd = self.lineEdit_Password.text()
        info = (acct, pswd)
        conn = SqlConn().get_conn()
        cursor = conn.cursor()
        # 查询数据
        cursor.execute('SELECT * FROM `students_account`.`accounts`')
        data = cursor.fetchall()
        account = []
        for i in data:
            account.append(i[0])
        if info in data:
            self.show_mainwindow_signal.emit()
        elif acct in account:
            self.message('密码错误')
        else:
            self.message('用户名未注册')
        cursor.close()
        SqlConn().close_conn()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = Ui_LoadPage()
    MainWindow.show()
    sys.exit(app.exec_())
