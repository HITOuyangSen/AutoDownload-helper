# -*- coding: utf-8 -*-

"""
Module implementing MainPage.
"""
import sys,os
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, QThread, QTimer, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtMultimedia import QSoundEffect
import requests
import re
import datetime,time
import json
import pymongo
from resource.MainPage import Ui_MainPage
import threading

global Info,title_new
title_new,Info=[],[]
class MainPage(QMainWindow, Ui_MainPage):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        
        @param parent reference to the parent widget
        @type QWidget
        """

        super(MainPage, self).__init__()
        self.setupUi(self)
        self.SoundTip = SoundTip(self)
        self.Initial()


    def Initial(self):

        #查询数据
        self.Mongo_URl='localhost'
        self.Mongo_DB='Video'
        self.client=pymongo.MongoClient(self.Mongo_URl)
        self.db=self.client[self.Mongo_DB]
        self.Mongo_Table=self.db.list_collection_names()[0]
        self.Information=list(self.db[self.Mongo_Table].find())
        self.client.close()

        #数据初始化
        self.HomePageUrl_lineEdit.setText(self.Mongo_Table)
        row=self.Information_tableWidget.rowCount()
        Info_len=len(self.Information)
        while(row<Info_len):
            self.Information_tableWidget.insertRow(row)
            row=self.Information_tableWidget.rowCount()
        for i in range(len(self.Information)):
            self.Information_tableWidget.setItem(i, 0, QTableWidgetItem(self.Information[i]['title']))
            self.Information_tableWidget.setItem(i, 1, QTableWidgetItem(self.Information[i]['TimeLength']))
            if i==0:
                self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('最近更新'))
            else:
                self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('无更新'))

    def ChangeInfo_Table(self):
        global Info,title_new
        self.Info,self.title_new=Info,title_new
        self.title=[]
        for i in self.Information:
            self.title.append(i['title'])
        differ=[]
        if self.title_new != self.title:
            for i, value in enumerate(self.Info):
                if value['title'] in self.title:
                    self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('无更新'))
                else:
                    self.Information_tableWidget.insertRow(0)
                    self.Information_tableWidget.setItem(0, 0, QTableWidgetItem(value['title']))
                    self.Information_tableWidget.setItem(0, 1, QTableWidgetItem(value['TimeLength']))
                    self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('正在下载'))
                    differ.append(value) 
            self.Information_tableWidget.repaint()
            for i ,value in enumerate(differ):
                file_path='{0}/video/{1}.{2}'.format(os.getcwd(),value['title'],'mp4')
                header = {
                        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                                    "like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 "
                        }
                video=requests.get(value['video_url'],headers=header).content
                if not os.path.exists(file_path):
                    with open(file_path,'wb') as f:
                        f.write(video)
                        f.close()
                self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('更新完毕'))
                self.Information_tableWidget.repaint()
            self.Information=self.Info
            self.Mongo_Table=self.HomePageUrl_lineEdit.text()
            self.save_to_database(self.Information)

    def getHTMLText(self,url):
        try:
            header = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                              "like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 "
            }
            respond= requests.get(url, headers=header,timeout=30)
            time.sleep(0.1)
            return respond
        except:
            self.getHTMLText(url)



    def message(self, str0: str):
        QMessageBox.information(self, 'Hi', '{}'.format(str0), QMessageBox.Yes)  # 提示信息对话窗
        return

    def Stadandtime(self, t: str):
        t = t.split('-')
        iso_time = []
        this_year = datetime.date.today().year
        iso_time.append(this_year)
        iso_time.append(int(t[0]))
        iso_time.append(int(t[1]))
        m = datetime.date(iso_time[0], iso_time[1], iso_time[2])
        return m.isoformat()

    def save_to_database(self,result):
        if self.db[self.Mongo_Table].remove() and self.db[self.Mongo_Table].insert(result):
            self.client.close()
            return True
        else:
            return False
    
    @pyqtSlot()
    def on_Scrap_pushButton_clicked(self):
        self.url=self.HomePageUrl_lineEdit.text()
        self.get_info=Get_Info(self.url)
        self.get_info.Info_ready.connect(self.ChangeInfo_Table)
        self.get_info.start()

        self.Scrap_pushButton.setText("监听下载中...")
        self.Scrap_pushButton.setCheckable(False)
        self.Scrap_pushButton.repaint()
        threading.Timer(120,self.get_info.start()).start()

    @pyqtSlot(int, int)
    def on_Information_tableWidget_cellClicked(self, row, column):
        try:
            if self.Information:
                url = self.Information[row]['url']
                QtGui.QDesktopServices.openUrl(QtCore.QUrl(url))
            else:
                self.message('获取信息失败！')
        except Exception:
            self.message('请填写用户目标链接！')


class SoundTip(QThread):
    def __init__(self, parent=None, *args, **kwargs):
        super(SoundTip, self).__init__(parent, *args, **kwargs)
        self.sound_file = 'resource/images/tipSound.wav'
        self.sound = QSoundEffect()
        self.sound.setSource(PyQt5.QtCore.QUrl.fromLocalFile(self.sound_file))
        self.sound.setLoopCount(2)
        self.sound.setVolume(100)

    def run(self):
        self.sound.play()

class Get_Info(QThread):
    Info_ready=pyqtSignal()
    def __init__(self,url):
        super().__init__()
        self.url=url

    def TimeConvert(self, t: int):
        m, s = divmod(t, 60)
        b = "%02d:%02d" % (m, s)
        return b

    def getHTMLText(self,url):
        try:
            header = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                              "like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 "
            }
            respond= requests.get(url, headers=header,timeout=30)
            time.sleep(0.1)
            return respond
        except:
            self.getHTMLText(url)
    
    def get_videoUrl(self, url_s, id, times):
        pattern = r'http://tv.sohu.com/v/(.*?)==.html'
        suburl = re.findall(pattern, url_s)[0]

        # 获取videonew.do链接,并从中获取'su'、'ck'参数信息
        videonew_url = "https://my.tv.sohu.com/play/videonew.do?vid={0}&ver=&ssl=1&referer=https%3A%2F%2Ftv.sohu.com%2Fv%2F{1}%3D%3D.html&t={2}".format(
            id, suburl, times)
        # html=get_jsondata(videonew_url)
        html = self.getHTMLText(videonew_url)
        if html.content:
            html = html.json()
        su = html['data']['su'][0]
        ck = html['data']['ck'][0]

        # 通过获取的参数信息构成ip?new链接（包含后台视频链接的真正链接）
        ipnew_url = 'https://data.vod.itc.cn/ip?new={0}&num=1&key={1}&ch=pgc&pt=1&pg=2&prod=h5n&uid=15775043675348643281'.format(
            su, ck)
        # html=get_jsondata(ipnew_url)
        html = self.getHTMLText(ipnew_url)
        time.sleep(1)
        if html.content:
            html = html.json()
        url = html['servers'][0]['url']
        return url

    def openUrl(self,URL):
        tmp = self.getHTMLText(URL).text.strip()
        pattern = r'\"list\":\[(.*?)\]'
        tmp = re.findall(pattern, tmp)
        message = eval(tmp[0])
        Info0 = []
        for i in message:
            title = (i['title'])
            link = i['url']
            Timelength = self.TimeConvert(i['videoLength'])
            video_source = self.get_videoUrl(i['url'], i['id'], i['uploadTime'])
            Info0.append({'title':title, 'TimeLength':Timelength, 'url':link, 'video_url':video_source})
        return Info0

    def run(self):
        global Info
        global title_new
        if self.url == "https://tv.sohu.com/user/media/video.do?uid=293643430":
            self.url = "https://my.tv.sohu.com/user/wm/ta/v.do?callback=jQuery17208274530945288818_1577511351653&uid" \
                    "=293643430&pg=1&size=50&sortType=2&_=1577511351689 "
        Info = self.openUrl(self.url)
        for i in Info:
            title_new.append(i['title'])
        self.Info_ready.emit()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainPage()
    MainWindow.show()
    sys.exit(app.exec_())
