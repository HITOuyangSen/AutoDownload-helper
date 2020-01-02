# -*- coding: utf-8 -*-

"""
Module implementing MainPage.
"""
import sys, os
import threading
import PyQt5
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import pyqtSlot, QThread
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QAbstractItemView, QMessageBox
from PyQt5.QtMultimedia import QSoundEffect
import requests
import re
import datetime
import json
import pymongo
from resource.MainPage import Ui_MainPage


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

        super(MainPage, self).__init__(parent)
        self.setupUi(self)
        self.Information_tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.SoundTip = SoundTip(self)
        self.Scrap_pushButton.clicked.connect(self.on_Scrap_pushButton_clicked)
        self.Mongo_URl = 'localhost'
        self.Mongo_DB = 'Video'
        self.client = pymongo.MongoClient(self.Mongo_URl)
        self.db = self.client[self.Mongo_DB]
        self.Mongo_Table = self.db.list_collection_names()[0]
        self.Information = list(self.db[self.Mongo_Table].find())
        self.Initial()
        self.HomePageUrl_lineEdit.setText(self.Mongo_Table)

    def Initial(self):
        row = self.Information_tableWidget.rowCount()
        Info_len = len(self.Information)
        while (row < Info_len):
            self.Information_tableWidget.insertRow(row)
            row = self.Information_tableWidget.rowCount()
        for i in range(len(self.Information)):
            self.Information_tableWidget.setItem(i, 0, QTableWidgetItem(self.Information[i]['title']))
            self.Information_tableWidget.setItem(i, 1, QTableWidgetItem(self.Information[i]['TimeLength']))
            if i == 0:
                self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('最近更新'))
            else:
                self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('无更新'))

    def getHTMLText(self, url):
        try:
            header = {
                "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                              "like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 "
            }
            r = requests.get(url, headers=header)
            if type(r) is not None:
                return r
            else:
                self.getHTMLText(url)
        except:
            self.getHTMLText(url)

    def TimeConvert(self, t: int):
        m, s = divmod(t, 60)
        b = "%02d:%02d" % (m, s)
        return b

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

    def get_videoUrl(self, url_s, id, time):

        pattern = r'http://tv.sohu.com/v/(.*?)==.html'
        suburl = re.findall(pattern, url_s)[0]

        # 获取videonew.do链接,并从中获取'su'、'ck'参数信息
        videonew_url = "https://my.tv.sohu.com/play/videonew.do?vid={0}&ver=&ssl=1&referer=https%3A%2F%2Ftv.sohu.com%2Fv%2F{1}%3D%3D.html&t={2}".format(
            id, suburl, time)
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
        if html.content:
            html = html.json()
        url = html['servers'][0]['url']
        return url

    def openurl(self, url):
        Info = self.getHTMLText(url).text.strip()
        pattern = r'\"list\":\[(.*?)\]'
        tmp = re.findall(pattern, Info)
        message = eval(tmp[0])
        data = []
        for i in message:
            title = (i['title'])
            link = i['url']
            Timelength = self.TimeConvert(i['videoLength'])
            video_source = self.get_videoUrl(i['url'], i['id'], i['uploadTime'])
            data.append({'title': title, 'TimeLength': Timelength, 'url': link, 'video_url': video_source})
        return data

    def save_to_database(self, result):
        if self.db[self.Mongo_Table].remove() and self.db[self.Mongo_Table].insert(result):
            return True
        else:
            return False

    @pyqtSlot()
    def on_Scrap_pushButton_clicked(self):
        def mask():
            url = self.HomePageUrl_lineEdit.text()
            if url == "https://tv.sohu.com/user/media/video.do?uid=293643430":
                url = "https://my.tv.sohu.com/user/wm/ta/v.do?callback=jQuery17208274530945288818_1577511351653&uid" \
                      "=293643430&pg=1&size=50&sortType=2&_=1577511351689 "
            self.Info = self.openurl(url)
            title = []
            for i in self.Information:
                title.append(i['title'])
            title_new = []
            for i in self.Info:
                title_new.append(i['title'])
            if title_new != title:
                for i, value in enumerate(self.Info):
                    if value['title'] in title:
                        self.Information_tableWidget.setItem(i, 2, QTableWidgetItem('无更新'))
                    else:
                        self.Information_tableWidget.insertRow(0)
                        self.Information_tableWidget.setItem(0, 0, QTableWidgetItem(value['title']))
                        self.Information_tableWidget.setItem(0, 1, QTableWidgetItem(value['TimeLength']))
                        file_path = '{0}/video/{1}.{2}'.format(os.getcwd(), value['title'], 'mp4')
                        header = {
                            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, "
                                          "like Gecko) Chrome/79.0.3945.88 Mobile Safari/537.36 "
                        }
                        video = requests.get(value['video_url'], headers=header).content
                        DownLoad_statu = '正在下载'
                        self.Information_tableWidget.setItem(i, 2, QTableWidgetItem(DownLoad_statu))
                        if not os.path.exists(file_path):
                            with open(file_path, 'wb') as f:
                                f.write(video)
                                f.close()
                        DownLoad_statu = '下载完毕'
                        self.Information_tableWidget.setItem(i, 2, QTableWidgetItem(DownLoad_statu))
                    self.SoundTip.start()
                self.Information = self.Info
                self.save_to_database(self.Information)
            self.Mongo_Table = url
            threading.Timer(300, mask).start()

        self.Scrap_pushButton.setText("监听下载中...")
        self.Scrap_pushButton.setCheckable(False)
        self.Scrap_pushButton.repaint()
        mask()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainPage()
    MainWindow.show()
    sys.exit(app.exec_())
