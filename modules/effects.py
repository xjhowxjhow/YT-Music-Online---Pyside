from core import *

GLOBAL_TOGLE = False

class Effects (Ui_Form):
    
    def slide_content_ads(self):
        self.adss.setTransitionDirection(Qt.Horizontal)
        self.adss.setTransitionSpeed(200)
        self.adss.setTransitionEasingCurve(QEasingCurve.InOutExpo)
        self.adss.setSlideTransition(True)

    def togle_resize(self):
        global GLOBAL_TOGLE
        if GLOBAL_TOGLE == False:
            self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(60)
            self.animation.setEndValue(250)
            self.animation.setEasingCurve(QEasingCurve.InOutExpo)
            self.animation.start()


            
            
            GLOBAL_TOGLE = True
        else:
            self.animation = QPropertyAnimation(self.menu, b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(250)
            self.animation.setEndValue(60)
            self.animation.setEasingCurve(QEasingCurve.InOutExpo)
            self.animation.start()
            
            GLOBAL_TOGLE = False
            
            
