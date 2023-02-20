from yt_dlp import *
import os
import psutil
import sys
from PySide2.QtCore import *
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2 import QtGui
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from formui import Ui_Form
from youtubesearchpython import VideosSearch
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
import urllib.request
import threading
import time
from PySide2.QtCore import QMetaObject, Qt
import requests
from datetime import datetime
from random import randint
from modules.testbottherad import Thead_Player
from modules.SearchThread import SearchThread


STATUS_PLAYER = False
PAUSE = False
PORCERNT = 0
CURRENT_PATCH = ''
TIMER_RUN = 0
TIMER_FULL = 0


class LoadImageRunnable(QRunnable):
    def __init__(self, url, callback):
        super().__init__()
        self.url = url
        self.callback = callback

    @Slot()
    def run(self):
        print('baixando imagem')
        pixmap = self.load_image(self.url)
        return self.callback(pixmap)

    
    def load_image(self, url):
        data = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(data)
        return pixmap
    

    








    
    
class funcoes(Ui_Form):



    def get_data_search(self, search):
        self.thread = SearchThread(search)
        self.thread.search_results.connect(lambda data:  funcoes.handle_search_results(self, data))
        self.thread.start()

    def handle_search_results(self, search_results):
        threadpool = QThreadPool.globalInstance()
        self.tableWidget.setRowCount(0)

        for i, result in enumerate(search_results):
            # print thumbnail
            print(result['thumbnail'])
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(result['link']))
            #  sem self para ser unico
            thumbnail_button = QPushButton()
            thumbnail_button.setIconSize(QtCore.QSize(100, 100))
            self.tableWidget.setCellWidget(i, 1, thumbnail_button)

            thumbnail_button.setObjectName(f"thumbnail_{i}")
            thumbnail_button.setStyleSheet("background-color: transparent; border: none;")
            # threadpool para baixar imagem em paralelo e nao travar a interface
            # para entendimento o lambda é uma função anonima que recebe o pixmap e o button e seta o icon do button com o pixmap retornado 
            #apartir do : é o retorno da função anonima antes do : é o que a função recebe como parametro 
            #exmplo pratico:
            #soma = lambda x, y: x + y
            #resultado = soma(2, 3)  # resultado é 5
            
            load_image_runnable = LoadImageRunnable(result['thumbnail'], lambda pixmap, button=thumbnail_button: button.setIcon(pixmap))
            threadpool.start(load_image_runnable)


            # self.thumbnail_button.setIcon(QIcon(result['thumbnail']))

            self.tableWidget.setItem(i, 2, QTableWidgetItem(result['title']))
            self.tableWidget.item(i, 2).setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            self.tableWidget.setItem(i, 3, QTableWidgetItem(result['duration']))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(result['view_count']))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(result['published_time']))
            # align center
            self.tableWidget.item(i, 3).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.item(i, 4).setTextAlignment(Qt.AlignCenter)
            self.tableWidget.item(i, 5).setTextAlignment(Qt.AlignCenter)




        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

    
    
    def search_and_play(self, url):
        directory = os.path.dirname(os.path.realpath(__file__))
        folder = directory + '\downloads\\'
        outtmpl = folder + '\%(title)s' + '.mp3'
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredquality': '192',
            }],
        }

        with YoutubeDL(ydl_opts) as ydl:
            # Download and save file in folder
            try:
                ydl.download([url])
            except:
                pass

            # Get thumbnail
            info_dict = ydl.extract_info(url, download=False)
            thumbnail = info_dict.get('thumbnail', None)
            pix_map = QPixmap()
            pix_map.loadFromData(requests.get(thumbnail).content)
            self.video_label.setPixmap(pix_map)
            self.video_label.setScaledContents(True)

            # Get file name
            info_dict = ydl.extract_info(url, download=False)
            # Get duration
            duration = info_dict.get('duration', None)
            video_title = info_dict.get('title', None)
            self.set_titulo.setText(video_title)
            self.title_page2.setText(video_title)
            # Invert bar
            video_title = video_title.replace('/', '\\')
            video_title = video_title + '.mp3'
            print(video_title)

            # Play file \
            patch = folder + video_title
            global CURRENT_PATCH
            global STATUS_PLAYER
            print(CURRENT_PATCH, "CURRENT_PATCH")
            if STATUS_PLAYER == True:
                print("status ta ativo vamo parar")
                # stop thread

                # stop player

                self.player.stop()

                self.clok_resta_.setText("00:00:00")
                self.clok_start.setText("00:00:00")
                self.progress_music.setValue(0)

                if CURRENT_PATCH == '' or CURRENT_PATCH == None:
                    pass
                else:
                    pass
                    # remove file in player

                STATUS_PLAYER = False

            CURRENT_PATCH = patch
            print(CURRENT_PATCH, "novo patch")
            funcoes._Delete_Files(self)
            #Start player
            self.adss.setCurrentWidget(self.page_video_img)
            return funcoes.start_thread(self,patch)


    def start_thread(self,patch):
        self.start_player = Thead_Player(patch)
        self.start_player.start()
        self.start_player.data_received.connect(lambda data: funcoes.Update_Ui(self,data))
        
    def stop_music(self):
        self.start_player.stop()

    def pause_music(self):
        global PAUSE
        if PAUSE == False:
            self.start_player.pause()
            self.pause_music.setIcon(QIcon(':/btn/image/resume.png'))

            PAUSE = True
        else:
            self.start_player.resume()
            self.pause_music.setIcon(QIcon(':/btn/image/pause.png'))
            PAUSE = False


    def _Delete_Files(self):
        
        def thead(self):
            _folder_ = os.path.dirname(os.path.realpath(__file__)) + '\downloads\\'
    
            for file in os.listdir(_folder_):
                if file.endswith(".mp3"):
                    if _folder_ + file == CURRENT_PATCH:
                        pass
                    else:
                        try:
                            os.remove(_folder_ + file)
                        except Exception as e:
                            pass
                else:
                    pass
        thread = threading.Thread(target=thead , args=(self,) ,name='thread_delet',daemon=True)
        thread.start()
        



    def Update_Ui(self,data):
        print(data)
        start = data['position']
        remaining = data['remaining']
        progress = data['percent_complete']
        print("update ui")
        self.clok_start.setText(start)
        self.clok_resta_.setText(remaining)
        self.progress_music.setValue(progress)