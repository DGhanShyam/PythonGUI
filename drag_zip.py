import sys, os
from PyQt5.QtWidgets import QApplication, QFileDialog, QLabel, QMainWindow, QPushButton, QStyle, QVBoxLayout, QWidget
from PyQt5.QtCore import QByteArray, QTimer, Qt, QThread
from PyQt5.QtGui import QIcon, QMovie, QPixmap
import time, json
import zipfile
from win32 import win32api
paths=[]

class ImageLabel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label= QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('\n\n Drop Zip Files \n\n')
        self.label.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
        self.btn_icon = QPushButton('Save Location')
        self.btn_icon.clicked.connect(self.json_change)
        self.btn_icon.setIcon(QApplication.style().standardIcon(QStyle.SP_DialogSaveButton))
        self.movie = QMovie('photos/giphy.gif' , QByteArray(), self)


        layout= QVBoxLayout()

        layout.addWidget(self.btn_icon)
        layout.addWidget(self.label)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)        

    def json_change(self):
        with open ('json/new.json', 'r') as json_file:
            data= json.load(json_file)

        files= QFileDialog.getExistingDirectory (self, 'Select extraction location')
        print(files)

        data['dir']= files
        # print(data)

        with open ('json/new.json', 'w') as json_file:
            data= json.dump(data, json_file)
        json_file.close()

    def zipfile(self, path):
      
        if path != '':
            os.startfile(path)
            # st= os.path.basename(path)
            self.label.setText('FILES EXTRACTED : \n ' +path + '\n '  '\n' '\nDRAG NEW FILES TO EXTRACT ')
            self.movie.stop()        
            

        else:
            self.label.setText('' '\nDRAG NEW FILES TO EXTRACT ')    
            self.label.setText('Extract destination not selected : '  ' \n '    '\n '  '\n' '\nDRAG NEW FILES TO EXTRACT ')
            self.movie.stop()        
            

    def otherfile(self, path):
        self.movie.stop()        
        st= os.path.basename(path)
        self.label.setText('NOT A ZIP FILE: ' + st)            

    def loading(self):
        # self.label.setText('Extracting Files...')
        # self.movie.setCacheMode(QMovie.CacheAll)
        self.movie.setSpeed(300)
        QApplication.processEvents() 
        self.label.setMovie(self.movie)
        self.movie.start()        

class AppDemo(QMainWindow, QThread):
    def __init__(self,parent=None):
        super(AppDemo, self).__init__(parent=None)

        self.resize(400, 400)
        self.setWindowTitle('Zip Files')
        self.setAcceptDrops(True)
 
        mainLayout = QVBoxLayout()
 
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)

        w = QWidget()
        w.setLayout(mainLayout)       
        self.setCentralWidget(w)           
 
        # self.setLayout(mainLayout)
 
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent(self, event):
        
        if event.mimeData().hasUrls:
            event.setDropAction(Qt.CopyAction)
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):

        paths.clear()
        if event.mimeData().hasUrls:
            self.photoViewer.loading()        
            event.setDropAction(Qt.CopyAction)
            for url in event.mimeData().urls():
                if url.isLocalFile():
                    paths.append(str(url.toLocalFile()))
                else:
                    paths.append(str(url.toString()))   

            print(paths)
            file_path = event.mimeData().urls()[0].toLocalFile()

            # self.worker = AppDemo(self.unzip(paths))            # for wiki
            # self.worker.start()
            self.unzip(paths)
 
            event.accept()
        else:
            event.ignore()

    def unzip(self, lists):
        QApplication.processEvents() 
              
        for item in lists:
            if zipfile.is_zipfile(item) == True:

                user = win32api.GetUserName()
                link="C:/Users"
                with open ('json/new.json', 'r') as json_file:
                    json_data= json.load(json_file)
                data= json_data['dir']

                if data != '':
                    zip_ref = zipfile.ZipFile(item, 'r')
                    zip_ref.extractall(data)
                    QApplication.processEvents() 

                    self.photoViewer.zipfile(data)                     

                elif os.path.exists(os.path.join(link, user)):

                    self.run_unzip(link, user, item)    
                else:    
                    QApplication.processEvents() 
                    files= ''
                    files= QFileDialog.getExistingDirectory (self, 'Select extraction location')
                    print(files)
                    zip_ref = zipfile.ZipFile(item, 'r')
                    zip_ref.extractall(files)
                    self.photoViewer.zipfile(files) 
                    print('else')
                    

            else:
                self.photoViewer.otherfile(item)


    def run_unzip(self, link, user, item):
        QApplication.processEvents() 
        paths= os.path.join(link, user)   
        paths= paths + '\Documents'        
        zip_ref = zipfile.ZipFile(item, 'r')
        zip_ref.extractall(paths)
        os.startfile(paths)
        self.photoViewer.zipfile(paths)      


# def run(): 
#     app = QApplication(sys.argv)
#     demo = AppDemo()
#     demo.setWindowIcon(QIcon("photos/zz.jpeg"))
#     demo.show()
#     sys.exit(app.exec_())

# run()    