import sys
from PyQt5.QtWidgets import *# QApplication, QHBoxLayout, QLabel, QWidget #QApplication, QLabel, QMainWindow, QToolBar, QAction, QStatusBar
from PyQt5.QtCore import QSize, QTimer, Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import time
# from PyQt5.QtGui import QIcon
# PyQt5.QtCore.QSize

class movie(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent=None)
    
        # self.setSizePolicy(QtWidgets.QSizePolicy.Expa8nding, QtWidgets.QSizePolicy.Expanding)
        self.setGeometry(400, 400, 400, 400)

        self.label= QLabel()
        self.movie = QtGui.QMovie('giphy-downsized.gif' , QtCore.QByteArray(), self)
        # self.movie.setCacheMode(QMovie.CacheAll)
        # self.movie.setSpeed(100)

        self.label.setMovie(self.movie)
        self.movie.start()
        # QTimer.singleShot(20, self.movie.stop())                                            
        time.sleep(4)
        layout= QHBoxLayout()
        layout.addWidget(self.label)
            
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

# app = QApplication(sys.argv)

# window = movie()
# # window.setWindowIcon(QtGui.QIcon("beans.png"))
# window.setWindowFlags(Qt.FramelessWindowHint)
# window.show()
# app.exec_()