# -*- coding: utf-8 -*-

"""
Module implementing ResetPswdPage.
"""

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow, QApplication,  QMessageBox
import sys
from resource.ResetPswdPage import Ui_ResetPswdPage
from SqlConn import *

class ResetPswdPage(QMainWindow, Ui_ResetPswdPage):
    """
    Class documentation goes here.
    """
    def __init__(self, parent=None, *args, **kwargs):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """
        super(ResetPswdPage, self).__init__(parent, *args, **kwargs)
        self.setupUi(self)
    
    def message(self,str0:str):
        QMessageBox.information(self, 'Hi', '{}'.format(str0), QMessageBox.Yes)    # 提示信息对话窗
        return
        
    @pyqtSlot()
    def on_Reset_clicked(self):
        acct=self.Account.text()
        pswd= self.Reset_Password.text()
        pswd1= self.Reset_Password1.text()
        if pswd==pswd1:
            sql=SqlConn()
            result=sql.update(acct,pswd)
            if result:
                self.message('密码修改成功!')
            else:
                self.message('密码修改失败!请联系管理员！')
        else:
            self.message('请确认两次输入密码相同！')
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_reset= ResetPswdPage()
    my_reset.show()
    sys.exit(app.exec_())

