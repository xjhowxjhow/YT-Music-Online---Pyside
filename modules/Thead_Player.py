from core import *

class Thead_Player(QThread):
    data_received = Signal(dict)

    def __init__(self, audio):
        QThread.__init__(self)
        self.audio = audio
        self.player = QMediaPlayer()
        self.player.positionChanged.connect(self.get_data_info)




    def run(self):
        try:
            self.play(self.audio)
        except Exception as e:
            print(e)
            
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
        
        
    def volume(self, value):
        print('volume:'+str(value))
        self.player.setVolume(value)

    def progress(self, value):
        value = (value / 100) * self.player.duration()
        self.player.setPosition(int(value))
        


    def monitor(self):
        print('-----UPDATE PROGRESS-----')
        print('tempo atual: '+str(self.player.position()) + 'ms')
        print('tempo total: '+str(self.player.duration()) + 'ms')
        print('nova posicao: '+str(self.player.position()) + 'ms')
        print('-------------------------')
        
        
    def get_data_info(self):
        
        position = self.player.position()
        duration = self.player.duration()

        if position == duration:
            print('finish')
        else:
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
    
