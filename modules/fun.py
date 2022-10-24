from yt_dlp import *
import os
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
            # print(i)
            # print(i['id'])
            # print(i['title'])
            # print(i['duration'])
            # print(i['viewCount']['short'])
            # print(i['thumbnails'][0]['url'])
            # print(i['channel']['name'])
            # print(i['channel']['link'])
            # print(i['channel']['id'])
            # print(i['link'])
            # print(i['publishedTime'])
            # print(i['descriptionSnippet'])
            # print('----------------------------------------')
        videosSearch = VideosSearch(search+" vevo", limit = 30)
        videosResult = videosSearch.result()
        index = 0
    
        for video in videosResult['result']:
            print(video['title'], video['link'], video['duration'])

            
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            #0ulr
            #1thumb
            #2title
            #3duration
            #4views
            #5data
            #button play
            
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
            #set background image in label
            #remove pixmap
      
            

            
            self.video_label.setScaledContents(True)
            self.pushButton_pago.setIconSize(QtCore.QSize(200, 200))
            self.pushButton_pago.setIcon(QIcon(pixmap))
            #set background image
            self.tableWidget.setCellWidget(rowPosition, 1, self.pushButton_pago)
            #editable off
            
            
            
            
            
            self.tableWidget.setItem(rowPosition , 2, QTableWidgetItem(video['title']))
            #non editable
            self.tableWidget.item(rowPosition, 2).setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled)
            
            self.tableWidget.setItem(rowPosition , 3, QTableWidgetItem(video['duration']))
            
            
            self.tableWidget.setItem(rowPosition , 4, QTableWidgetItem(video['viewCount']['short']))
            
            
            self.tableWidget.setItem(rowPosition , 5, QTableWidgetItem(video['publishedTime']))
            
            
            #PLAY BUTTON
            # self.play_23 = QPushButton("Play")
            # self.tableWidget.setCellWidget(rowPosition , 6, QTableWidgetItem(self.play_23))
            index += 1
        

        #block editables
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
    
        return True
    
    
    
    
    
    def search_and_play(self,url):
       
        diretorio =  os.path.dirname(os.path.realpath(__file__))
        
        folder = diretorio + '\downloads\\'
        outtmpl = folder + '\%(title)s.%(ext)s'
        ydl_opts = {
            #legendas
            'writesubtitles': True,
            'subtitleslangs': ['pt','en'],
            'subtitlesformat': 'srt',
            
            
            

            # audio

            'format': 'bestaudio/best',
            'outtmpl': outtmpl,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
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
            video_title = video_title + '.webm'
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
                while var_1.text() and var_2.text() == "00:00:00":
                    var_1.setText("00:00:00")
                    var_2.setText("00:00:00")
                    self.progress_music.setValue(0)
                

                try:
                    if CURRENT_PATCH:
                        url_none= ''
                        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url_none)))
                        os.remove(CURRENT_PATCH)
                        print("removido")
                    else:
                        print("nao tem nada pra remover")
                        pass
                except:
                    print("nao tem nada pra remover")
                    pass
                STATUS_PLAYER = False
                
            CURRENT_PATCH = patch
            print(CURRENT_PATCH,"novo patch")
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
            current_row = self.tableWidget.currentRow()

            full_duration = self.tableWidget.item(current_row, 3).text() #06:00
            progress_full=  full_duration.split(':') 
            full_duration = full_duration.split(':')
            
            
            print(full_duration)
            if len(full_duration) == 2:
                #ate´9:59
                minute = int(full_duration[0])
                second = int(full_duration[1])
                full_duration = (minute * 60) + second
                convert = time.strftime('%H:%M:%S', time.gmtime(full_duration))
            else:
                pass
    
                

            
            time_start = time.time()
            global STATUS_PLAYER
            STATUS_PLAYER = True
            global PAUSE
            PAUSE = False
            global PORCERNT 
            
            
            while STATUS_PLAYER == True:

                if PAUSE == False:
                    
                    time.sleep(1)
                    #convert time
                    time_end = time.time()
                    time_total = time_end - time_start
                    time_total = time.strftime("%H:%M:%S", time.gmtime(time_total))
                    #set time
                    self.clok_start.setText(time_total)
                    #left time
                    time_1 = datetime.strptime(convert,"%H:%M:%S")
                    time_2 = datetime.strptime(time_total,"%H:%M:%S")
                    time_left = time_1 - time_2
                    time_left = str(time_left)
                    
                    #Progress bar

            
                        
                    #unifica minutos e segundos
                   
                    
                    if time_left == '0:00:00':
                        self.player.stop()
                        url_none = ''
                        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url_none)))
                        STATUS_PLAYER = False
                        
                        #delete file
                        os.remove(patch)
                        
                        break
                    self.clok_resta_.setText(time_left)
                else:
                    print("pausado")
                    print(convert,time_total)
                    
                    pass
            #delete file
           

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
        url_none = ''
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url_none)))
        global STATUS_PLAYER
        STATUS_PLAYER = False
        global CURRENT_PATCH
        os.remove(CURRENT_PATCH)
        #stop thread player

        return True
        
    def Volume(self,value):
        self.player.setVolume(value)




    def Progress_bar(self):
        global PORCERNT
        self.progress_music.setValue(PORCERNT)
        
        
        