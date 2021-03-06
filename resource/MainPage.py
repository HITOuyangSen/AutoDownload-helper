# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainPage.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainPage(object):
    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(735, 636)
        MainPage.setMinimumSize(QtCore.QSize(735, 636))
        MainPage.setMaximumSize(QtCore.QSize(735, 636))
        MainPage.setAcceptDrops(True)
        MainPage.setWhatsThis("")
        MainPage.setStyleSheet("#MainPage{\n"
                               "border-image: url(:/mainwindow/images/Mainbackground.bmp);\n"
                               "}")
        MainPage.setAnimated(False)
        self.centralWidget = QtWidgets.QWidget(MainPage)
        self.centralWidget.setObjectName("centralWidget")
        self.TargetUser_label = QtWidgets.QLabel(self.centralWidget)
        self.TargetUser_label.setGeometry(QtCore.QRect(40, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.TargetUser_label.setFont(font)
        self.TargetUser_label.setAlignment(QtCore.Qt.AlignCenter)
        self.TargetUser_label.setObjectName("TargetUser_label")
        self.Scrap_pushButton = QtWidgets.QPushButton(self.centralWidget)
        self.Scrap_pushButton.setGeometry(QtCore.QRect(330, 100, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.Scrap_pushButton.setFont(font)
        self.Scrap_pushButton.setAutoFillBackground(False)
        self.Scrap_pushButton.setStyleSheet("#Scrap_pushButton{\n"
                                            "    border-radius:10px;\n"
                                            "    background-color: rgb(85, 170, 255);\n"
                                            "}\n"
                                            "")
        self.Scrap_pushButton.setObjectName("Scrap_pushButton")
        self.HomePageUrl_lineEdit = QtWidgets.QLineEdit(self.centralWidget)
        self.HomePageUrl_lineEdit.setGeometry(QtCore.QRect(200, 40, 411, 41))
        self.HomePageUrl_lineEdit.setStyleSheet("#HomePageUrl_lineEdit{\n"
                                                "        border-radius:10px;}")
        self.HomePageUrl_lineEdit.setObjectName("HomePageUrl_lineEdit")
        self.layoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(181, 161, 453, 390))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.Information_tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.Information_tableWidget.setMinimumSize(QtCore.QSize(110, 0))
        self.Information_tableWidget.setBaseSize(QtCore.QSize(123, 231))
        self.Information_tableWidget.setAutoFillBackground(False)
        self.Information_tableWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Information_tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.Information_tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.Information_tableWidget.setTabKeyNavigation(False)
        self.Information_tableWidget.setProperty("showDropIndicator", False)
        self.Information_tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.Information_tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.Information_tableWidget.setCornerButtonEnabled(False)
        self.Information_tableWidget.setObjectName("Information_tableWidget")
        self.Information_tableWidget.setColumnCount(3)
        self.Information_tableWidget.setRowCount(10)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignVCenter)
        self.Information_tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        self.Information_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Information_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(10)
        item.setFont(font)
        self.Information_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Information_tableWidget.setItem(0, 0, item)
        self.Information_tableWidget.horizontalHeader().setVisible(True)
        self.Information_tableWidget.horizontalHeader().setHighlightSections(False)
        self.Information_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.Information_tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.Information_tableWidget)
        MainPage.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)

    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "自动下载助手"))
        self.TargetUser_label.setText(_translate("MainPage", "目标用户:"))
        self.Scrap_pushButton.setText(_translate("MainPage", "开始自动下载"))
        self.label.setText(_translate("MainPage", "用户作品信息"))
        item = self.Information_tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainPage", "1"))
        item = self.Information_tableWidget.verticalHeaderItem(1)
        item.setText(_translate("MainPage", "2"))
        item = self.Information_tableWidget.verticalHeaderItem(2)
        item.setText(_translate("MainPage", "3"))
        item = self.Information_tableWidget.verticalHeaderItem(3)
        item.setText(_translate("MainPage", "4"))
        item = self.Information_tableWidget.verticalHeaderItem(4)
        item.setText(_translate("MainPage", "5"))
        item = self.Information_tableWidget.verticalHeaderItem(5)
        item.setText(_translate("MainPage", "6"))
        item = self.Information_tableWidget.verticalHeaderItem(6)
        item.setText(_translate("MainPage", "7"))
        item = self.Information_tableWidget.verticalHeaderItem(7)
        item.setText(_translate("MainPage", "8"))
        item = self.Information_tableWidget.verticalHeaderItem(8)
        item.setText(_translate("MainPage", "9"))
        item = self.Information_tableWidget.verticalHeaderItem(9)
        item.setText(_translate("MainPage", "10"))
        item = self.Information_tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainPage", "作品名称"))
        item = self.Information_tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainPage", "作品时长"))
        item = self.Information_tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainPage", "下载状态"))
        __sortingEnabled = self.Information_tableWidget.isSortingEnabled()
        self.Information_tableWidget.setSortingEnabled(False)
        self.Information_tableWidget.setSortingEnabled(__sortingEnabled)


import pic_rc
if __name__ == "__main__":
    import sys,PyQt5
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = PyQt5.QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec_())
