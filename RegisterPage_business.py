# -*- coding: utf-8 -*-

"""
Module implementing RegisterPage.
"""

import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from SqlConn import *
from resource.RegisterPage import *


class RegisterPage(QMainWindow, Ui_RegisterPage):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, *args, **kwargs):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(RegisterPage, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
    
    def message(self,str0:str):
        QMessageBox.information(self, 'Hi', '{}'.format(str0), QMessageBox.Yes)    # 提示信息对话窗
        return
        
        
    @pyqtSlot()
    def on_Register_clicked(self):
        acct=self.Account.text()
        pswd= self.Register_Password.text()
        pswd1= self.Register_Password1.text()
        if pswd==pswd1:
            sql=SqlConn()
            result=sql.insert(acct,pswd)
            if result:
                self.message('注册成功!')
            else:
                self.message('注册失败!请联系管理员！')
        else:
            self.message('请确认两次输入密码相同！')
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_register= RegisterPage()
    my_register.show()
    sys.exit(app.exec_())
