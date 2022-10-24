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
from datetime import datetime

GLOBAL_TOGLE = False

class Effects (Ui_Form):
    
    def slide_content_ads(self):
        self.adss.setTransitionDirection(QtCore.Qt.Horizontal)
        self.adss.setTransitionSpeed(200)
        self.adss.setTransitionEasingCurve(QtCore.QEasingCurve.InOutExpo)
        self.adss.setSlideTransition(True)

    def togle_resize(self):
        global GLOBAL_TOGLE
        if GLOBAL_TOGLE == False:
            self.animation = QtCore.QPropertyAnimation(self.menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(65)
            self.animation.setEndValue(250)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutExpo)
            self.animation.start()


            
            
            GLOBAL_TOGLE = True
        else:
            self.animation = QtCore.QPropertyAnimation(self.menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(250)
            self.animation.setEndValue(65)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutExpo)
            self.animation.start()
            
            GLOBAL_TOGLE = False