from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from modules.custom_qstacked_widgets import *

import sources






class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(958, 827)
        Form.setStyleSheet(u"font-size:14px;\n"
"font-family: \"Bahnschrift Light SemiCondensed\";\n"
"color:rgb(255,255,255);")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        self.stackedWidget.setFrameShadow(QFrame.Raised)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.stackedWidget.addWidget(self.login)
        self.main = QWidget()
        self.main.setObjectName(u"main")
        self.main.setStyleSheet(u"\n"
"background-position: center;\n"
"\n"
"background-repeat:no-repeat;\n"
"border: 0px;\n"
"color: rgb(0, 0, 0);")
        self.verticalLayout = QVBoxLayout(self.main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.uimain = QFrame(self.main)
        self.uimain.setObjectName(u"uimain")
        self.uimain.setMaximumSize(QSize(16777215, 16777215))
        self.uimain.setStyleSheet(u"")
        self.uimain.setFrameShape(QFrame.StyledPanel)
        self.uimain.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.uimain)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menu = QFrame(self.uimain)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(60, 0))
        self.menu.setMaximumSize(QSize(60, 16777215))
        self.menu.setStyleSheet(u"background-image: url();\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"")
        self.menu.setFrameShape(QFrame.NoFrame)
        self.menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.menu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainlogo = QFrame(self.menu)
        self.mainlogo.setObjectName(u"mainlogo")
        self.mainlogo.setMinimumSize(QSize(0, 90))
        self.mainlogo.setMaximumSize(QSize(16777215, 90))
        self.mainlogo.setStyleSheet(u"border-bottom: 1px solid rgba(0, 0, 0,70);")
        self.mainlogo.setFrameShape(QFrame.StyledPanel)
        self.mainlogo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.mainlogo)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.mainlogo)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(60, 60))
        self.frame_8.setMaximumSize(QSize(100, 16777215))
        self.frame_8.setStyleSheet(u"background-image: url(:/fundo/60x60.png);\n"
"background-position: center;\n"
"background-repeat:no-repeat;\n"
"background-color: rgba(0, 0, 0, 0); \n"
"border:none;\n"
"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_8)

        self.label = QLabel(self.mainlogo)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Bahnschrift Light SemiCondensed")
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"border:none;")

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.mainlogo)

        self.categorias = QFrame(self.menu)
        self.categorias.setObjectName(u"categorias")
        self.categorias.setStyleSheet(u"")
        self.categorias.setFrameShape(QFrame.StyledPanel)
        self.categorias.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.categorias)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.scrolbar = QFrame(self.categorias)
        self.scrolbar.setObjectName(u"scrolbar")
        self.scrolbar.setMinimumSize(QSize(4, 0))
        self.scrolbar.setMaximumSize(QSize(4, 16777215))
        self.scrolbar.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);")
        self.scrolbar.setFrameShape(QFrame.StyledPanel)
        self.scrolbar.setFrameShadow(QFrame.Raised)
        self.animcurretnpage = QFrame(self.scrolbar)
        self.animcurretnpage.setObjectName(u"animcurretnpage")
        self.animcurretnpage.setGeometry(QRect(0, 0, 4, 60))
        self.animcurretnpage.setMinimumSize(QSize(4, 60))
        self.animcurretnpage.setMaximumSize(QSize(4, 10))
        self.animcurretnpage.setStyleSheet(u"background-color: rgb(0, 85, 255);")
        self.animcurretnpage.setFrameShape(QFrame.HLine)
        self.animcurretnpage.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_5.addWidget(self.scrolbar)

        self.topmenu = QFrame(self.categorias)
        self.topmenu.setObjectName(u"topmenu")
        self.topmenu.setMinimumSize(QSize(0, 0))
        self.topmenu.setMaximumSize(QSize(250, 16777215))
        self.topmenu.setSizeIncrement(QSize(0, 20))
        self.topmenu.setStyleSheet(u"")
        self.topmenu.setFrameShape(QFrame.StyledPanel)
        self.topmenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topmenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.togle = QPushButton(self.topmenu)
        self.togle.setObjectName(u"togle")
        self.togle.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"Bahnschrift Light SemiCondensed")
        self.togle.setFont(font1)
        self.togle.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon = QIcon()
        icon.addFile(u":/btn/image/togle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.togle.setIcon(icon)
        self.togle.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.togle)

        self.busca = QPushButton(self.topmenu)
        self.busca.setObjectName(u"busca")
        self.busca.setMinimumSize(QSize(50, 0))
        self.busca.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setFamily(u"Bahnschrift Light SemiCondensed")
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.busca.setFont(font2)
        self.busca.setCursor(QCursor(Qt.PointingHandCursor))
        self.busca.setFocusPolicy(Qt.ClickFocus)
        self.busca.setLayoutDirection(Qt.LeftToRight)
        self.busca.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/btn/image/menu-busca.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busca.setIcon(icon1)
        self.busca.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.busca)

        self.categoria = QPushButton(self.topmenu)
        self.categoria.setObjectName(u"categoria")
        self.categoria.setMinimumSize(QSize(50, 0))
        self.categoria.setMaximumSize(QSize(16777215, 16777215))
        self.categoria.setFont(font2)
        self.categoria.setLayoutDirection(Qt.LeftToRight)
        self.categoria.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/btn/image/categori.png", QSize(), QIcon.Normal, QIcon.Off)
        self.categoria.setIcon(icon2)
        self.categoria.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.categoria)

        self.playlist = QPushButton(self.topmenu)
        self.playlist.setObjectName(u"playlist")
        self.playlist.setMinimumSize(QSize(50, 0))
        self.playlist.setMaximumSize(QSize(16777215, 16777215))
        self.playlist.setFont(font2)
        self.playlist.setLayoutDirection(Qt.LeftToRight)
        self.playlist.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/btn/image/play_list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.playlist.setIcon(icon3)
        self.playlist.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.playlist)

        self.mix = QPushButton(self.topmenu)
        self.mix.setObjectName(u"mix")
        self.mix.setMinimumSize(QSize(50, 0))
        self.mix.setMaximumSize(QSize(16777215, 16777215))
        self.mix.setFont(font2)
        self.mix.setLayoutDirection(Qt.LeftToRight)
        self.mix.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/btn/image/mix.png", QSize(), QIcon.Normal, QIcon.Off)
        self.mix.setIcon(icon4)
        self.mix.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.mix)

        self.preferencias = QPushButton(self.topmenu)
        self.preferencias.setObjectName(u"preferencias")
        self.preferencias.setFont(font2)
        self.preferencias.setLayoutDirection(Qt.LeftToRight)
        self.preferencias.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/btn/image/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.preferencias.setIcon(icon5)
        self.preferencias.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.preferencias)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)

        self.devbtn = QPushButton(self.topmenu)
        self.devbtn.setObjectName(u"devbtn")
        self.devbtn.setMinimumSize(QSize(50, 0))
        self.devbtn.setMaximumSize(QSize(16777215, 16777215))
        self.devbtn.setFont(font2)
        self.devbtn.setLayoutDirection(Qt.LeftToRight)
        self.devbtn.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"\n"
"\n"
"\n"
"\n"
"	padding:15px;\n"
"	border-bottom: 1px solid rgba(0, 0, 0,70);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	background-color: rgb(206, 206, 206);\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"font:  14pt \"Microsoft YaHei\";\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/btn/image/notify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.devbtn.setIcon(icon6)
        self.devbtn.setIconSize(QSize(25, 25))

        self.verticalLayout_8.addWidget(self.devbtn)


        self.horizontalLayout_5.addWidget(self.topmenu)


        self.verticalLayout_3.addWidget(self.categorias)


        self.horizontalLayout_3.addWidget(self.menu)

        self.content = QFrame(self.uimain)
        self.content.setObjectName(u"content")
        self.content.setMaximumSize(QSize(16777215, 16777215))
        self.content.setStyleSheet(u"background-image: url();\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(33, 37, 43, 255), stop:0.503888 rgba(40, 44, 52, 255), stop:1 rgba(57, 61, 68, 255));\n"
"color:rgba(255,255,255);")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.content)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.toptools = QFrame(self.content)
        self.toptools.setObjectName(u"toptools")
        self.toptools.setMaximumSize(QSize(16777215, 35))
        self.toptools.setStyleSheet(u"background-image: url();\n"
"border:0px;\n"
"background-color: rgba(0, 0, 0,0);\n"
"")
        self.toptools.setFrameShape(QFrame.StyledPanel)
        self.toptools.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toptools)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.toptools)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(40, 40))
        self.minimize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/minimize.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/minimize clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.minimize)

        self.maxmize = QPushButton(self.toptools)
        self.maxmize.setObjectName(u"maxmize")
        self.maxmize.setMinimumSize(QSize(40, 40))
        self.maxmize.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/max 1.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/max_ click.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.maxmize)

        self.exit = QPushButton(self.toptools)
        self.exit.setObjectName(u"exit")
        self.exit.setMinimumSize(QSize(40, 40))
        self.exit.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	background-image: url(:/fundo/close.png);\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: left;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 40); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	background-image: url(:/fundo/close clik.png);\n"
"background-color: rgba(0, 0, 0, 75); \n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.exit)


        self.verticalLayout_2.addWidget(self.toptools)

        self.contets = QStackedWidget(self.content)
        self.contets.setObjectName(u"contets")
        self.contets.setStyleSheet(u"background-image: url();\n"
"background-color: rgba(0, 0, 0,0);\n"
"")
        self.contets.setFrameShape(QFrame.StyledPanel)
        self.contets.setFrameShadow(QFrame.Raised)
        self.contetsPage1 = QWidget()
        self.contetsPage1.setObjectName(u"contetsPage1")
        self.verticalLayout_5 = QVBoxLayout(self.contetsPage1)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.PAG1 = QFrame(self.contetsPage1)
        self.PAG1.setObjectName(u"PAG1")
        self.PAG1.setStyleSheet(u"background-color: rgba(255, 255, 255,10);\n"
"")
        self.PAG1.setFrameShape(QFrame.StyledPanel)
        self.PAG1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.PAG1)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(40, 0, 0, 0)
        self.TOPBUT = QFrame(self.PAG1)
        self.TOPBUT.setObjectName(u"TOPBUT")
        self.TOPBUT.setMaximumSize(QSize(16777215, 60))
        self.TOPBUT.setStyleSheet(u"background-color: rgba(0, 0, 0,0);")
        self.TOPBUT.setFrameShape(QFrame.StyledPanel)
        self.TOPBUT.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.TOPBUT)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.TOPBUT)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(120, 40))
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 1px solid rgba(0, 0, 0,200);\n"
"\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton)

        self.pushButton_9 = QPushButton(self.TOPBUT)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(120, 40))
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setStyleSheet(u"\n"
"\n"
"\n"
"\n"
"QPushButton{\n"
"	\n"
"border-bottom: 3px solid rgba(255, 255, 255, 0); \n"
"\n"
"    background-color: rgba(0, 0, 0, 0); \n"
"	 text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color: rgba(0, 0, 0, 0); \n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"border-bottom: 1px solid rgb(0, 188, 242);\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.pushButton_9)

        self.horizontalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_8)


        self.verticalLayout_6.addWidget(self.TOPBUT)

        self.line = QFrame(self.PAG1)
        self.line.setObjectName(u"line")
        self.line.setMaximumSize(QSize(16777215, 1))
        self.line.setStyleSheet(u"background-color: rgba(0,0,0,50);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.adss = QStackedWidget(self.PAG1)
        self.adss.setObjectName(u"adss")
        self.adss.setMaximumSize(QSize(16777215, 16777215))
        self.adss.setStyleSheet(u"background-color: rgba(0, 0, 0, 0); ")
        self.adss.setFrameShape(QFrame.StyledPanel)
        self.adss.setFrameShadow(QFrame.Raised)
        self.adssPage1 = QWidget()
        self.adssPage1.setObjectName(u"adssPage1")
        self.horizontalLayout_6 = QHBoxLayout(self.adssPage1)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 50, 0)
        self.ads_esquerda = QFrame(self.adssPage1)
        self.ads_esquerda.setObjectName(u"ads_esquerda")
        self.ads_esquerda.setMinimumSize(QSize(565, 34))
        self.ads_esquerda.setMaximumSize(QSize(16777215, 16777215))
        self.ads_esquerda.setStyleSheet(u"")
        self.ads_esquerda.setFrameShape(QFrame.StyledPanel)
        self.ads_esquerda.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.ads_esquerda)
        self.verticalLayout_7.setSpacing(30)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 10, 0, 0)
        self.search_frame = QFrame(self.ads_esquerda)
        self.search_frame.setObjectName(u"search_frame")
        self.search_frame.setMinimumSize(QSize(0, 0))
        self.search_frame.setMaximumSize(QSize(16777215, 60))
        self.search_frame.setStyleSheet(u"background-color: rgba(0, 0, 0,0);\n"
"border-radius:5px;")
        self.search_frame.setFrameShape(QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.search_frame)
        self.horizontalLayout_14.setSpacing(10)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 10, 0)
        self.back_content = QPushButton(self.search_frame)
        self.back_content.setObjectName(u"back_content")
        self.back_content.setMinimumSize(QSize(50, 0))
        self.back_content.setMaximumSize(QSize(50, 50))
        self.back_content.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"\n"
"\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/btn/image/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_content.setIcon(icon7)
        self.back_content.setIconSize(QSize(30, 30))

        self.horizontalLayout_14.addWidget(self.back_content)

        self.label_5 = QLabel(self.search_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"\n"
"border-left:0px;\n"
"border-top:0px;\n"
"border-right:0px;\n"
"\n"
"border-radius:0px;")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_5)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Maximum, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_6)

        self.group_frame_seachr = QFrame(self.search_frame)
        self.group_frame_seachr.setObjectName(u"group_frame_seachr")
        self.group_frame_seachr.setMinimumSize(QSize(0, 0))
        self.group_frame_seachr.setMaximumSize(QSize(600, 16777215))
        self.group_frame_seachr.setStyleSheet(u"background-color: rgba(0, 0, 0,50);\n"
"border-radius:10px;")
        self.group_frame_seachr.setFrameShape(QFrame.StyledPanel)
        self.group_frame_seachr.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.group_frame_seachr)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.group_frame_seachr)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"border-bottom-left-radius:10;\n"
"border-bottom-right-radius:0;\n"
"border-top-left-radius:10;\n"
"border-top-right-radius:0;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setClearButtonEnabled(True)

        self.horizontalLayout_11.addWidget(self.lineEdit)

        self.btn_procurar = QPushButton(self.group_frame_seachr)
        self.btn_procurar.setObjectName(u"btn_procurar")
        self.btn_procurar.setMinimumSize(QSize(50, 0))
        self.btn_procurar.setMaximumSize(QSize(16777215, 50))
        self.btn_procurar.setFont(font1)
        self.btn_procurar.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	background-color:rgba(255,255,255,70);\n"
"border-bottom-left-radius:0;\n"
"border-bottom-right-radius:10;\n"
"border-top-left-radius:0;\n"
"border-top-right-radius:10;\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/btn/image/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_procurar.setIcon(icon8)

        self.horizontalLayout_11.addWidget(self.btn_procurar)


        self.horizontalLayout_14.addWidget(self.group_frame_seachr)


        self.verticalLayout_7.addWidget(self.search_frame)

        self.boasvindas_2 = QLabel(self.ads_esquerda)
        self.boasvindas_2.setObjectName(u"boasvindas_2")
        self.boasvindas_2.setMinimumSize(QSize(50, 0))
        self.boasvindas_2.setMaximumSize(QSize(16777215, 154))
        self.boasvindas_2.setFont(font1)
        self.boasvindas_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.boasvindas_2)

        self.line_2 = QFrame(self.ads_esquerda)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMaximumSize(QSize(16777215, 1))
        self.line_2.setStyleSheet(u"background-color: rgba(0,0,0,50);")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_7.addWidget(self.line_2)

        self.menu_frame = QFrame(self.ads_esquerda)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(0, 0))
        self.menu_frame.setMaximumSize(QSize(16777215, 16777215))
        self.menu_frame.setStyleSheet(u"\n"
"border: 0px;\n"
"border-radius:5px;")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.menu_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, -1, 0, -1)
        self.tableWidget = QTableWidget(self.menu_frame)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font1)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setStyleSheet(u"QWidget {  background-color: rgba(0, 0, 0,0)}\n"
"QHeaderView::section { background-color: rgb(53, 53, 53); border:none; width:45px; height: 50px; border-radius:0px; }\n"
" QTableWidget { gridline-color:rgba(0, 0, 0,0); border-radius:10px;  } QTableWidget QTableCornerButton::section { background-color: #646464; border-radius:0px; } QTableView:item {  border-radius:0px; } QTableView::item:selected{ background-color: rgba(0, 0, 0,255); color: rgb(255, 255, 255); } QScrollBar:horizontal { border: 1px solid #2A2929; background: #2A2929; height: 7px; margin: 0px 21px 0 21px; } QScrollBar::handle:horizontal { background: #646464; min-width: 5px; } QScrollBar::add-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: right; subcontrol-origin: margin; } QScrollBar::sub-line:horizontal { border: 1px solid #2A2929; background: #2A2929; width: 20px; subcontrol-position: left; subcontrol-origin: margin; } QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal { backg"
                        "round: none; } QScrollBar:vertical { border: none; background: rgb(45, 45, 68); width: 5px; margin: 15px 0 15px 0; border-radius: 0px; } /*  HANDLE BAR VERTICAL */ QScrollBar::handle:vertical { background-color: rgb(80, 80, 122); min-height: 30px; border-radius: 7px; } QScrollBar::handle:vertical:hover{ background-color: rgb(255, 0, 127); } QScrollBar::handle:vertical:pressed { background-color: rgb(185, 0, 92); } /* BTN TOP - SCROLLBAR */ QScrollBar::sub-line:vertical { border: none; background-color: rgb(59, 59, 90); height: 15px; border-top-left-radius: 7px; border-top-right-radius: 7px; subcontrol-position: top; subcontrol-origin: margin; } QScrollBar::sub-line:vertical:hover { background-color: rgb(255, 0, 127); } QScrollBar::sub-line:vertical:pressed { background-color: rgb(185, 0, 92); } /* BTN BOTTOM - SCROLLBAR */ QScrollBar::add-line:vertical { border: none; background-color: rgb(59, 59, 90); height: 15px; border-bottom-left-radius: 7px; border-bottom-right-radius: 7px; subcontrol-position: bottom; s"
                        "ubcontrol-origin: margin; } QScrollBar::add-line:vertical:hover { background-color: rgb(255, 0, 127); } QScrollBar::add-line:vertical:pressed { background-color: rgb(185, 0, 92); } /* RESET ARROW */ QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical { background: none; } QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical { background: none; }")
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(29)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(163)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_10.addWidget(self.tableWidget)


        self.verticalLayout_7.addWidget(self.menu_frame)


        self.horizontalLayout_6.addWidget(self.ads_esquerda)

        self.adss.addWidget(self.adssPage1)
        self.page_video_img = QWidget()
        self.page_video_img.setObjectName(u"page_video_img")
        self.page_video_img.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.page_video_img)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 5, 50, 10)
        self.frame_2 = QFrame(self.page_video_img)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 70))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.back_buscar = QPushButton(self.frame_2)
        self.back_buscar.setObjectName(u"back_buscar")
        self.back_buscar.setMinimumSize(QSize(50, 50))
        self.back_buscar.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"	\n"
"\n"
"\n"
"border: 1px solid rgba(255,255,255,30);\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/btn/image/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_buscar.setIcon(icon9)
        self.back_buscar.setIconSize(QSize(30, 30))

        self.horizontalLayout_9.addWidget(self.back_buscar)

        self.title_page2 = QLabel(self.frame_2)
        self.title_page2.setObjectName(u"title_page2")
        font3 = QFont()
        font3.setFamily(u"Bahnschrift Light SemiCondensed")
        font3.setBold(False)
        font3.setItalic(False)
        font3.setWeight(50)
        font3.setStrikeOut(False)
        font3.setKerning(False)
        font3.setStyleStrategy(QFont.PreferAntialias)
        self.title_page2.setFont(font3)
        self.title_page2.setScaledContents(False)

        self.horizontalLayout_9.addWidget(self.title_page2)

        self.horizontalSpacer_7 = QSpacerItem(1054, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.frame_image = QFrame(self.page_video_img)
        self.frame_image.setObjectName(u"frame_image")
        self.frame_image.setStyleSheet(u"")
        self.frame_image.setFrameShape(QFrame.StyledPanel)
        self.frame_image.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_image)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)

        self.video_label = QLabel(self.frame_image)
        self.video_label.setObjectName(u"video_label")
        self.video_label.setMinimumSize(QSize(0, 0))
        self.video_label.setMaximumSize(QSize(500, 400))
        self.video_label.setStyleSheet(u"")
        self.video_label.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.video_label)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_11.addWidget(self.frame_image)

        self.adss.addWidget(self.page_video_img)

        self.verticalLayout_6.addWidget(self.adss)

        self.frame = QFrame(self.PAG1)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 171))
        self.frame.setStyleSheet(u"background-color:rgba(255,255,255,0);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame)
        self.verticalLayout_9.setSpacing(5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 50, 30)
        self.progress_frame_3 = QFrame(self.frame)
        self.progress_frame_3.setObjectName(u"progress_frame_3")
        self.progress_frame_3.setMinimumSize(QSize(0, 0))
        self.progress_frame_3.setMaximumSize(QSize(16777215, 30))
        self.progress_frame_3.setStyleSheet(u"background-color: rgba(0, 0, 0,100);\n"
"border-radius:5px;\n"
"border: 1px solid rgba(0, 0, 0,70);")
        self.progress_frame_3.setFrameShape(QFrame.StyledPanel)
        self.progress_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.progress_frame_3)
        self.horizontalLayout_12.setSpacing(10)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(10, 0, 10, 0)
        self.clok_start = QLabel(self.progress_frame_3)
        self.clok_start.setObjectName(u"clok_start")
        self.clok_start.setFont(font1)
        self.clok_start.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"\n"
"border:none;\n"
"border-radius:0px;")

        self.horizontalLayout_12.addWidget(self.clok_start)

        self.progress_music = QProgressBar(self.progress_frame_3)
        self.progress_music.setObjectName(u"progress_music")
        self.progress_music.setMaximumSize(QSize(16777215, 7))
        self.progress_music.setCursor(QCursor(Qt.PointingHandCursor))
        self.progress_music.setStyleSheet(u"QProgressBar\n"
"{\n"
"    background: green;\n"
"    color: black;\n"
"    border-style: outset;\n"
"	border:none;\n"
"background-color:rgba(255,255,255,0);\n"
"\n"
"    border-radius: 2px;\n"
"\n"
"}\n"
"QProgressBar::chunk\n"
"{\n"
"     border-radius: 3px;\n"
"	background-color: rgb(92, 155, 179);\n"
"	border-top-left-radius:7px;\n"
"	 border-bottom-left-radius:7px;\n"
"\n"
"}")
        self.progress_music.setValue(24)
        self.progress_music.setTextVisible(False)

        self.horizontalLayout_12.addWidget(self.progress_music)

        self.clok_resta_ = QLabel(self.progress_frame_3)
        self.clok_resta_.setObjectName(u"clok_resta_")
        self.clok_resta_.setFont(font1)
        self.clok_resta_.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"\n"
"border:none;\n"
"border-radius:0px;")

        self.horizontalLayout_12.addWidget(self.clok_resta_)


        self.verticalLayout_9.addWidget(self.progress_frame_3)

        self.group_options_player = QFrame(self.frame)
        self.group_options_player.setObjectName(u"group_options_player")
        self.group_options_player.setMinimumSize(QSize(0, 100))
        self.group_options_player.setMaximumSize(QSize(16777215, 100))
        self.group_options_player.setStyleSheet(u"background-color: rgba(0, 0, 0,100);\n"
"border-radius:5px;\n"
"border: 1px solid rgba(0, 0, 0,70);")
        self.group_options_player.setFrameShape(QFrame.StyledPanel)
        self.group_options_player.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.group_options_player)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.text_and_vol = QFrame(self.group_options_player)
        self.text_and_vol.setObjectName(u"text_and_vol")
        self.text_and_vol.setMinimumSize(QSize(0, 0))
        self.text_and_vol.setMaximumSize(QSize(16777215, 30))
        self.text_and_vol.setStyleSheet(u"background:transparent;\n"
"border-radius:5px;\n"
"border: none;")
        self.text_and_vol.setFrameShape(QFrame.StyledPanel)
        self.text_and_vol.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.text_and_vol)
        self.horizontalLayout_13.setSpacing(10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.label_4 = QLabel(self.text_and_vol)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"background-color:rgba(255,255,255,0);\n"
"border-left:0px;\n"
"border-top:0px;\n"
"border-right:0px;\n"
"\n"
"border-radius:0px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.label_4)

        self.control_vol = QSlider(self.text_and_vol)
        self.control_vol.setObjectName(u"control_vol")
        self.control_vol.setMinimumSize(QSize(100, 0))
        self.control_vol.setMaximumSize(QSize(100, 16777215))
        self.control_vol.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.control_vol)

        self.set_titulo = QLabel(self.text_and_vol)
        self.set_titulo.setObjectName(u"set_titulo")
        self.set_titulo.setMinimumSize(QSize(0, 0))
        self.set_titulo.setStyleSheet(u"")
        self.set_titulo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.set_titulo)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addWidget(self.text_and_vol)

        self.control = QFrame(self.group_options_player)
        self.control.setObjectName(u"control")
        self.control.setMinimumSize(QSize(0, 0))
        self.control.setStyleSheet(u"background:transparent;\n"
"border: none;")
        self.control.setFrameShape(QFrame.StyledPanel)
        self.control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.control)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_3)

        self.play_music = QPushButton(self.control)
        self.play_music.setObjectName(u"play_music")
        self.play_music.setMinimumSize(QSize(30, 30))
        self.play_music.setFont(font1)
        self.play_music.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"	border: 1px solid rgba(0, 0, 0,70);\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,90);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,120);\n"
"\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/btn/image/play.png", QSize(), QIcon.Normal, QIcon.Off)
        self.play_music.setIcon(icon10)

        self.horizontalLayout_8.addWidget(self.play_music)

        self.pause_music = QPushButton(self.control)
        self.pause_music.setObjectName(u"pause_music")
        self.pause_music.setMinimumSize(QSize(40, 40))
        self.pause_music.setFont(font1)
        self.pause_music.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"	border: 1px solid rgba(0, 0, 0,70);\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,90);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,120);\n"
"\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/btn/image/pause.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pause_music.setIcon(icon11)

        self.horizontalLayout_8.addWidget(self.pause_music)

        self.stop_music = QPushButton(self.control)
        self.stop_music.setObjectName(u"stop_music")
        self.stop_music.setMinimumSize(QSize(30, 30))
        self.stop_music.setFont(font1)
        self.stop_music.setStyleSheet(u"\n"
"\n"
"QPushButton{\n"
"	\n"
"\n"
"	border-radius:10px;\n"
"\n"
"	border: 1px solid rgba(0, 0, 0,70);\n"
"background-color:rgba(255,255,255,70);\n"
"\n"
"\n"
"border-radius:7px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,90);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	\n"
"	\n"
"background-color:rgba(255,255,255,120);\n"
"\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/btn/image/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.stop_music.setIcon(icon12)

        self.horizontalLayout_8.addWidget(self.stop_music)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addWidget(self.control)


        self.verticalLayout_9.addWidget(self.group_options_player)


        self.verticalLayout_6.addWidget(self.frame)


        self.verticalLayout_5.addWidget(self.PAG1)

        self.contets.addWidget(self.contetsPage1)

        self.verticalLayout_2.addWidget(self.contets)


        self.horizontalLayout_3.addWidget(self.content)


        self.verticalLayout.addWidget(self.uimain)

        self.stackedWidget.addWidget(self.main)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(1)
        self.adss.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"Music Online Down", None))
        self.togle.setText(QCoreApplication.translate("Form", u"Menu", None))
        self.busca.setText(QCoreApplication.translate("Form", u"Busca", None))
        self.categoria.setText(QCoreApplication.translate("Form", u"Categorias", None))
        self.playlist.setText(QCoreApplication.translate("Form", u"PlayList", None))
        self.mix.setText(QCoreApplication.translate("Form", u"Mix", None))
        self.preferencias.setText(QCoreApplication.translate("Form", u"Preferencias", None))
        self.devbtn.setText(QCoreApplication.translate("Form", u"Atualiza\u00e7\u00f5es", None))
        self.minimize.setText("")
        self.maxmize.setText("")
        self.exit.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"Playing", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Conteudo", None))
        self.back_content.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Buscar Musica", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Busque sua musica aqui", None))
        self.btn_procurar.setText("")
        self.boasvindas_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:16pt;\">A experi\u00eancia Perfeita espera por voc\u00ea </span></p><p><span style=\" font-size:11pt;\">Vincule todas as suas musicas, baixe, veja letras e muito mais!</span></p></body></html>", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"url", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"thumb", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"desc", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"time", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"view", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"data", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"play", None));
        self.back_buscar.setText("")
        self.title_page2.setText("")
        self.video_label.setText("")
        self.clok_start.setText(QCoreApplication.translate("Form", u"0:00", None))
        self.clok_resta_.setText(QCoreApplication.translate("Form", u"0:00", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Volume", None))
        self.set_titulo.setText("")
        self.play_music.setText("")
        self.pause_music.setText("")
        self.stop_music.setText("")
    # retranslateUi

