from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QFileDialog, QGridLayout, QHBoxLayout,QVBoxLayout, QLabel, QLineEdit, QMainWindow, QPushButton, QStyle, QTextEdit, QTimeEdit, QVBoxLayout, QWidget
import json
from PyQt5.QtCore import QByteArray, QTimer, Qt
import smtplib
from PyQt5.QtGui import QMovie
import time
from mov import movie


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setGeometry(910, 200, 600, 500)

        with open ('json/newfile.json', 'r') as file:
            data= json.load(file)

        sender_mail= data['sender_mail']
        sender_pass= data['sender_pass']

        self.from_label= QLabel("From :")
        self.from_label.setStyleSheet("font: 9pt;"  "font-weight: bold;" )
        self.from_label.setMaximumSize(70, 50)

        self.from_txt= QLineEdit(sender_mail)
        self.from_txt.setFixedWidth(380)
        self.from_txt.setFixedHeight(33)
        # self.from_txt.setReadOnly(True)
        self.from_txt.setStyleSheet("font: 8pt;"  "font-weight: bold;" )

        self.label1= QLabel("Subject :")
        self.label1.setStyleSheet("font: 9pt;"  "font-weight: bold;" )

        self.line1= QTextEdit()        
        self.line1.setMaximumSize(900,52)
        self.line1.setStyleSheet("font: 8pt;"  "font-weight: bold;" )
        
        self.label2= QLabel("Content :")
        self.label2.setStyleSheet("font: 9pt;"  "font-weight: bold;" )
        self.line2= QTextEdit()

        self.send_btn= QPushButton("SEND")
        self.send_btn.clicked.connect(self.send)
        self.send_btn.setStyleSheet("font: 9pt;"  "font-weight: bold;" )

        self.layout= QVBoxLayout()
        self.layout1= QHBoxLayout()

        self.layout.addLayout(self.layout1)

        self.layout1.addWidget(self.from_label)
        self.layout1.addWidget(self.from_txt, alignment= Qt.AlignLeft)

        self.layout.addWidget(self.label1)
        self.layout.addWidget(self.line1)
        self.layout.addWidget(self.label2)
        self.layout.addWidget(self.line2)
        self.layout.addWidget(self.send_btn, alignment= Qt.AlignRight)

        widget = QWidget()
        widget.setLayout(self.layout)

        self.setCentralWidget(widget)     


    def send(self):
        print(self.line1.toPlainText())
        print(self.line2.toPlainText())
        with open ('json/newfile.json', 'r') as file:
            data= json.load(file)   

        sender_mail= data['sender_mail']
        sender_pass= data['sender_pass']

        allmails= data['reciever_mail']
        print(allmails)
        valid_mails= []
        invalid_mails= []
        mail_subject= self.line1.toPlainText()
        mail_content= self.line2.toPlainText()       
        
        for item in range ( len(allmails) ) :
            self.movie = QMovie('g.gif' , QByteArray(), self)
            self.movie.setSpeed(100)
            self.label2.setMovie(self.movie)
            self.movie.start() 
            QApplication.processEvents()         
            time.sleep(3)     
            each_mail= data['reciever_mail'][item]

            print("mail: " +data['reciever_mail'][item])            

            sent_from = sender_mail
            to = each_mail      #, 'bill@gmail.com'  
            subject = mail_subject
            body =  mail_content+ "\n\n- VITAM"

            email_text = """\
            From: %s
            To: %s
            Subject: %s

            %s
            """ % (sent_from, ", ".join(to), subject, body)

            try:
                server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                server.ehlo()
                server.login(sender_mail, sender_pass)
                server.sendmail(sent_from, to, email_text)
                server.close()

                print ('Email sent!')
                valid_mails.append(each_mail)
            except:
                print('Something went wrong...')
                invalid_mails.append(each_mail)
        self.label2.setText('Content :')


    def signal(self):
        self.movie = QMovie('photos/giphy.gif' , QByteArray(), self)
        self.movie.setSpeed(100)
        # QApplication.processEvents() 
        self.label2.setMovie(self.movie)
        self.movie.start() 
        # self.send()                                   

    def stop(self):
        self.movie.stop()         


# if __name__ == "__main__":
#     import sys

#     app = QApplication(sys.argv)
#     app.setApplicationName('Mail')

#     main = MyWindow()
#     main.setWindowIcon(QtGui.QIcon("photos/mail.svg"))

#     main.show()

#     sys.exit(app.exec_())