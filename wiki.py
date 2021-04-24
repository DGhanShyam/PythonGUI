import schedule, time
import pygetwindow as pgw
import sys, os
from PyQt5.QtWidgets import QApplication, QFileDialog, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStyle, QTimeEdit, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QIcon, QMovie, QPixmap


class Break_reminder(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()                              # grid matrix layout
        layout1 = QVBoxLayout()                              # grid matrix layout
        
        self.search_text = QLineEdit()
        self.search_text.setMaxLength(40)
        self.search_text.setFixedSize(270, 50)
        self.search_text.setPlaceholderText("Enter reminder message")   


        layout1.addWidget(self.search_text)

        widget = QWidget()
        widget.setLayout(layout1)
        self.setCentralWidget(widget)                   



def run(): 
    app = QApplication(sys.argv)
    demo = Break_reminder()
    demo.setWindowIcon(QIcon("photos/zz.jpeg"))
    demo.show()
    sys.exit(app.exec_())

run()    