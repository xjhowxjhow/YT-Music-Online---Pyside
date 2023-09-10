
from core import *
from formui import Ui_Form
from modules.fun import *
from modules.effects import * 


class MainWindow (Ui_Form,QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.show()
        self.app = QCoreApplication.instance()
        Effects.slide_content_ads(self)
        
        #SHADOW
        #////////////////////////////////////////////////////////////////////////////////////

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setColor(QColor(0, 0, 0, 100))        
        self.tableWidget.setGraphicsEffect(self.shadow)
        
        self.shadow2 = QGraphicsDropShadowEffect(self)
        self.shadow2.setBlurRadius(20)
        self.shadow2.setXOffset(0)
        self.shadow2.setColor(QColor(0, 0, 0, 100))
        self.group_options_player.setGraphicsEffect(self.shadow2)
        
        #EFFECTS 
        #////////////////////////////////////////////////////////////////////////////////////
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
        self.progress_music.installEventFilter(self)
        #COLUNA URL
        self.tableWidget.setColumnHidden(0, True)
        self.tableWidget.setColumnHidden(6, True)
        self.tableWidget.horizontalHeader().setVisible(False)
        #focus
        self.tableWidget.setFocusPolicy(Qt.NoFocus)

        
        
    def eventFilter(self, obj, event):
        if obj == self.togle and event.type() == QEvent.MouseButtonPress:
            return Effects.togle_resize(self)
         
        if obj == self.back_content and event.type() == QEvent.MouseButtonPress:
            
            self.adss.setCurrentWidget(self.page_video_img)
            return True
        if obj == self.back_buscar and event.type() == QEvent.MouseButtonPress:
            
            self.adss.setCurrentWidget(self.adssPage1)
            return True
        
        if obj == self.tableWidget.currentRow() and event.type() == QEvent.MouseButtonDblClick:
            print("double click")
            current_row = self.tableWidget.currentRow()
            url = self.tableWidget.item(current_row, 0).text()
            funcoes.search_and_play(self,url)
            return True
        #EVENTS AP
        if obj == self.lineEdit and event.type() == QEvent.KeyPress:
            if event.key() == Qt.Key_Return and self.lineEdit.hasFocus():
                text_search = self.lineEdit.text()
                if text_search == "":
                    pass    
                    return True
                else:
                    funcoes.get_data_search(self,str(text_search))
                return True
            return False
            
            
            
        if obj == self.btn_procurar and event.type() == QEvent.MouseButtonPress:
            text_search = self.lineEdit.text()
            
            if text_search == "":
                pass
            else:
                funcoes.get_data_search(self,str(text_search))
            return True
        
        if obj == self.play_music and event.type() == QEvent.MouseButtonPress:
            current_row = self.tableWidget.currentRow()
            url = self.tableWidget.item(current_row, 0).text()
            funcoes.search_and_play(self,url)
            return True
        if obj == self.pause_music and event.type() == QEvent.MouseButtonPress:
            funcoes.pause_music(self)
            return True
        if obj == self.stop_music and event.type() == QEvent.MouseButtonPress:
            funcoes.stop_music(self)
            return True
        #volume event slider sroll  
        if obj == self.control_vol and event.type() == QEvent.MouseButtonRelease or event.type() == QEvent.Scroll:
            
            value = self.control_vol.value()
            funcoes.Volume(self,value)
            return True

        if obj ==self.progress_music and event.type() == QEvent.MouseButtonRelease:
            funcoes.update_progress(self)
            return True
        
        return super(MainWindow,self).eventFilter(obj, event)

        

        
        
        
        
if __name__ == '__main__':
    os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    app =QApplication(sys.argv)
    mainWin = MainWindow()
    ret = app.exec_()
    sys.exit()
    
    