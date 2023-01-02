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



STATUS_PLAYER = False
PAUSE = False
PORCERNT = 0
CURRENT_PATCH = ''
TIMER_RUN = 0
TIMER_FULL = 0


class Player(QMediaPlayer):
    stackSignal = QtCore.Signal()
    def __init__(self):
        super().__init__()
        #print current file
        self.file = QMediaContent()
        
    
        self.positionChanged.connect(self.position_changed)
        self.durationChanged.connect(self.duration_changed)
        self.stateChanged.connect(self.state_changed)
        
    def stop(self):
    
        global STATUS_PLAYER
        STATUS_PLAYER = False
        return super().stop()

    def retunr_position(self):
        return self.position
       
    def position_changed(self, position):
        self.position = position
        
    def duration_changed(self, duration):
        self.duration = duration

    def state_changed(self, state):

        global STATUS_PLAYER
        if state == 0:
            STATUS_PLAYER = False
            
        else:
            STATUS_PLAYER = True
        

    

class WorkerSignals(QObject):
     def __init__(self, parent=None):
         super().__init__(parent)
         finished = Signal()
         error = Signal(tuple)
         result = Signal(object)
         progress = Signal(int)
        # Add other signals here
    
class Worker(QRunnable):
    def __init__(self, function, *args, **kwargs):
        super(Worker, self).__init__()
        self.function = function
        self.args = args
        self.kwargs = kwargs

    @Slot()
    def run(self):
        self.function(*self.args, **self.kwargs)


    
    
class funcoes(Ui_Form):


    def get_data_search(self, search):
        font = QFont()
        font.setFamily(u"Bahnschrift Light SemiCondensed")
        font.setPointSize(11)
        cont = self.tableWidget.rowCount()
        if cont > 0:
            for i in range (cont): 
                if self.tableWidget.rowCount() >= 0:
                    self.tableWidget.removeRow(self.tableWidget.rowCount()-1)


        videosSearch = VideosSearch(search+" vevo", limit = 30)
        videosResult = videosSearch.result()
    
        for video in videosResult['result']:
            print(video['title'], video['link'], video['duration'])

            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            #link
            self.tableWidget.setItem(rowPosition , 0, QTableWidgetItem(video['link']))
            

            #thumb
            self.pushButton_pago = QPushButton()
            self.pushButton_pago.setObjectName("thumbnaill")


            #download image em set background
            url = video['thumbnails'][0]['url']
            data = urllib.request.urlopen(url).read()
            image = QtGui.QImage()
            image.loadFromData(data)
            pixmap = QtGui.QPixmap(image)
            
            self.video_label.setScaledContents(True)
            self.pushButton_pago.setIconSize(QtCore.QSize(200, 200))
            self.pushButton_pago.setIcon(QIcon(pixmap))
            #set background image
            self.tableWidget.setCellWidget(rowPosition, 1, self.pushButton_pago)

            #title
            self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(video['title']))
            #non editable
            self.tableWidget.item(rowPosition, 2).setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            #DUration
            self.tableWidget.setItem(rowPosition , 3, QTableWidgetItem(video['duration']))
            #view
            self.tableWidget.setItem(rowPosition , 4, QTableWidgetItem(video['viewCount']['short']))
            #tempo publicado
            self.tableWidget.setItem(rowPosition , 5, QTableWidgetItem(video['publishedTime']))

        #block editables
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
        return True
    
    
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
                    self.player.setMedia(QMediaContent())
                    # remove file in player

                STATUS_PLAYER = False

            CURRENT_PATCH = patch
            print(CURRENT_PATCH, "novo patch")
            funcoes._Delete_Files(self)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(patch)))
            self.player.play()

            self.adss.setCurrentWidget(self.page_video_img)

            funcoes._start_thread(self)

    def _start_thread(self):
        instance = QThreadPool.globalInstance()
        run = funcoes.Player_statemnt
        thread = Worker(run, self)
        instance.start(thread)
        # fisnish thread

        return True

    def Player_statemnt(self): # thread
        self.clok_resta_.setText('00:00:00')
        self.clok_start.setText('00:00:00')
        self.progress_music.setValue(0)
        global STATUS_PLAYER
        while STATUS_PLAYER == True:
            QThread.msleep(1000)
            if self.player.state() == 0:

                QMetaObject.invokeMethod(self, "Terminated", Qt.QueuedConnection)
                STATUS_PLAYER = False

                break

            print("atualizando")

            QMetaObject.invokeMethod(self, "Update_Ui", Qt.QueuedConnection)

    def Update_Ui(self):
        
        self.boasvindas_2.setText("Aguarde, carregando..." + str(randint(0, 100)))
        a = self.player.duration
        b = self.player.position
        # convert position to time
        position = time.strftime('%H:%M:%S', time.gmtime(b / 1000))   
        # remaining 
        remaining = a - b
        remaining = time.strftime('%H:%M:%S', time.gmtime(remaining / 1000))
        # set time in label
        self.clok_start.setText(position)
        # time.sleep(0.1)
        self.clok_resta_.setText(remaining)
        # set progress bar
        operation = b/ a * 100
        format = "{:.2f}".format(operation)
        # int format
        print("working, player")
        self.progress_music.setValue(int(float(format)))
        return True
    
    def Terminated_Music(self):
        self.clok_resta_.setText('00:00:00')
        self.clok_start.setText('00:00:00')
        self.progress_music.setValue(0)
        self.player.stop()
        
        return True
    
    def Pause(self):
        global STATUS_PLAYER
        global PAUSE
        if STATUS_PLAYER == True:
            if PAUSE == False:
                self.player.pause()
                PAUSE = True
                self.pause_music.setIcon(QIcon(':/btn/image/resume.png'))
            else:
                self.player.play()
                PAUSE = False
                self.pause_music.setIcon(QIcon(':/btn/image/pause.png'))
         

        else:
            pass


    def Stop(self):
        self.player.stop()

        self.clok_resta_.setText('00:00:00')
        self.clok_start.setText('00:00:00')
        self.progress_music.setValue(0)
        time.sleep(0.5)
        self.player.setMedia(QMediaContent(None))
        #remove file in player

        global STATUS_PLAYER
        STATUS_PLAYER = False
        instance = QThreadPool.globalInstance()
        instance.clear()
        funcoes._Delete_Files(self)

        return True


    def Volume(self,value):
        self.player.setVolume(value)




    def Progress_bar(self):
        global PORCERNT
        self.progress_music.setValue(PORCERNT)
        
        
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