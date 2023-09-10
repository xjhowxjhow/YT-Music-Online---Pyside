#Pyside Core
from PySide2.QtCore import QEvent,QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject,QThreadPool, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent,QRunnable,QThread,QEasingCurve,Slot,Signal
from PySide2.QtGui import QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient
from PySide2.QtWidgets import QPushButton,QTableWidgetItem,QAbstractItemView,QGraphicsDropShadowEffect,QApplication,QWidget
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
#Tools
import os 
import sys
import time
import urllib
from random import randint
import threading
# Libs Core
from yt_dlp import *
from youtubesearchpython import VideosSearch
import requests
# Ui 
from ui.formui import Ui_Form
