
from yt_dlp import *
import os
from PySide2.QtCore import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent
from PySide2.QtCore import QUrl
from formui import Ui_Form
import sys
from modules.fun import *
from modules.effects import * 




class MainWindow (Ui_Form,QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.show()
        self.app = QCoreApplication.instance()
        #shadow
        self.shadow = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        
        self.shadow.setColor(QColor(0, 0, 0, 100))
        
        self.tableWidget.setGraphicsEffect(self.shadow)

        # self.tableWidget.setStyleSheet("QWidget { color: #000000; border-radius:0px; } QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px; border-radius:0px; } QTableWidget { gridline-color: #fffff8; border-radius:0px; border-radius:0px; } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item { border-bottom: 0.5px solid qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 0), stop:0.45677 rgba(0, 0, 0, 0), stop:0.479846 rgba(255, 255, 255, 255), stop:0.50571 rgba(239, 236, 55, 0), stop:1 rgba(239, 236, 55, 0)); border-radius:0px; } QTableView::item:selected{ background-color: rgba(0, 0, 0,255); color: rgb(255, 255, 255); } QScrollBar:horizontal { border: 1px solid #2A2929; background: #2A2929; height: 7px; margin: 0px 21px 0 21px; } QScrollBar::handle:horizontal { background: #646464; min-width: 5px; } QScrollBar::add-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: right; subcontrol-origin: margin; } QScrollBar::sub-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: left; subcontrol-origin: margin; } QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { background: none; } QScrollBar:vertical { border: none; background: rgb(45, 45, 68); width: 5px; margin: 15px 0 15px 0; border-radius: 0px; } /*  HANDLE BAR VERTICAL */ QScrollBar::handle:vertical { background-color: rgb(80, 80, 122); min-height: 30px; border-radius: 7px; } QScrollBar::handle:vertical:hover{ background-color: rgb(255, 0, 127); } QScrollBar::handle:vertical:pressed { background-color: rgb(185, 0, 92); } /* BTN TOP - SCROLLBAR */ QScrollBar::sub-line:vertical { border: none; background-color: rgb(59, 59, 90); height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(255, 0, 127); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(185, 0, 92); } /* BTN BOTTOM - SCROLLBAR */ QScrollBar::add-line:vertical { border: none; background-color: rgb(59, 59, 90); height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; subcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(255, 0, 127); } QScrollBar::add-line:vertical:pressed { background-color: rgb(185, 0, 92); } /* RESET ARROW */ QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }")
        #vertical style
        self.shadow2 = QtWidgets.QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 100))
        self.group_options_player.setGraphicsEffect(self.shadow2)
        
        #effects
        Effects.slide_content_ads(self)
        

        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #event filter
        self.togle.installEventFilter(self)
        self.btn_procurar.installEventFilter(self)
        self.play_music.installEventFilter(self)
        self.stop_music.installEventFilter(self)
        self.pause_music.installEventFilter(self)
        self.control_vol.installEventFilter(self)
        self.lineEdit.installEventFilter(self)
        self.back_content.installEventFilter(self)
        self.back_buscar.installEventFilter(self)
        #COLUNA URL
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(6, True)
        self.tableWidget.horizontalHeader().setVisible(False)
        #focus
        self.tableWidget.setFocusPolicy(Qt.NoFocus)

        
        
    def eventFilter(self, obj, event):
        if obj == self.togle and event.type() == QtCore.QEvent.MouseButtonPress:
            return Effects.togle_resize(self)
         
        if obj == self.back_content and event.type() == QtCore.QEvent.MouseButtonPress:
            
            self.adss.setCurrentWidget(self.page_video_img)
            return True
        if obj == self.back_buscar and event.type() == QtCore.QEvent.MouseButtonPress:
            
            self.adss.setCurrentWidget(self.adssPage1)
            return True
        
        #double CLICK ROW TABLE
        if obj == self.tableWidget.currentRow() and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("double click")
            current_row = self.tableWidget.currentRow()
            url = self.tableWidget.item(current_row, 0).text()
            funcoes.search_and_play(self,url)
            return True
        #EVENTS AP
        if obj == self.lineEdit and event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_Return and self.lineEdit.hasFocus():
                text_search = self.lineEdit.text()
                if text_search == "":
                    pass
                    return True
                else:
                    funcoes.get_data_search(self,str(text_search))
                return True
            return False
            
            
            
        if obj == self.btn_procurar and event.type() == QtCore.QEvent.MouseButtonPress:
            text_search = self.lineEdit.text()
            
            if text_search == "":
                pass
            else:
                funcoes.get_data_search(self,str(text_search))
            return True
        
        if obj == self.play_music and event.type() == QtCore.QEvent.MouseButtonPress:
            current_row = self.tableWidget.currentRow()
            url = self.tableWidget.item(current_row, 0).text()
            funcoes.search_and_play(self,url)
            return True
        if obj == self.pause_music and event.type() == QtCore.QEvent.MouseButtonPress:
            funcoes.pause_music(self)
            return True
        if obj == self.stop_music and event.type() == QtCore.QEvent.MouseButtonPress:
            funcoes.stop_music(self)
            return True
        
        #volume event slider sroll  
        if obj == self.control_vol and event.type() == QtCore.QEvent.MouseButtonRelease or event.type() == QtCore.QEvent.Scroll:
            
            value = self.control_vol.value()
            funcoes.Volume(self,value)
            return True
        
        return super(MainWindow,self).eventFilter(obj, event)

        

        
        
        
        
if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit()
    
    