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
import requests
from datetime import datetime



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
        
        #interval
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.progress)
        self.timer.start()
    def stop(self):
        print('stop comand')
        self.position = 0
        self.duration = 0
        self.file = QMediaContent()
        self.state = 0
        self.timer.stop()
        return super().stop()
    def retunr_position(self):
        return self.position
       
    def position_changed(self, position):
        self.position = position
        
    def duration_changed(self, duration):
        self.duration = duration

    def state_changed(self, state):
        #delete file
    
        global STATUS_PLAYER
        if state == 0:
            STATUS_PLAYER = False
            
        else:
            STATUS_PLAYER = True
    
    def progress(self):


        try:
            operation = self.position / self.duration * 100
            format = "{:.2f}".format(operation)
            global PORCERNT
            PORCERNT = float(format)
        except:
            pass
        
        self.stackSignal.emit()
        
        
        return True
        

    
    

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
    
    
    
    
    
    def search_and_play(self,url):
       
        diretorio =  os.path.dirname(os.path.realpath(__file__))
        
        folder = diretorio + '\downloads\\'
        outtmpl = folder + '\%(title)s'+'.mp3'
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredquality': '192',
            }],
            

            
            
        }
  
            
        with YoutubeDL(ydl_opts) as ydl:
            
            #download and save file in folder
            try:
                ydl.download([url])
                
                
            except:
                pass
            
            #get thumbnail 
            info_dict = ydl.extract_info(url, download=False)
            thumbnail = info_dict.get('thumbnail', None)

            pix_map = QPixmap()
            pix_map.loadFromData(requests.get(thumbnail).content)
            
            
            self.video_label.setPixmap(pix_map)
            self.video_label.setScaledContents(True)
            

            
            #get file name
            info_dict = ydl.extract_info(url, download=False)
            #get duration
            duration = info_dict.get('duration', None)

            video_title = info_dict.get('title', None)
            self.set_titulo.setText(video_title)
            self.title_page2.setText(video_title)
            #inverter barra
            video_title = video_title.replace('/', '\\')
            video_title = video_title + '.mp3'
            print(video_title)
            
            #play file \
            patch = folder + video_title
            global CURRENT_PATCH 
            global STATUS_PLAYER
            print(CURRENT_PATCH,"CURRENT_PATCH")
            if STATUS_PLAYER == True:
                print("status ta ativo vamo parar")
                # stop thread


                #stop player

                
            
                self.player.stop()
                
                
                var_1= self.clok_resta_
                var_2= self.clok_start
             
                var_1.setText("00:00:00")
                var_2.setText("00:00:00")
                self.progress_music.setValue(0)
                

      
                if  CURRENT_PATCH == '' or CURRENT_PATCH == None:
                    pass
                else:
                    
                    self.player.setMedia(QMediaContent())
                    #remove file in player
                    
                    

                STATUS_PLAYER = False
                
            CURRENT_PATCH = patch
            print(CURRENT_PATCH,"novo patch")
            funcoes._Delete_Files(self)
            self.player.setMedia(QMediaContent(QUrl.fromLocalFile(patch)))
            self.player.play()

            funcoes.Player_statemnt(self,patch)
            self.adss.setCurrentWidget(self.page_video_img)
            
            return True
            
            # minutos 5 / 30 = 100
            
    
                
   
            
    def Player_statemnt(self, patch):
        self.clok_resta_.setText('00:00:00')
        self.clok_start.setText('00:00:00')
        self.progress_music.setValue(0)
        def thead(self):
               
           state = self.player.state()
           while True:
               if int(state) == 0 :
                   print("player parado")
                   break
               
               else:
                    time.sleep(0.1)
                    a = self.player.duration
                    b = self.player.position
                    # convert position to time
                    position = time.strftime('%H:%M:%S', time.gmtime(b / 1000))

                    # restante 
                    restante = a - b
                    restante = time.strftime('%H:%M:%S', time.gmtime(restante / 1000))
                    #set time in label
                    self.clok_start.setText(position)
                    self.clok_resta_.setText(restante)
                    #set progress bar
                

            
           

        thread = threading.Thread(target=thead , args=(self,) ,name='thread_player',daemon=True)
        thread.start()
        
        
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