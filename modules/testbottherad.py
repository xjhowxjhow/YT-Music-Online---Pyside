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


class Thead_Player(QThread):
    data_received = Signal(dict)

    def __init__(self, audio):
        QThread.__init__(self)
        self.audio = audio
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.get_data_info)
        self.player.durationChanged.connect(self.get_data_info)



    def run(self):
        try:
            self.play(self.audio)
        except Exception as e:
            print(e)
            
            self.handle_data(False)  # call handle_data function with False

    def status(self):
        return self.player.state()            

    def pause(self):
        print('pause')
        self.player.pause()
        
    def resume(self):
        print('resume')
        self.player.play()
        
    def stop(self):
        self.player.stop()
        print('stop')
        

    def play(self, url):
        # file patach
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(url)))
        self.player.play()
        print('play')
        

    def handle_data(self, data):
        # Function to handle data received from the API
        if data:
            self.data_received.emit(data)
        else:
            self.data_received.emit(False)
            print("Error request")

    
    def somavalor(self,n,n2):
        print('sum:'+str(n)+'+'+str(n2))
        return print(n+n2)
    

    def get_data_info(self):
        position = self.player.position()
        duration = self.player.duration()
        if duration > 0:
            remaining = duration - position
            position_str = time.strftime('%H:%M:%S', time.gmtime(position / 1000))
            remaining_str = time.strftime('%H:%M:%S', time.gmtime(remaining / 1000))
            duration_str = time.strftime('%H:%M:%S', time.gmtime(duration / 1000))
            percent_complete = int((position / duration) * 100)
            data = {
                'position': position_str,
                'remaining': remaining_str,
                'percent_complete': percent_complete,
                'duration': duration_str
            }
            self.data_received.emit(data)

