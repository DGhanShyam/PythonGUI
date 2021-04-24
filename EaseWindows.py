import sys,threading
from PyQt5.QtWidgets import * #QAction, QApplication, QHBoxLayout, QMainWindow, QPushButton, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt, pyqtSlot, QThread
from PyQt5 import QtCore, QtGui
import time, psutil
from drag_zip import AppDemo
from mail import MyWindow
import time
import psutil
from hurry.filesize import size
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import urllib

class Widgets(QMainWindow):

    def __init__(self,parent=None):
        super(Widgets, self).__init__(parent=None)
        self.TIME_LIMIT = 1000
        self.setGeometry(1620, 40, 250,600)
        # self.setStyleSheet("background-color: rgb(235,225,190);")        
                                    #rgb(235,225,190)
        self.splash = QSplashScreen(QPixmap('photos/worm-s-eye-view-of-high-rise-buildings-1461374.jpg'))
        # self.splash.move(100,100)
        # self.splash.setGeometry(100, 100, 1400, 900)
        self.splash.show()
        QTimer.singleShot(2, self.splash.close)        

        self.x_thread = threading.Thread(target=self.bytescal )
        self.y_thread = threading.Thread(target=self.progressBar )

        Widgetslayout= QVBoxLayout()

        media_layout= QHBoxLayout()
        search_layout= QHBoxLayout()
        search_files_layout= QHBoxLayout()
        footer_layout= QHBoxLayout()

        self.btn = QPushButton(QtGui.QIcon("photos/Logo_Twitter_bird-256.webp"), '')
        self.btn.clicked.connect(self.browser)
        self.btn1 = QPushButton(QtGui.QIcon("photos/Logo_LinkedIn-256.webp"), '')
        # self.btn1.clicked.connect(self.browser)        
        self.btn2 = QPushButton(QtGui.QIcon("photos/Logo_facebook-256.webp"), '')         #social icons
        # self.btn2.clicked.connect(self.browser)        
        self.btn3 = QPushButton(QtGui.QIcon("photos/Logo_Youtube-256.webp"), '')
        # self.btn3.clicked.connect(self.browser)
        self.btn4 = QPushButton(QtGui.QIcon("photos/Logo_reddit_robot-256.webp"), '')
        # self.btn4.clicked.connect(self.browser)

        self.text_feild = QLineEdit()
        self.text_feild.setMaxLength(40)
        self.text_feild.setPlaceholderText("Select icons below to search")     # search feild
        self.text_feild.returnPressed.connect(self.return_pressed)        

        self.wiki = QPushButton(QtGui.QIcon("photos/w.jpeg"), '')
        self.github = QPushButton(QtGui.QIcon("photos/git.jpeg"), '')          # search buttons
        self.google = QPushButton(QtGui.QIcon("photos/google.jpeg"), '')  

        self.search_icon= QPushButton(QtGui.QIcon("photos/searchicon.jpeg"), '')

        self.search_text = QLineEdit()
        self.search_text.setMaxLength(40)
        self.search_text.setPlaceholderText("Search  files")         
        self.search_text.returnPressed.connect(self.return_pressed)     

        self.manage_files= QPushButton(QtGui.QIcon("photos/folder.png"),'Manage Files')   

        self.reminder= QPushButton(QtGui.QIcon("photos/rem.png"),'Reminder')   
        # self.reminder.clicked.connect(self.progressBar)

        self.zip_files= QPushButton(QtGui.QIcon("photos/zz.jpeg"),'Extract Files')   
        self.zip_files.clicked.connect(self.zip_window)        

        self.send_mail= QPushButton(QtGui.QIcon('photos/mail.svg'),'Send Mail')   
        self.send_mail.clicked.connect(self.mailing)

        self.ram_button= QPushButton(QtGui.QIcon('photos/smartphone-ram.png'),'Ram Usage')
        self.ram_button.clicked.connect(self.show_progress_bar)

        self.progress = QProgressBar(self)
        # self.progress.sho()
        #QTimer.singleShot(12, self.progressBar)              

        self.netspeed= QLabel()
        self.netspeed.setStyleSheet("font: 10pt;"  "font-weight: bold;" )

        self.easewindow = QLabel('Ease Windows')
        self.easewindow.setStyleSheet("font: 10pt;"  "font-weight: bold;" )

        self.settings= QPushButton(QtGui.QIcon("photos/1.webp"), '')
        self.close= QPushButton(QtGui.QIcon("photos/close.png"), '')
        self.close.clicked.connect(self.close_application)
        # self.close.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogCloseButton))
            
        self.btn.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 13px;"
                            "background-color: white;"
                            )
        self.btn1.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )
        self.btn2.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )
        self.btn3.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )
        self.btn4.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )
        self.text_feild.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 6px;"
                        "border-radius: 10px;"
                        "background-color: #F5F5F5;"
                        )
        self.wiki.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )           
        self.github.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 8px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )         
        self.google.setStyleSheet( 
                        "border-style: inline;"
                        "border-width: 10px;"
                        "border-radius: 13px;"
                        "background-color: white;"
                        )   
        self.search_text.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #F5F5F5;"
                            )          
        self.search_icon.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: white;"
                            )            
        self.settings.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 1px;"
                            "border-radius: 1px;"
                            "background-color: light grey;"
                            )            
        self.close.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 1px;"
                            "border-radius: 1px;"
                            )    
        self.manage_files.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #B8B8B8;"
                            "font-weight:bold;"
                            )  
        self.reminder.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #B8B8B8;"
                            "font-weight:bold;"
                            )  
        self.zip_files.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #B8B8B8;"
                            "font-weight:bold;"
                            )          
        self.send_mail.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #B8B8B8;"
                            "font-weight:bold;"
                            )           
        self.ram_button.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 8px;"
                            "border-radius: 10px;"
                            "background-color: #B8B8B8;"
                            "font-weight:bold;"
                            )          
        self.progress.setStyleSheet(
                            "border-style: inline;"
                            "border-width: 2px;"
                            "border-radius: 4px;"
                            "background-color:white;"
                            "font-weight:bold;"
                             "text-align: center;"
                            )  
        QProgressBar.setStyleSheet(self, 
                           "QProgressBar::hover {"
                           "background-color:  #B8B8B8;  }" );                            

        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        Widgetslayout.addLayout(media_layout)
        media_layout.addWidget(self.btn)
        media_layout.addWidget(self.btn1)
        media_layout.addWidget(self.btn2)
        media_layout.addWidget(self.btn3)
        media_layout.addWidget(self.btn4)

        Widgetslayout.addItem(spacerItem)
        Widgetslayout.addWidget(self.text_feild)

        Widgetslayout.addLayout(search_layout)

        search_layout.addWidget(self.wiki)
        search_layout.addWidget(self.github)
        search_layout.addWidget(self.google) 

        Widgetslayout.addItem(spacerItem)
        Widgetslayout.addLayout(search_files_layout)      

        search_files_layout.addWidget(self.search_icon)
        search_files_layout.addWidget(self.search_text)

        Widgetslayout.addWidget(self.manage_files)
        Widgetslayout.addWidget(self.reminder)
        Widgetslayout.addWidget(self.zip_files)
        Widgetslayout.addWidget(self.send_mail)
        Widgetslayout.addWidget(self.progress)
        # Widgetslayout.addWidget(self.ram_button)
        Widgetslayout.addWidget(self.netspeed, alignment= Qt.AlignCenter)

        Widgetslayout.addLayout(footer_layout)
        
        footer_layout.addWidget(self.close, alignment=Qt.AlignBottom)
        footer_layout.addWidget(self.settings, alignment=Qt.AlignBottom)        
        footer_layout.addWidget(self.easewindow, alignment=Qt.AlignBottom)

        w = QWidget()
        w.setLayout(Widgetslayout)

        self.setCentralWidget(w)  

        self.x_thread.start()
        self.y_thread.start()

    def return_pressed(self):
        text_data= self.text_feild.text()
        print(text_data)

    def close_application(self):
        self.x_thread._stop()
        self.y_thread._stop()
        time.sleep(2)
        app.exit()                         #   app.closeAllWindows()    but still background run, for notif'n purpose

    def browser(self):
    
        self.boolean= True
        if self.boolean == True:
            try:
                self.driver1 = webdriver.Firefox(executable_path= 'webdriver/geckodriver.exe')
                self.boolean= False                
                self.transfer(self.driver1)     
            except :
                print('firefiox didnt work')     
                  
        if self.boolean == True:    
            try:
                self.driver2 = webdriver.Chrome(executable_path= 'webdriver/chromedriver.exe')
                self.boolean= False
                self.transfer(self.driver2)  
            except :
                print('chrome didnt work')    

        if self.boolean == True:
            try:
                self.driver3 = webdriver.Edge(executable_path= 'webdriver/msedgedriver.exe')
                self.boolean= False
                self.transfer(self.driver3)  
            except :
                print('Edge didnt work')        

    def transfer(self, drive):
        self.driver= drive
        self.driver.get("http://www.facebook.com")
        user_name = 'shyamsundarrao54@gmail.com'
        password = 'shyam4243'
        element = self.driver.find_element_by_id("email")
        element.send_keys(user_name)
        element = self.driver.find_element_by_id("pass")
        element.send_keys(password)
        element.send_keys(Keys.RETURN)                
        
    def zip_window(self):
        # self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.zip = AppDemo()
        self.zip.setWindowIcon(QIcon('photos/zz.jpeg'))
        self.zip.show() 

    def mailing(self):
        # self.dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.mail = MyWindow()
        self.mail.setWindowIcon(QIcon('photos/mail.svg'))
        self.mail.show() 

    def show_progress_bar(self):    
        self.ram_button.hide()
        self.progress.show()
        self.progressBar()

        self.progress.hide()      
        self.ram_button.show()  
        # window.hide()
        # time.sleep(2)   
        # run()

    def progressBar(self):
        count = 0
        while True:
            # count += 1
            time.sleep(1.2)
            # QApplication.processEvents()         
            self.progress.setValue( int(psutil.virtual_memory().percent))

    def bytescal(self):
        # QApplication.processEvents()         
        self.t= 0
        while True:
            # QApplication.processEvents()         
            self.total = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv        
            self.send_stat(self.total- self.t ) 
            self.t= self.total
    def send_stat(self, bytesize):
        time.sleep(2)
        self.speed=  str(size(bytesize)) 
        self.netspeed.setText(self.speed)
            

app = QApplication(sys.argv)
window = Widgets()
window.setWindowFlags(Qt.FramelessWindowHint)
window.show()
# thread = AThread()
# thread.start()
app.exec_()                