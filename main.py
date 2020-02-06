import sys

import PyQt5.sip
from PyQt5.QtWidgets import QApplication
import MainPage_business
import LoadPage_business
import RegisterPage_business
import ResetPswdPage__business
import MainPage_business

def show_register():
    window.register_window = RegisterPage_business.RegisterPage(window)
    window.register_window.show()


def show_resetpswd():
    window.reset_window = ResetPswdPage__business.ResetPswdPage(window)
    window.reset_window.show()


def show_mainwindow():
    window.MainPage_window = MainPage_business.MainPage(window)
    window.MainPage_window.show()
    window.hide()


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = LoadPage_business.Ui_LoadPage()
    window.show_register_signal.connect(show_register)
    window.show_resetpswd_signal.connect(show_resetpswd)
    window.show_mainwindow_signal.connect(show_mainwindow)
    window.show()
    sys.exit(app.exec_())
