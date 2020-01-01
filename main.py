import sys
import PyQt5
import PyQt5.sip
from PyQt5.QtWidgets import QApplication
import LoadPage_business, MainPage_business
import RegisterPage_business
import ResetPswdPage__business


def show_register():
    register_window = RegisterPage_business.RegisterPage(window)
    register_window.show()


def show_resetpswd():
    reset_window = ResetPswdPage__business.ResetPswdPage(window)
    reset_window.show()


def show_mainwindow():
    register_window = MainPage_business.MainPage(window)
    register_window.show()
    window.hide()


if __name__ == "__main__":
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = LoadPage_business.Ui_LoadPage()
    window.show_register_signal.connect(show_register)
    window.show_resetpswd_signal.connect(show_resetpswd)
    window.show_mainwindow_signal.connect(show_mainwindow)
    window.show()
    sys.exit(app.exec_())
